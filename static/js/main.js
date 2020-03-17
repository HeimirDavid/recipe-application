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

    let menuOpen = false;
    let delRecipeOpen = false;

 
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
    

    $('#del-recipe').click(function() {
        if(!delRecipeOpen) {
            $('#popup-delete').show();
            delRecipeOpen = true;
        } else {
            $('#popup-delete').hide();
            delRecipeOpen = false;
        }
    });


    //$("#del-recipe").on("click", deleteRecipe());    //Might be unneccessary

    $('#cancel').click(function() {
        $('#popup-delete').hide();
        delRecipeOpen = false;
    });

    $('#confirm-del').click(function() {
        $('#popup-delete').hide();
        delRecipeOpen = false;
    });


    ////////////////////////////////////
    let loginWindow = false;
    $('#login-menu-btn').click(function() {
        if(!loginWindow) {
            $('.login-container').fadeIn('fast');
            loginWindow = true;
            console.log("Open Login")
            $('.register-container').fadeOut('fast');
            registerWindow = false;
        } else {
            $('.login-container').fadeOut('fast');
            loginWindow = false;
            console.log("Hide Login")
        }
    });

    $('#close_logo').click(function() {
        if(!loginWindow) {
            $('.login-container').fadeIn('fast');
            loginWindow = true;
        } else {
            $('.login-container').fadeOut('fast');
            loginWindow = false;
        }
    });

    //////////////////////////////////////

    let registerWindow = false;
    $('.ToggleRegLog').click(function() {
        if(!registerWindow) {
            $('.register-container').fadeIn('fast');
            registerWindow = true;
            $('.login-container').fadeOut('fast');
            loginWindow = false;
            console.log("Open Register Window")
        } else {
            $('.register-container').fadeOut('fast');
            registerWindow = false;
            $('.login-container').fadeIn('fast');
            loginWindow = true;
            console.log("Close Register Window")
        }
    });

    $('#close_register').click(function() {
        if(!registerWindow) {
            $('.register-container').fadeIn('fast');
            registerWindow = true;
        } else {
            $('.register-container').fadeOut('fast');
            registerWindow = false;
        }
    });

});