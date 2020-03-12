$(document).ready(function() { 


    //Allows user to add more ingredient fields
    $('#add_ing_field').click(function() {
        $('<input placeholder="1tbsp avocado oil" name="ingredients" type="text" class="validate"></input>').insertBefore(this);
    });
    
    //Allows user to remove last ingredient field
    $('#remove_ing_field').click(function() {
        $('#ingredients_list input').last().remove();
    }); 


    //Open main navigation
    $('#mainNavBtn').click(function() {
        console.log('Jibbicola');
    });


});


// Code for the hamburger menu, comes from this tutorial: https://www.youtube.com/watch?v=dIyVTjJAkLw
const menuBtn = document.querySelector('.menu-button');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if(!menuOpen) {
        menuBtn.classList.add('open');
        menuOpen = true;
    } else {
        menuBtn.classList.remove('open');
        menuOpen = false;
    }
})