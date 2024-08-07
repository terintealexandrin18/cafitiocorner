from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile
from wishlist.models import Wishlist
from django.db.models.functions import Lower


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all().annotate(
        avg_rating=Avg('reviews__rating')
    )
    query = None
    categories = None
    sort = 'name'
    direction = 'asc'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'rating':
                sortkey = 'avg_rating'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(
                Q(category__name__in=categories) |
                Q(category__parent__name__in=categories)
            )
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search "
                               "criteria!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
            products = products.filter(queries)

    if not request.GET.get('sort'):
        products = products.order_by('name')

    for product in products:
        reviews = product.reviews.all()
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        product.average_rating = round(average_rating)
        product.filled_stars = range(int(product.average_rating))
        product.empty_stars = range(5 - int(product.average_rating))

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        user_wishlist = Wishlist.objects.filter(
            user_profile=user_profile
        ).values_list('product_id', flat=True)
    else:
        user_wishlist = []

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': page_obj,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
        'user_wishlist': list(user_wishlist),
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details including reviews
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    user_wishlist = []
    review_form = None

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        user_wishlist = Wishlist.objects.filter(
            user_profile=user_profile
        ).values_list('product_id', flat=True)

        if request.method == 'POST' and 'submit_review' in request.POST:
            review_form = ReviewForm(data=request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.product = product
                new_review.user = request.user
                new_review.save()
                messages.success(request, 'Review successfully added!')
                return redirect('product_detail', product_id=product_id)
            else:
                messages.error(
                    request, 'Failed to add review. Please '
                    'ensure the form is valid.')
        else:
            review_form = ReviewForm()

    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    average_rating = round(average_rating)

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'average_rating': average_rating,
        'user_wishlist': list(user_wishlist),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure '
                'the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure '
                'the form is valid.'
            )
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
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def submit_review(request, product_id):
    """
    Submit a review for a product
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    average_rating = round(average_rating)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(
                request, 'Failed to add review. '
                'Please ensure the form is valid.')
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': form,
        'average_rating': average_rating,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def edit_review(request, review_id):
    """
    Edit an existing review
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('product_detail', product_id=review.product.id)
    else:
        form = ReviewForm(instance=review)
    return redirect('product_detail', product_id=review.product.id)


@login_required
def delete_review(request, review_id):
    """
    Delete an existing review
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product_id = review.product.id
    review.delete()
    messages.success(request, 'Review deleted successfully!')
    return redirect('product_detail', product_id=product_id)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if Wishlist.objects.filter(user_profile=user_profile,
                               product=product).exists():
        messages.info(request, f'{product.name} is already in your Wishlist.')
    else:
        Wishlist.objects.create(user_profile=user_profile, product=product)
        messages.success(request, f'{product.name} added to '
                         'Wishlist successfully!')
    return redirect(reverse('products'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(
        user_profile=user_profile, product=product
    )
    wishlist_item.delete()
    messages.success(
        request, f'{product.name} has been successfully removed.'
    )
    return redirect(reverse('wishlist'))
