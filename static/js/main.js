$(document).ready(function() { 

    //var menuOpen = false;

    //Allows user to add more ingredient fields
    $('#add_ing_field').click(function() {
        $('<input placeholder="1tbsp avocado oil" name="ingredients" type="text" class="validate"></input>').insertBefore(this);
    });
    
    //Allows user to remove last ingredient field
    $('#remove_ing_field').click(function() {
        $('#ingredients_list input').last().remove();
    }); 


    //Open main navigation
/*
    function toggleMenu() {
        if(!menuOpen) {
            $('.navRow').css('visibility', 'visble');
            menuOpen = true;
        } else {
             $('.navRow').css('visibility', 'hidden');
             menuOpen = false;
        }
    }

    $('#mainNavBtn').click(function() {
        toggleMenu();
    });
*/




    // Code for the hamburger menu, comes from this tutorial: https://www.youtube.com/watch?v=dIyVTjJAkLw
    const menuBtn = document.querySelector('.menu-button');
    let menuOpen = false;
    menuBtn.addEventListener('click', () => {
        if(!menuOpen) {
            menuBtn.classList.add('open');
            $('.navRow').css('visibility', 'visible').fadeIn('slow');
            menuOpen = true;
        } else {
            menuBtn.classList.remove('open');
            $('.navRow').css('visibility', 'hidden').fadeOut('slow');
            menuOpen = false;
        }
    })


});