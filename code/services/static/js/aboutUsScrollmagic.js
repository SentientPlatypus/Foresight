const controller = new ScrollMagic.Controller();

var slides = document.querySelectorAll("section.panel");

// create scene for every slide
for (var i=0; i<slides.length; i++) {
    new ScrollMagic.Scene({
            triggerElement: slides[i],
            offset:(window.innerHeight)*0.3
        })
        .setPin(slides[i], {pushFollowers: false})
        .addTo(controller);
}