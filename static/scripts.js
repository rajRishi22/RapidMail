document.addEventListener('DOMContentLoaded', () => {
    const elementsToHighlight = document.querySelectorAll('.highlight-text');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('highlight');
            } else {
                entry.target.classList.remove('highlight');
            }
        });
    }, observerOptions);

    elementsToHighlight.forEach(element => {
        observer.observe(element);
    });
});