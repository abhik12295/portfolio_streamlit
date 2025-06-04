document.addEventListener('DOMContentLoaded', () => {
    // Update spotlight in hero section
    document.addEventListener('mousemove', (e) => {
        const hero = document.querySelector('.hero-section');
        if (hero) {
            const rect = hero.getBoundingClientRect();
            hero.style.setProperty('--mx', `${e.clientX - rect.left}px`);
            hero.style.setProperty('--my', `${e.clientY - rect.top}px`);
        }
    });
});