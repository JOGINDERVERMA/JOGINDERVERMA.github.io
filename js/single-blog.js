document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    const blogContainer = document.getElementById('blog-container');
    const pageTitle = document.getElementById('page-title');

    if (id !== null && blogPosts && blogPosts[id]) {
        const post = blogPosts[id];
        
        // Update page title for SEO
        pageTitle.textContent = `${post.title} | Joginder Verma`;

        blogContainer.innerHTML = `
            <div class="single-blog-header">
                <span class="single-blog-category">${post.category}</span>
                <h1 class="single-blog-title">${post.title}</h1>
            </div>
            
            <img src="${post.image}" alt="${post.title}" class="single-blog-image">
            
            <div class="single-blog-content">
                ${post.content}
            </div>
        `;
    } else {
        // Post not found
        blogContainer.innerHTML = `
            <div style="text-align:center; padding: 100px 0;">
                <h2>Blog post not found.</h2>
                <a href="/blog" class="btn outline-btn mt-4">Return to Blog</a>
            </div>
        `;
    }
});
