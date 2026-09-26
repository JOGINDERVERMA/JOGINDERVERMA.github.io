import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace menu-btn
old_menu_btn = '<div class="menu-btn">Menu</div>'
new_menu_btn = """        <div class="menu-btn">
            <span class="menu-text" style="font-weight:500; font-size:0.9rem; text-transform:uppercase;">Menu</span>
            <div class="hamburger">
                <div class="bar"></div>
                <div class="bar"></div>
            </div>
        </div>"""
content = content.replace(old_menu_btn, new_menu_btn)

# Add mobile menu overlay before <main>
overlay_html = """    <!-- Mobile Overlay Menu -->
    <div class="mobile-menu-overlay">
        <div class="mobile-nav-links">
            <a href="#about" class="mobile-link">01. About</a>
            <a href="#philosophy" class="mobile-link">02. Philosophy</a>
            <a href="#experience" class="mobile-link">03. Experience</a>
            <a href="#education" class="mobile-link">04. Education</a>
            <a href="#skills" class="mobile-link">05. Skills</a>
            <a href="#pricing" class="mobile-link">06. Pricing</a>
            <a href="#contact" class="mobile-link">07. Contact</a>
        </div>
        <div class="mobile-socials">
            <a href="https://twitter.com/PRINCEVERMA143_" target="_blank" style="color:var(--text-primary); text-decoration:none; font-weight:500;">Twitter</a>
            <a href="https://github.com/JOGINDERVERMA" target="_blank" style="color:var(--text-primary); text-decoration:none; font-weight:500;">GitHub</a>
            <a href="https://www.linkedin.com/in/joginderdevwork/" target="_blank" style="color:var(--text-primary); text-decoration:none; font-weight:500;">LinkedIn</a>
        </div>
    </div>

    <main>"""
content = content.replace('<main>', overlay_html)

with open('index.html', 'w') as f:
    f.write(content)


# CSS Updates
css_addition = """
/* Mobile Menu Overlay */
.mobile-menu-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: var(--bg-color);
    z-index: 99;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease;
}

.mobile-menu-overlay.active {
    opacity: 1;
    pointer-events: auto;
}

.mobile-nav-links {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    text-align: center;
}

.mobile-link {
    font-size: 2.5rem;
    font-weight: 600;
    text-transform: uppercase;
    transform: translateY(20px);
    opacity: 0;
    transition: all 0.4s ease;
    color: var(--text-primary);
}

.mobile-link:hover {
    opacity: 0.5;
}

.mobile-menu-overlay.active .mobile-link {
    transform: translateY(0);
    opacity: 1;
}

.mobile-menu-overlay.active .mobile-link:nth-child(1) { transition-delay: 0.1s; }
.mobile-menu-overlay.active .mobile-link:nth-child(2) { transition-delay: 0.15s; }
.mobile-menu-overlay.active .mobile-link:nth-child(3) { transition-delay: 0.2s; }
.mobile-menu-overlay.active .mobile-link:nth-child(4) { transition-delay: 0.25s; }
.mobile-menu-overlay.active .mobile-link:nth-child(5) { transition-delay: 0.3s; }
.mobile-menu-overlay.active .mobile-link:nth-child(6) { transition-delay: 0.35s; }
.mobile-menu-overlay.active .mobile-link:nth-child(7) { transition-delay: 0.4s; }

.mobile-socials {
    margin-top: 4rem;
    display: flex;
    gap: 2rem;
    opacity: 0;
    transition: opacity 0.4s ease 0.5s;
}

.mobile-menu-overlay.active .mobile-socials {
    opacity: 1;
}

/* Hamburger */
.menu-btn {
    display: none; 
    align-items: center;
    gap: 10px;
    z-index: 101; 
}

.hamburger {
    display: flex;
    flex-direction: column;
    gap: 6px;
    width: 25px;
}

.bar {
    width: 100%;
    height: 2px;
    background: var(--text-primary);
    transition: all 0.3s ease;
}

.menu-btn.open .bar:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
}

.menu-btn.open .bar:nth-child(2) {
    transform: translateY(-8px) rotate(-45deg);
}

.menu-btn.open .menu-text {
    opacity: 0; /* hide text on open */
}

/* 10x Responsive Tweaks */
@media (max-width: 992px) {
    .menu-btn { 
        display: flex; 
    }
    .header {
        padding: 1.5rem 2rem;
    }
    .container {
        padding: 0 2rem;
    }
    .hero {
        padding-top: 120px;
    }
    .headline {
        font-size: clamp(3rem, 10vw, 5rem);
    }
    .huge-text {
        font-size: clamp(3rem, 10vw, 5rem);
    }
    .section {
        padding: 80px 0;
    }
    .about-headline {
        font-size: clamp(1.8rem, 6vw, 2.5rem);
    }
    .edu-school {
        font-size: 1.8rem;
    }
    .package-card {
        padding: 2.5rem 1.5rem;
    }
}

@media (max-width: 576px) {
    .container {
        padding: 0 1.5rem;
    }
    .header {
        padding: 1.2rem 1.5rem;
    }
    .contact-buttons {
        flex-direction: column;
        width: 100%;
    }
    .btn {
        width: 100%;
        text-align: center;
    }
    .pricing-tabs {
        flex-direction: column;
    }
    .tab-btn {
        width: 100%;
    }
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)

# JS Updates
js_addition = """
// Mobile Navigation
const menuBtn = document.querySelector('.menu-btn');
const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');
const mobileLinks = document.querySelectorAll('.mobile-link');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('open');
    mobileMenuOverlay.classList.toggle('active');
    
    // Prevent scrolling when menu is open
    if (mobileMenuOverlay.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = '';
    }
});

// Close menu when clicking a link
mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        menuBtn.classList.remove('open');
        mobileMenuOverlay.classList.remove('active');
        document.body.style.overflow = '';
    });
});

// Add menu-btn to custom cursor interactables
menuBtn.addEventListener('mouseenter', () => {
    cursorFollower.style.width = '60px';
    cursorFollower.style.height = '60px';
    cursorFollower.style.backgroundColor = 'rgba(0, 0, 0, 0.05)';
    cursor.style.transform = 'translate(-50%, -50%) scale(0.5)';
});

menuBtn.addEventListener('mouseleave', () => {
    cursorFollower.style.width = '40px';
    cursorFollower.style.height = '40px';
    cursorFollower.style.backgroundColor = 'transparent';
    cursor.style.transform = 'translate(-50%, -50%) scale(1)';
});
"""
with open('js/script.js', 'a') as f:
    f.write(js_addition)

