// Custom Cursor
const cursor = document.querySelector('.cursor');
const cursorFollower = document.querySelector('.cursor-follower');

document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
    
    // Follower has a slight delay
    setTimeout(() => {
        cursorFollower.style.left = e.clientX + 'px';
        cursorFollower.style.top = e.clientY + 'px';
    }, 80);
});

// Hover effect for interactive elements
const interactables = document.querySelectorAll('a, button, .menu-btn, .exp-row');

interactables.forEach(el => {
    el.addEventListener('mouseenter', () => {
        cursorFollower.style.width = '60px';
        cursorFollower.style.height = '60px';
        cursorFollower.style.backgroundColor = 'rgba(0, 0, 0, 0.05)';
        cursor.style.transform = 'translate(-50%, -50%) scale(0.5)';
    });
    
    el.addEventListener('mouseleave', () => {
        cursorFollower.style.width = '40px';
        cursorFollower.style.height = '40px';
        cursorFollower.style.backgroundColor = 'transparent';
        cursor.style.transform = 'translate(-50%, -50%) scale(1)';
    });
});

// Scroll animations with Intersection Observer
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

const animatedElements = document.querySelectorAll('.fade-in-up');
animatedElements.forEach(el => observer.observe(el));

// Current Year for Footer
document.getElementById('year').textContent = new Date().getFullYear();

// Header effect on scroll
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.style.padding = '1rem 4rem';
        header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.02)';
    } else {
        header.style.padding = '1.5rem 4rem';
        header.style.boxShadow = 'none';
    }
});

// Pricing Tabs
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        tabBtns.forEach(b => b.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));
        
        btn.classList.add('active');
        document.getElementById(btn.dataset.tab).classList.add('active');
    });
});

// Update interactables to include tab buttons
document.querySelectorAll('.tab-btn').forEach(el => {
    el.addEventListener('mouseenter', () => {
        cursorFollower.style.width = '60px';
        cursorFollower.style.height = '60px';
        cursorFollower.style.backgroundColor = 'rgba(0, 0, 0, 0.05)';
        cursor.style.transform = 'translate(-50%, -50%) scale(0.5)';
    });
    
    el.addEventListener('mouseleave', () => {
        cursorFollower.style.width = '40px';
        cursorFollower.style.height = '40px';
        cursorFollower.style.backgroundColor = 'transparent';
        cursor.style.transform = 'translate(-50%, -50%) scale(1)';
    });
});

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
