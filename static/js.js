var menuVisible = false;
$(document).ready(function(){
    $(".nav-link").mouseover(function(){
        $(this).css("background", "#326589");
    })
    $(".nav-link").mouseout(function(){
        $(this).css("background", "#2D4759");
    })
    $("#nav-home").attr("href", "http://127.0.0.1:5000/");
    $("#nav-about").attr("href", "http://127.0.0.1:5000/about");
    $("#nav-projects").attr("href", "http://127.0.0.1:5000/projects");
    $("#menu-button").click(function(){
        if (menuVisible){
            $("#side-bar-wrapper").css("display", "none");
            menuVisible = false;
        }
        else{
            $("#side-bar-wrapper").css("display", "block");
            $('html, body').animate({scrollTop : 0},400);
            menuVisible = true;
        }
    })
})
