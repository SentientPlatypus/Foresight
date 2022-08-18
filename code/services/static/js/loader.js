$(window).on("load", function(){
    $("#loader-wrapper").fadeOut("slow");
})

function toggleLoader()
{
    $("#loader-wrapper").fadeIn("slow");
}