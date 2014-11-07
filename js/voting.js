var downPressed = false,
    upPressed = false;

$('.thumbup').click(function(){
    if (downPressed) {
        $('.thumbdown').removeClass('thumbdownpressed');
    }
    $(this).addClass('thumbuppressed');
    upPressed = true;
});

$('.thumbdown').click(function(){
    if (upPressed) {
        $('.thumbup').removeClass('thumbuppressed');
    }
    $(this).addClass('thumbdownpressed');
    downPressed = true;
  
});

function reset(){
    $('.thumbscaleDown').removeClass('thumbscaleDown');
    $('.thumbcheck').removeClass('thumbok');
    downPressed = false;
    upPressed = false;
   
}
