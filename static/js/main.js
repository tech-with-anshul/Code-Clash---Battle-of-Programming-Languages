document.addEventListener('DOMContentLoaded', () => {
    // Initialize AOS
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        mirror: false
    });

    // Initialize Particles.js
    if (document.getElementById('particles-js')) {
        particlesJS.load('particles-js', '/static/js/particles-config.json', function() {
            console.log('callback - particles.js config loaded');
        });
    }

    // Initialize Typed.js if element exists
    const typedElement = document.getElementById('typed-text');
    if (typedElement) {
        new Typed('#typed-text', {
            strings: [
                'Python vs Java', 
                'React vs Angular', 
                'C++ vs Rust', 
                'The Ultimate Clash'
            ],
            typeSpeed: 50,
            backSpeed: 30,
            backDelay: 2000,
            loop: true,
            cursorChar: '|',
            autoInsertCss: true,
        });
    }

    // Basic GSAP Animations
    gsap.from('.navbar-brand', { opacity: 0, x: -50, duration: 1, ease: 'power3.out' });
    gsap.from('.nav-link', { opacity: 0, y: -20, duration: 0.8, stagger: 0.1, ease: 'power2.out', delay: 0.2 });
    if(document.querySelector('.hero-content')) {
        gsap.from('.hero-content', { opacity: 0, y: 30, duration: 1.5, ease: 'power3.out', delay: 0.5 });
    }

    // Language Selection Logic
    const languageCards = document.querySelectorAll('.language-card');
    const proceedBtnContainer = document.getElementById('proceed-btn-container');
    const selectionCounter = document.getElementById('selection-counter');
    let selectedLanguages = [];

    if (languageCards.length > 0) {
        languageCards.forEach(card => {
            card.addEventListener('click', () => {
                const langId = card.getAttribute('data-lang-id');
                
                // If already selected, deselect it
                if (selectedLanguages.includes(langId)) {
                    selectedLanguages = selectedLanguages.filter(id => id !== langId);
                    card.classList.remove('selected');
                } else {
                    // Only allow selecting if less than 2 are currently selected
                    if (selectedLanguages.length < 2) {
                        selectedLanguages.push(langId);
                        card.classList.add('selected');
                    } else {
                        // Highlight effect to indicate they can't select more
                        gsap.to(card, { x: 10, duration: 0.1, yoyo: true, repeat: 3 });
                    }
                }
                
                // Update counter text
                if (selectionCounter) {
                    selectionCounter.innerText = `Selected: ${selectedLanguages.length} / 2`;
                    if (selectedLanguages.length === 2) {
                        selectionCounter.classList.add('text-success');
                        selectionCounter.classList.remove('text-warning');
                    } else {
                        selectionCounter.classList.remove('text-success');
                        selectionCounter.classList.add('text-warning');
                    }
                }

                // Show/Hide proceed button
                if (selectedLanguages.length === 2) {
                    proceedBtnContainer.classList.add('show');
                    const btn = proceedBtnContainer.querySelector('a');
                    if (btn) {
                        btn.href = `/arena?lang1=${selectedLanguages[0]}&lang2=${selectedLanguages[1]}`;
                    }
                } else {
                    proceedBtnContainer.classList.remove('show');
                }
            });
        });
    }
});
