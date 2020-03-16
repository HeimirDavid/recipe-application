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
    $("#mainNavBtn").on("click", toggleMenu()); //Might be unneccessary

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
  

    function deleteRecipe() {
        $('#del-recipe').click(function() {
            if(!delRecipeOpen) {
                $('#popup-delete').show();
                delRecipeOpen = true;
            } else {
                $('#popup-delete').hide();
                delRecipeOpen = false;
            }
        });
    };

    $("#del-recipe").on("click", deleteRecipe());    //Might be unneccessary

    $('#cancel').click(function() {
        $('#popup-delete').hide();
        delRecipeOpen = false;
    });

    $('#confirm-del').click(function() {
        $('#popup-delete').hide();
        delRecipeOpen = false;
    });


});