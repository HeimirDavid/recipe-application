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
    // Has been modified for my needs and added some more functionality to open and close the menu
    // as well as open and close (X) the hamburger.
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
    });
    
    //Open and close a warning popup before you delete a recipe
    $('#del-recipe').click(function() {
        if(!delRecipeOpen) {
            $('#popup-delete').fadeIn('fast');
            delRecipeOpen = true;
        } else {
            $('#popup-delete').fadeOut('fast');
            delRecipeOpen = false;
        }
    });

    //Close the delete warning popup by pressing the cancel or delete button  
    $('.close-del-popup').click(function() {
        $('#popup-delete').fadeOut('fast');
        delRecipeOpen = false;
    });

    /*****  Login Window  *****/
    let loginWindow = false;

    $('#login-menu-btn').click(function() {
        //Close the main menu when login/register is pressed in the menu
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
    // Close the login container when the X is pressed
    $('#close_logo').click(function() {
        if(loginWindow) { 
            $('.login-container').fadeOut('fast');
            loginWindow = false;
        } 
    });

    /*****  Register Window  *****/

    // Toggle between the register and the login window when 'ToggleRegLog' is clicked.
    // This by using flags and fade the login/register containers in and out.
    let registerWindow = false;
    $('.ToggleRegLog').click(function() {
        if(!registerWindow) {
            $('.register-container').fadeIn('fast');
            $('.login-container').fadeOut('fast');
            loginWindow = false;
            registerWindow = true;
            console.log("Open Register Window");
        } else {
            $('.register-container').fadeOut('fast');
            $('.login-container').fadeIn('fast');
            loginWindow = true;
            registerWindow = false;
            console.log("Close Register Window");
        }
    });

    // Close the register window by pressing the X in the right corner which has the ID of 'close_register'
    $('#close_register').click(function() {
        if(!registerWindow) {
            $('.register-container').fadeIn('fast');
            registerWindow = true;
        } else {
            $('.register-container').fadeOut('fast');
            registerWindow = false;
        }
    });

    //Blink the flash message to add attention to it. this by fading it in and out with 500 ms.
    function blink_text(num) {
        for(i = 0; i < num; i++) {
            $('.flash-message').fadeOut(500);
            $('.flash-message').fadeIn(500);
        }
    }

    blink_text(4);
   

    
});