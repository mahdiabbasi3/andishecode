let slideIndex = 0;

function moveSlide(step) {
    const slides = document.querySelectorAll('.slide');
    slideIndex = (slideIndex + step + slides.length) % slides.length;
    document.querySelector('.slider').style.transform = `translateX(-${slideIndex * 100}%)`;
}

setInterval(() => moveSlide(1), 5000); // تغییر خودکار اسلایدها
