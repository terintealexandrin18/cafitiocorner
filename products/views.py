from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.filter(status='approved')
    average_rating = product.reviews.aggregate(average=Avg('rating'))['average'] or 0

    user_rating = None
    if request.user.is_authenticated:
        user_rating = Review.objects.filter(product=product, user=request.user).first()

    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
        'user_rating': user_rating,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_rating(request, product_id):
    """ Add a rating to a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        Review.objects.create(product=product, user=request.user, rating=rating, status='approved')
        messages.success(request, 'Rating submitted successfully.')
    return redirect('product_detail', product_id=product_id)


@login_required
def add_review(request, product_id):
    """ Add a review to a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Review.objects.create(product=product, user=request.user, comment=comment, status='pending')
        messages.success(request, 'Review submitted successfully. It will be visible once approved.')
    return redirect('product_detail', product_id=product_id)


@login_required
def edit_review(request, review_id):
    """ Edit a review """
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.user:
        messages.error(request, "You do not have permission to edit this review.")
        return redirect('product_detail', product_id=review.product.id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        review.comment = comment
        review.status = 'pending'  
        review.save()
        messages.success(request, 'Review updated successfully. It will be visible once approved.')
        return redirect('product_detail', product_id=review.product.id)
    context = {'review': review}
    return render(request, 'products/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.user:
        messages.error(request, "You do not have permission to delete this review.")
        return redirect('product_detail', product_id=review.product.id)
    review.delete()
    messages.success(request, 'Review deleted successfully.')
    return redirect('product_detail', product_id=review.product.id)