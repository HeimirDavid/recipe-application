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

    //$('#mainNavBtn').on("click", toggleMenu());


    //function toggleMenu() {
        //toggle the main navigation. both open and close the hamburger (adding 'open' class) and the menu
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
        //Close the main menu
        $('.menu-button').removeClass('open');
        $('.navRow').css({'visibility': 'hidden', 'opacity': '0'});
        menuOpen = false;

        if(!loginWindow) { //show the login window/close the register window
            $('.login-container').fadeIn('fast');
            $('.register-container').fadeOut('fast');
            loginWindow = true;
            registerWindow = false;
        } else { //hide the login contaniner
            $('.login-container').fadeOut('fast');
            loginWindow = false;
        }
    });

    $('#close_logo').click(function() {
        if(loginWindow) { 
            $('.login-container').fadeOut('fast');
            loginWindow = false;
        } /*else {
            $('.login-container').fadeIn('fast');
            loginWindow = true;
        }*/
    });

    //////////////////////////////////////

    let registerWindow = false;
    $('.ToggleRegLog').click(function() {
        if(!registerWindow) {
            $('.register-container').fadeIn('fast');
            $('.login-container').fadeOut('fast');
            loginWindow = false;
            registerWindow = true;
            console.log("Open Register Window")
        } else {
            $('.register-container').fadeOut('fast');
            $('.login-container').fadeIn('fast');
            loginWindow = true;
            registerWindow = false;
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

    
    function blink_text(num) {
        for(i = 0; i < num; i++) {
            $('.flash-message').fadeOut(500);
            $('.flash-message').fadeIn(500);
        }
    }

    blink_text(4);
    /*
    function blink_text() {
        $('.flash-message').fadeOut(500);
        $('.flash-message').fadeIn(500);
        $('.flash-message').fadeOut(500);
        $('.flash-message').fadeIn(500);
        $('.flash-message').fadeOut(500);
        $('.flash-message').fadeIn(500);
    }

    blink_text();*/

    
});