import json

posts = [
    {"title": "Why Joginder Verma Believes UI/UX is the Future of Web Design", "category": "Design", "excerpt": "An in-depth look at why UI/UX goes beyond pixels. Joginder Verma explains the psychology behind user-centric design.", "image": "https://picsum.photos/seed/joginder1/600/400"},
    {"title": "Mastering SEO in 2026: Tips from Joginder Verma", "category": "SEO", "excerpt": "Want to rank higher on Google? Joginder Verma shares his top strategies for dominating local and global search results.", "image": "https://picsum.photos/seed/joginder2/600/400"},
    {"title": "HTML & CSS Best Practices by Joginder Verma", "category": "Development", "excerpt": "Writing clean, semantic HTML and modular CSS is crucial. Learn Joginder Verma's approach to scalable frontend architecture.", "image": "https://picsum.photos/seed/joginder3/600/400"},
    {"title": "JavaScript ES6+ Essentials Every Developer Should Know", "category": "JavaScript", "excerpt": "Joginder Verma breaks down the most important JavaScript ES6+ features that will make your code cleaner and faster.", "image": "https://picsum.photos/seed/joginder4/600/400"},
    {"title": "How Joginder Verma Uses jQuery in Modern Projects", "category": "jQuery", "excerpt": "Is jQuery dead? Joginder Verma discusses when it still makes sense to use jQuery for rapid DOM manipulation in 2026.", "image": "https://picsum.photos/seed/joginder5/600/400"},
    {"title": "Building Responsive Sites with Bootstrap", "category": "Bootstrap", "excerpt": "A guide by Joginder Verma on leveraging Bootstrap's grid system to build 10x responsive websites quickly.", "image": "https://picsum.photos/seed/joginder6/600/400"},
    {"title": "Client Communication: The Joginder Verma Method", "category": "Client Success", "excerpt": "Delivering a great website is only half the job. Joginder Verma shares how to handle client feedback and ensure project success.", "image": "https://picsum.photos/seed/joginder7/600/400"},
    {"title": "The Power of Google My Business (GMB)", "category": "SEO", "excerpt": "Joginder Verma explains why setting up GMB is the most critical step for any local business looking for organic leads.", "image": "https://picsum.photos/seed/joginder8/600/400"},
    {"title": "Why Joginder Verma Advocates for AI in Development", "category": "Development", "excerpt": "AI isn't replacing developers; it's empowering them. Joginder Verma's thoughts on integrating AI into your coding workflow.", "image": "https://picsum.photos/seed/joginder9/600/400"},
    {"title": "Designing for Accessibility: A Priority for Joginder Verma", "category": "Design", "excerpt": "Web accessibility is not optional. Learn how Joginder Verma ensures his UI/UX designs are inclusive for all users.", "image": "https://picsum.photos/seed/joginder10/600/400"},
    {"title": "React.js vs Vanilla JS: When to use which?", "category": "JavaScript", "excerpt": "Joginder Verma compares React.js and Vanilla JavaScript, helping you choose the right stack for your next project.", "image": "https://picsum.photos/seed/joginder11/600/400"},
    {"title": "Joginder Verma's Guide to Freelance Pricing", "category": "Business", "excerpt": "Struggling to price your services? Joginder Verma shares his package-based pricing strategy for web development and SEO.", "image": "https://picsum.photos/seed/joginder12/600/400"},
    {"title": "Optimizing Website Speed and Core Web Vitals", "category": "SEO", "excerpt": "Speed is a ranking factor. Joginder Verma reveals how to optimize images, minify CSS, and improve your Google PageSpeed score.", "image": "https://picsum.photos/seed/joginder13/600/400"},
    {"title": "The Art of the Landing Page", "category": "Design", "excerpt": "How to design landing pages that convert. Joginder Verma breaks down the anatomy of a high-converting hero section.", "image": "https://picsum.photos/seed/joginder14/600/400"},
    {"title": "Managing WordPress Security: Tips by Joginder Verma", "category": "Development", "excerpt": "Keep your WordPress sites safe from hackers. Joginder Verma's checklist for bulletproof CMS security.", "image": "https://picsum.photos/seed/joginder15/600/400"},
    {"title": "Why Consistency Beats Perfection", "category": "Mindset", "excerpt": "Drawing from his popular LinkedIn posts, Joginder Verma explains why launching and iterating is better than waiting for perfection.", "image": "https://picsum.photos/seed/joginder16/600/400"},
    {"title": "Advanced CSS Animations and Transitions", "category": "CSS", "excerpt": "Bring your website to life. Joginder Verma shares code snippets for smooth, professional CSS animations.", "image": "https://picsum.photos/seed/joginder17/600/400"},
    {"title": "How Joginder Verma Approaches Mobile-First Design", "category": "Design", "excerpt": "With mobile traffic dominating the web, Joginder Verma discusses why you must design for the smallest screens first.", "image": "https://picsum.photos/seed/joginder18/600/400"},
    {"title": "Integrating Social Media into Your Website", "category": "Marketing", "excerpt": "Joginder Verma on how to seamlessly blend your Instagram and Twitter feeds into your HTML/CSS website architecture.", "image": "https://picsum.photos/seed/joginder19/600/400"},
    {"title": "The Future of Web Development According to Joginder Verma", "category": "Development", "excerpt": "From Web3 to Agentic AI, Joginder Verma predicts the next big trends that will shape the internet in the coming decade.", "image": "https://picsum.photos/seed/joginder20/600/400"},
    {"title": "How to Rank for Your Name on Google", "category": "SEO", "excerpt": "Joginder Verma shares his personal strategy for dominating branded search terms and building a powerful personal brand online.", "image": "https://picsum.photos/seed/joginder21/600/400"}
]

