const blogGrid = document.getElementById('blog-grid');

if(blogGrid && typeof blogPosts !== 'undefined') {
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
                <a href="/post?id=${index}" class="blog-read-more">Read Article →</a>
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
        document.querySelectorAll('.blog-card.fade-in-up').forEach(card => card.classList.add('visible'));
    }
}, 100);
