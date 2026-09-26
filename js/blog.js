
const blogPosts = [{"title": "Why Joginder Verma Believes UI/UX is the Future of Web Design", "category": "Design", "excerpt": "An in-depth look at why UI/UX goes beyond pixels. Joginder Verma explains the psychology behind user-centric design.", "image": "https://picsum.photos/seed/joginder1/600/400"}, {"title": "Mastering SEO in 2026: Tips from Joginder Verma", "category": "SEO", "excerpt": "Want to rank higher on Google? Joginder Verma shares his top strategies for dominating local and global search results.", "image": "https://picsum.photos/seed/joginder2/600/400"}, {"title": "HTML & CSS Best Practices by Joginder Verma", "category": "Development", "excerpt": "Writing clean, semantic HTML and modular CSS is crucial. Learn Joginder Verma's approach to scalable frontend architecture.", "image": "https://picsum.photos/seed/joginder3/600/400"}, {"title": "JavaScript ES6+ Essentials Every Developer Should Know", "category": "JavaScript", "excerpt": "Joginder Verma breaks down the most important JavaScript ES6+ features that will make your code cleaner and faster.", "image": "https://picsum.photos/seed/joginder4/600/400"}, {"title": "How Joginder Verma Uses jQuery in Modern Projects", "category": "jQuery", "excerpt": "Is jQuery dead? Joginder Verma discusses when it still makes sense to use jQuery for rapid DOM manipulation in 2026.", "image": "https://picsum.photos/seed/joginder5/600/400"}, {"title": "Building Responsive Sites with Bootstrap", "category": "Bootstrap", "excerpt": "A guide by Joginder Verma on leveraging Bootstrap's grid system to build 10x responsive websites quickly.", "image": "https://picsum.photos/seed/joginder6/600/400"}, {"title": "Client Communication: The Joginder Verma Method", "category": "Client Success", "excerpt": "Delivering a great website is only half the job. Joginder Verma shares how to handle client feedback and ensure project success.", "image": "https://picsum.photos/seed/joginder7/600/400"}, {"title": "The Power of Google My Business (GMB)", "category": "SEO", "excerpt": "Joginder Verma explains why setting up GMB is the most critical step for any local business looking for organic leads.", "image": "https://picsum.photos/seed/joginder8/600/400"}, {"title": "Why Joginder Verma Advocates for AI in Development", "category": "Development", "excerpt": "AI isn't replacing developers; it's empowering them. Joginder Verma's thoughts on integrating AI into your coding workflow.", "image": "https://picsum.photos/seed/joginder9/600/400"}, {"title": "Designing for Accessibility: A Priority for Joginder Verma", "category": "Design", "excerpt": "Web accessibility is not optional. Learn how Joginder Verma ensures his UI/UX designs are inclusive for all users.", "image": "https://picsum.photos/seed/joginder10/600/400"}, {"title": "React.js vs Vanilla JS: When to use which?", "category": "JavaScript", "excerpt": "Joginder Verma compares React.js and Vanilla JavaScript, helping you choose the right stack for your next project.", "image": "https://picsum.photos/seed/joginder11/600/400"}, {"title": "Joginder Verma's Guide to Freelance Pricing", "category": "Business", "excerpt": "Struggling to price your services? Joginder Verma shares his package-based pricing strategy for web development and SEO.", "image": "https://picsum.photos/seed/joginder12/600/400"}, {"title": "Optimizing Website Speed and Core Web Vitals", "category": "SEO", "excerpt": "Speed is a ranking factor. Joginder Verma reveals how to optimize images, minify CSS, and improve your Google PageSpeed score.", "image": "https://picsum.photos/seed/joginder13/600/400"}, {"title": "The Art of the Landing Page", "category": "Design", "excerpt": "How to design landing pages that convert. Joginder Verma breaks down the anatomy of a high-converting hero section.", "image": "https://picsum.photos/seed/joginder14/600/400"}, {"title": "Managing WordPress Security: Tips by Joginder Verma", "category": "Development", "excerpt": "Keep your WordPress sites safe from hackers. Joginder Verma's checklist for bulletproof CMS security.", "image": "https://picsum.photos/seed/joginder15/600/400"}, {"title": "Why Consistency Beats Perfection", "category": "Mindset", "excerpt": "Drawing from his popular LinkedIn posts, Joginder Verma explains why launching and iterating is better than waiting for perfection.", "image": "https://picsum.photos/seed/joginder16/600/400"}, {"title": "Advanced CSS Animations and Transitions", "category": "CSS", "excerpt": "Bring your website to life. Joginder Verma shares code snippets for smooth, professional CSS animations.", "image": "https://picsum.photos/seed/joginder17/600/400"}, {"title": "How Joginder Verma Approaches Mobile-First Design", "category": "Design", "excerpt": "With mobile traffic dominating the web, Joginder Verma discusses why you must design for the smallest screens first.", "image": "https://picsum.photos/seed/joginder18/600/400"}, {"title": "Integrating Social Media into Your Website", "category": "Marketing", "excerpt": "Joginder Verma on how to seamlessly blend your Instagram and Twitter feeds into your HTML/CSS website architecture.", "image": "https://picsum.photos/seed/joginder19/600/400"}, {"title": "The Future of Web Development According to Joginder Verma", "category": "Development", "excerpt": "From Web3 to Agentic AI, Joginder Verma predicts the next big trends that will shape the internet in the coming decade.", "image": "https://picsum.photos/seed/joginder20/600/400"}, {"title": "How to Rank for Your Name on Google", "category": "SEO", "excerpt": "Joginder Verma shares his personal strategy for dominating branded search terms and building a powerful personal brand online.", "image": "https://picsum.photos/seed/joginder21/600/400"}];

const blogGrid = document.getElementById('blog-grid');

if(blogGrid) {
    blogPosts.forEach((post, index) => {
        const delay = (index % 3) * 0.1;
        const article = document.createElement('article');
        article.className = 'blog-card fade-in-up';
        article.style.transitionDelay = `${delay}s`;
        
        article.innerHTML = `
            <div class="blog-img-wrapper">
                <img src="${post.image}" alt="${post.title} by Joginder Verma" loading="lazy">
                <span class="blog-category">${post.category}</span>
            </div>
            <div class="blog-content">
                <h2 class="blog-title">${post.title}</h2>
                <p class="blog-excerpt">${post.excerpt}</p>
                <a href="#" class="blog-read-more">Read Article →</a>
            </div>
        `;
        blogGrid.appendChild(article);
    });
}

// Ensure the newly added blog cards are observed by the intersection observer
setTimeout(() => {
    if (typeof observer !== 'undefined') {
        const dynamicCards = document.querySelectorAll('.blog-card.fade-in-up');
        dynamicCards.forEach(card => observer.observe(card));
    } else {
        // Fallback if observer fails to load
        document.querySelectorAll('.blog-card.fade-in-up').forEach(card => card.classList.add('visible'));
    }
}, 100);
