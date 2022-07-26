function changeColor() {
    let priceChange = document.getElementsByClassName("change");
    if (priceChange)
    {
        for (key in priceChange)
        {
            firstLetter = String(priceChange[key].innerText.substr(0,1))
            if (firstLetter == "-")
            {
                priceChange[key].classList.add("negative");
                priceChange[key].classList.remove("positive");
            }
            else
            {
                priceChange[key].classList.add("positive");
                priceChange[key].classList.remove("negative");
            }
        }
    }
};

$( "div.card" ).hover(
    function(){
        $(this).children().css("color", "white")
    },
    function(){
        $(this).children().css("color", "#707070")
    },
);

changeColor();