$(document).ready(function() { 

    //Allows user to add more ingredient fields
    $('#add_ing_field').click(function() {
        $('<input placeholder="1tbsp avocado oil" name="ingredients" type="text" class="validate"></input>').insertBefore(this);
    });
    
    //Allows user to remove last ingredient field
    $('#remove_ing_field').click(function() {
        $('#ingredients_list input').last().remove();
    }); 



    // Code for the hamburger menu, comes from this tutorial: https://www.youtube.com/watch?v=dIyVTjJAkLw
    //const menuBtn = document.querySelector('.menu-button');
    let menuOpen = false;
    let delRecipeOpen = false;

    //Call toggleMenu function on click
    $("#mainNavBtn").on("click", toggleMenu());


    function toggleMenu() {
        //const menuBtn = $('.menu-button')
        $('#mainNavBtn').click(function() {
            if(!menuOpen) {
                $('.menu-button').addClass('open');
                $('.navRow').css({'visibility': 'visible', 'opacity': '1'});
                menuOpen = true;
            } else {
                $('.menu-button').removeClass('open');
                $('.navRow').css({'visibility': 'hidden', 'opacity': '0'});
                menuOpen = false;
            }
        })
    };
    /*
    menuBtn.addEventListener('click', () => {
        if(!menuOpen) {
            menuBtn.classList.add('open');
            $('.navRow').css({'visibility': 'visible', 'opacity': '1'});
            menuOpen = true;
        } else {
            menuBtn.classList.remove('open');
            $('.navRow').css({'visibility': 'hidden', 'opacity': '0'});
            menuOpen = false;
        }
    })*/

    function deleteRecipe() {
        if(!delRecipeOpen) {
            $('#popup-delete').addClass('popup-open');
            delRecipeOpen = true;
        } else {
            $('#popup-delete').removeClass('popup-open');
            delRecipeOpen = false;
        }
    }

    $("#del-recipe").on("click", deleteRecipe());    


});