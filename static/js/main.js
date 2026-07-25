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
                'JavaScript vs TypeScript',
                'C++ vs Rust',
                'Go vs Ruby',
                'Who will win?'
            ],
            typeSpeed: 50,
            backSpeed: 30,
            backDelay: 2000,
            loop: true,
            cursorChar: '▌',
            autoInsertCss: true,
        });
    }

    // Basic GSAP Animations
    if (document.querySelector('.navbar-brand')) {
        gsap.from('.navbar-brand', { opacity: 0, x: -50, duration: 1, ease: 'power3.out' });
    }
    if (document.querySelector('.nav-link')) {
        gsap.from('.nav-link', { opacity: 0, y: -20, duration: 0.8, stagger: 0.1, ease: 'power2.out', delay: 0.2 });
    }
    if (document.querySelector('.hero-content')) {
        gsap.from('.hero-content', { opacity: 0, y: 30, duration: 1.5, ease: 'power3.out', delay: 0.5 });
    }

    // ═══ Language Selection Logic ═══
    const languageCards = document.querySelectorAll('.lang-card');
    const proceedBtnContainer = document.getElementById('proceed-btn-container');
    const counterPill = document.getElementById('counter-pill');
    const counterText = document.getElementById('counter-text');
    const dot1 = document.getElementById('dot1');
    const dot2 = document.getElementById('dot2');
    const slot1 = document.getElementById('slot1');
    const slot2 = document.getElementById('slot2');
    let selectedLanguages = [];
    let selectedIcons = [];

    if (languageCards.length > 0) {
        languageCards.forEach(card => {
            card.addEventListener('click', () => {
                const langId = card.getAttribute('data-lang-id');
                const langIcon = card.getAttribute('data-lang-icon');

                if (selectedLanguages.includes(langId)) {
                    // Deselect
                    const idx = selectedLanguages.indexOf(langId);
                    selectedLanguages.splice(idx, 1);
                    selectedIcons.splice(idx, 1);
                    card.classList.remove('selected');
                } else {
                    if (selectedLanguages.length < 2) {
                        selectedLanguages.push(langId);
                        selectedIcons.push(langIcon);
                        card.classList.add('selected');
                        // Pop animation
                        gsap.from(card, { scale: 0.9, duration: 0.3, ease: "back.out(2)" });
                    } else {
                        gsap.to(card, { x: 8, duration: 0.08, yoyo: true, repeat: 5 });
                        return;
                    }
                }

                // Update counter dots
                if (dot1) {
                    if (selectedLanguages.length >= 1) {
                        dot1.classList.add('filled');
                        dot1.innerHTML = '✓';
                    } else {
                        dot1.classList.remove('filled');
                        dot1.innerHTML = '1';
                    }
                }
                if (dot2) {
                    if (selectedLanguages.length >= 2) {
                        dot2.classList.add('filled');
                        dot2.innerHTML = '✓';
                    } else {
                        dot2.classList.remove('filled');
                        dot2.innerHTML = '2';
                    }
                }

                // Update counter text
                if (counterText) {
                    if (selectedLanguages.length === 0) counterText.innerText = 'Pick your fighters';
                    else if (selectedLanguages.length === 1) counterText.innerText = 'Pick one more';
                    else counterText.innerText = 'Ready to fight!';
                }
                if (counterPill) {
                    if (selectedLanguages.length === 2) counterPill.classList.add('ready');
                    else counterPill.classList.remove('ready');
                }

                // Update VS preview slots
                if (slot1) {
                    if (selectedIcons.length >= 1) {
                        slot1.innerHTML = `<i class="${selectedIcons[0]} colored"></i>`;
                        slot1.classList.add('active');
                        gsap.from(slot1, { scale: 0.5, duration: 0.3, ease: "back.out(2)" });
                    } else {
                        slot1.innerHTML = '?';
                        slot1.classList.remove('active');
                    }
                }
                if (slot2) {
                    if (selectedIcons.length >= 2) {
                        slot2.innerHTML = `<i class="${selectedIcons[1]} colored"></i>`;
                        slot2.classList.add('active');
                        gsap.from(slot2, { scale: 0.5, duration: 0.3, ease: "back.out(2)" });
                    } else {
                        slot2.innerHTML = '?';
                        slot2.classList.remove('active');
                    }
                }

                // Show/Hide proceed button
                if (proceedBtnContainer) {
                    if (selectedLanguages.length === 2) {
                        proceedBtnContainer.classList.add('show');
                        const btn = proceedBtnContainer.querySelector('a');
                        if (btn) {
                            btn.href = `/arena?lang1=${selectedLanguages[0]}&lang2=${selectedLanguages[1]}`;
                        }
                    } else {
                        proceedBtnContainer.classList.remove('show');
                    }
                }
            });
        });
    }
});
