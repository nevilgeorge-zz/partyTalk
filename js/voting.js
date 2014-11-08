var otherEl, 
    downPressed = false,
    upPressed = false;

$('.thumbup').click(function(){
    otherEl = $(this).parent().children()[1];
    if ($(otherEl).hasClass("thumbdownpressed")) {
        $(otherEl).removeClass('thumbdownpressed');
    }
    $(this).addClass('thumbuppressed');
    upPressed = true;
});

$('.thumbdown').click(function(){
    otherEl = $(this).parent().children()[0];
    if ($(otherEl).hasClass("thumbuppressed")) {
        $(otherEl).removeClass("thumbuppressed");
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