js_code = f"""
const blogPosts = {json.dumps(posts)};

const blogGrid = document.getElementById('blog-grid');

if(blogGrid) {{
    blogPosts.forEach((post, index) => {{
        const delay = (index % 3) * 0.1;
        const article = document.createElement('article');
        article.className = 'blog-card fade-in-up';
        article.style.transitionDelay = `${{delay}}s`;
        
        article.innerHTML = `
            <div class="blog-img-wrapper">
                <img src="${{post.image}}" alt="${{post.title}} by Joginder Verma" loading="lazy">
                <span class="blog-category">${{post.category}}</span>
            </div>
            <div class="blog-content">
                <h2 class="blog-title">${{post.title}}</h2>
                <p class="blog-excerpt">${{post.excerpt}}</p>
                <a href="#" class="blog-read-more">Read Article →</a>
            </div>
        `;
        blogGrid.appendChild(article);
    }});
}}
"""

with open('js/blog.js', 'w') as f:
    f.write(js_code)

blog_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Joginder Verma Blog | Web Design, SEO & Development Insights</title>
    <meta name="description" content="Read the latest insights from Joginder Verma on UI/UX design, SEO, HTML, CSS, JavaScript, and web development. Joginder Verma is a top specialist based in Jaipur.">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="cursor"></div>
    <div class="cursor-follower"></div>

    <header class="header">
        <div class="logo">
            <a href="index.html" style="display:flex; align-items:center; text-decoration:none; color:inherit;">
                <img src="img/main.jpg" alt="Joginder Verma" class="nav-profile-img">
                <span>Joginder Verma.</span>
            </a>
        </div>
        <nav class="nav-links">
            <a href="index.html#about" class="nav-link">About</a>
            <a href="index.html#philosophy" class="nav-link">Philosophy</a>
            <a href="index.html#pricing" class="nav-link">Pricing</a>
            <a href="blog.html" class="nav-link" style="font-weight:700;">Blog</a>
            <a href="index.html#contact" class="nav-link">Contact</a>
        </nav>
        <div class="menu-btn">
            <span class="menu-text" style="font-weight:500; font-size:0.9rem; text-transform:uppercase;">Menu</span>
            <div class="hamburger">
                <div class="bar"></div>
                <div class="bar"></div>
            </div>
        </div>
    </header>

    <!-- Mobile Overlay Menu -->
    <div class="mobile-menu-overlay">
        <div class="mobile-nav-links">
            <a href="index.html#about" class="mobile-link">01. About</a>
            <a href="index.html#experience" class="mobile-link">02. Experience</a>
            <a href="index.html#pricing" class="mobile-link">03. Pricing</a>
            <a href="blog.html" class="mobile-link">04. Blog</a>
            <a href="index.html#contact" class="mobile-link">05. Contact</a>
        </div>
        <div class="mobile-socials">
            <a href="https://twitter.com/PRINCEVERMA143_" target="_blank" style="color:var(--text-primary); text-decoration:none; font-weight:500;">Twitter</a>
            <a href="https://github.com/JOGINDERVERMA" target="_blank" style="color:var(--text-primary); text-decoration:none; font-weight:500;">GitHub</a>
            <a href="https://www.linkedin.com/in/joginderdevwork/" target="_blank" style="color:var(--text-primary); text-decoration:none; font-weight:500;">LinkedIn</a>
        </div>
    </div>

    <main style="padding-top: 150px; min-height: 100vh;">
        <div class="container">
            <div class="fade-in-up">
                <h1 class="headline" style="font-size: clamp(3rem, 6vw, 5rem); margin-bottom: 1rem;">Insights by Joginder Verma.</h1>
                <p style="font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 4rem; max-width: 600px;">Expert thoughts on UI/UX design, modern web development, and dominating search engines. Discover the strategies that drive success.</p>
            </div>
            
            <div class="blog-grid" id="blog-grid">
                <!-- Posts injected via JS -->
            </div>
        </div>
    </main>

    <footer class="footer" style="margin-top: 100px;">
        <div class="container footer-container">
            <p>&copy; <span id="year"></span> Joginder Verma. All rights reserved.</p>
            <div class="social-links">
                <a href="https://twitter.com/PRINCEVERMA143_" target="_blank" class="social-icon">Twitter</a>
                <a href="https://github.com/JOGINDERVERMA" target="_blank" class="social-icon">GitHub</a>
                <a href="https://www.linkedin.com/in/joginderdevwork/" target="_blank" class="social-icon">LinkedIn</a>
                <a href="https://wa.me/919166226522" target="_blank" class="social-icon">WhatsApp</a>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/919166226522" target="_blank" class="whatsapp-sticky">
        <i class="fab fa-whatsapp"></i>
    </a>

    <script src="js/script.js"></script>
    <script src="js/blog.js"></script>
</body>
</html>
"""

with open('blog.html', 'w') as f:
    f.write(blog_html)

# Add CSS for blog
css_addition = """
/* Blog Grid */
.blog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 3rem;
    padding-bottom: 100px;
}

.blog-card {
    background: var(--bg-color);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}

.blog-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.06);
}

.blog-img-wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 60%;
    overflow: hidden;
}

.blog-img-wrapper img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.blog-card:hover .blog-img-wrapper img {
    transform: scale(1.05);
}

.blog-category {
    position: absolute;
    top: 15px;
    left: 15px;
    background: var(--text-primary);
    color: var(--bg-color);
    padding: 0.3rem 1rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.blog-content {
    padding: 2rem;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.blog-title {
    font-size: 1.4rem;
    margin-bottom: 1rem;
    line-height: 1.3;
}

.blog-excerpt {
    font-size: 0.95rem;
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    flex: 1;
}

.blog-read-more {
    font-weight: 600;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: inline-flex;
    align-items: center;
    transition: transform 0.3s ease;
}

.blog-read-more:hover {
    transform: translateX(5px);
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)
