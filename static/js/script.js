const pricingCards = document.querySelectorAll('.pricing-card');

pricingCards.forEach((card, index) => {
    card.style.opacity = 0;
    card.style.transform = 'translateY(50px)';
    setTimeout(() => {
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        card.style.opacity = 1;
        card.style.transform = 'translateY(0)';
    }, index * 300);
});

const banner = document.querySelector('.banner');
const icons = [

    'https://img.icons8.com/?size=100&id=17949&format=png&color=000000',

    'https://cdn-icons-png.flaticon.com/512/5968/5968292.png', // JS

    'https://img.icons8.com/?size=100&id=eJHHh6ZbljAD&format=png&color=000000',
    'https://img.icons8.com/?size=100&id=PDn37mC1QXV6&format=png&color=000000',// Google
    'https://img.icons8.com/?size=100&id=PGHsq5peV5Fl&format=png&color=000000', // 404
    'https://img.icons8.com/?size=100&id=17949&format=png&color=000000',
    'https://img.icons8.com/?size=100&id=k4jADXhS5U1t&format=png&color=000000', //telegram
    'https://img.icons8.com/?size=100&id=zrTptiWiMTtu&format=png&color=000000', //web

    'https://img.icons8.com/?size=100&id=aMLZmDlq6SvC&format=png&color=000000', // WordPress
    'https://img.icons8.com/?size=100&id=aMLZmDlq6SvC&format=png&color=000000', // WordPres
];

for (let i = 0; i < 20; i++) {
    const img = document.createElement('img');
    img.src = icons[Math.floor(Math.random() * icons.length)];
    img.className = 'icon';
    img.style.left = Math.random() * 95 + '%';
    img.style.animationDuration = 3 + Math.random() * 3 + 's';
    img.style.width = 30 + Math.random() * 20 + 'px';
    img.style.animationDelay = Math.random() * 5 + 's';
    banner.appendChild(img);
}
const cards = document.querySelectorAll('.card');

cards.forEach(card => {
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * 10;
        const rotateY = ((x - centerX) / centerX) * 10;

        card.style.transform = `rotateY(${rotateY}deg) rotateX(${-rotateX}deg) translateY(-10px)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateY(0deg) rotateX(0deg) translateY(0)';
    });
});


// گرفتن دکمه‌های فیلتر و نمونه‌کارها
const filterBtns = document.querySelectorAll('.filter-btn');
const portfolioItems = document.querySelectorAll('.portfolio-item');

// افزودن رویداد کلیک برای فیلتر کردن
filterBtns.forEach(button => {
    button.addEventListener('click', (e) => {
        const filter = e.target.getAttribute('data-filter');
        filterPortfolio(filter);
    });
});

// عملکرد فیلتر کردن
function filterPortfolio(filter) {
    portfolioItems.forEach(item => {
        if (filter === 'all') {
            item.classList.remove('hidden');
        } else if (!item.classList.contains(filter)) {
            item.classList.add('hidden');
        } else {
            item.classList.remove('hidden');
        }
    });
}






const articles = document.querySelectorAll('.article-card');

articles.forEach((card, index) => {
    card.style.opacity = 0;
    card.style.transform = 'translateY(50px)';
    setTimeout(() => {
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        card.style.opacity = 1;
        card.style.transform = 'translateY(0)';
    }, index * 200);
});



