//  Js for dropdown nav on mobile  //    

$(document).ready(function(){
    // Close any open submenus when a new parent is clicked
    $('.dropdown-submenu > a').on("click", function(e){
        var submenu = $(this).next('.dropdown-menu');
        
        // Close any other open submenus
        $('.dropdown-submenu .dropdown-menu').not(submenu).slideUp();

        // Toggle the clicked submenu
        submenu.slideToggle();

        e.stopPropagation();
        e.preventDefault();
    });

    // Close submenus when clicking outside
    $(document).on('click', function(){
        $('.dropdown-submenu .dropdown-menu').slideUp();
    });

    // Prevent the closing of dropdown on clicking inside the menu
    $('.dropdown-menu').on('click', function(e){
        e.stopPropagation();
    });
});