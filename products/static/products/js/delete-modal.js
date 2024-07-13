    // Handle delete confirmation modal

document.addEventListener('DOMContentLoaded', function() {
    $('#deleteProductModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var url = button.data('url');
        var modal = $(this);

        $('#confirmDeleteBtn').off('click').on('click', function () {
            $('<form>', {
                "method": "POST",
                "action": url
            }).append($('#delete-product-form').html()).appendTo('body').submit();
        });
    });
});