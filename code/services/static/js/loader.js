$(window).on("load", function(){
    toggleLoader()
})

function toggleLoader()
{
    $("#loader-wrapper").fadeToggle("slow");
}


function toggleSpinny()
{
    $("#loading-bar-spinner").fadeToggle("slow");
}


