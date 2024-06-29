function toggleEditForm(reviewId) {
    var x = document.getElementById("editForm" + reviewId);
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    function initializeStarRating(container) {
        const stars = container.querySelectorAll('.star');
        const ratingInputs = container.querySelectorAll('input[type="radio"]');

        stars.forEach((star, index) => {
            star.addEventListener('mouseover', () => {
                for (let i = 0; i < stars.length; i++) {
                    stars[i].style.color = i <= index ? '#c9c2b2' : '#94857b';
                }
            });

            star.addEventListener('click', () => {
                for (let i = 0; i < stars.length; i++) {
                    stars[i].style.color = i <= index ? 'gold' : '#94857b';
                    ratingInputs[i].checked = i <= index;
                }
            });
        });

        container.addEventListener('mouseleave', () => {
            const checkedIndex = Array.from(ratingInputs).findIndex(input => input.checked);
            for (let i = 0; i < stars.length; i++) {
                stars[i].style.color = i <= checkedIndex ? 'gold' : '#94857b';
            }
        });
    }

    const ratingContainers = document.querySelectorAll('.rating-container');
    ratingContainers.forEach(container => {
        initializeStarRating(container);
    });
});