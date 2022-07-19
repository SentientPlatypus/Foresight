function changeColor() {
    let priceChange = document.getElementsByClassName("change");
    console.log(priceChange);
    for (key in priceChange)
    {
        firstLetter = String(priceChange[key].innerText.substr(0,1))
        console.log(firstLetter)
        if (firstLetter == "-")
        {
            console.log("Got here")
            if (!("negative" in priceChange[key].classList))
            {
                priceChange[key].classList.add("negative");
            }
            if ("positive" in priceChange[key].classList)
            {
                priceChange[key].classList.remove("positive");
            }
        }
        else
        {
            console.log("Got here2")
            if (!("positive" in priceChange[key].classList))
            {
                priceChange[key].classList.add("positive");
            }
            if ("negative" in priceChange[key].classList)
            {
                priceChange[key].classList.remove("negative");
            }
        }
    }
};

changeColor();