with open('index.html', 'r') as f:
    content = f.read()

pricing_html = """
        <div class="divider"></div>

        <section id="pricing" class="section pricing">
            <div class="container">
                <div class="section-header fade-in-up">
                    <h2>06. Services & Pricing</h2>
                </div>
                <div class="pricing-grid">
                    
                    <div class="pricing-category fade-in-up">
                        <h3 class="category-title">Design</h3>
                        <div class="pricing-item">
                            <span class="service-name">Logo Design</span>
                            <span class="service-price">From $150</span>
                        </div>
                        <div class="pricing-item">
                            <span class="service-name">Social Media Post Design</span>
                            <span class="service-price">$25 / post</span>
                        </div>
                        <div class="pricing-item">
                            <span class="service-name">Website UI/UX Design</span>
                            <span class="service-price">From $350</span>
                        </div>
                    </div>

                    <div class="pricing-category fade-in-up delay-1">
                        <h3 class="category-title">Development</h3>
                        <div class="pricing-item">
                            <span class="service-name">Basic Website (CMS)</span>
                            <span class="service-price">From $250</span>
                        </div>
                        <div class="pricing-item">
                            <span class="service-name">Custom HTML/CSS Website</span>
                            <span class="service-price">From $400</span>
                        </div>
                    </div>

                    <div class="pricing-category fade-in-up delay-2">
                        <h3 class="category-title">Marketing & Setup</h3>
                        <div class="pricing-item">
                            <span class="service-name">Social Media Setup</span>
                            <span class="service-price">$100</span>
                        </div>
                        <div class="pricing-item">
                            <span class="service-name">Google My Business (GMB)</span>
                            <span class="service-price">$75</span>
                        </div>
                        <div class="pricing-item">
                            <span class="service-name">Basic SEO Setup</span>
                            <span class="service-price">From $150</span>
                        </div>
                    </div>

                </div>
                <div class="pricing-note fade-in-up">
                    <p>* Prices are standard starting estimates. Final quotes depend on project scope and complexity.</p>
                </div>
            </div>
        </section>
"""

# Insert before contact section
content = content.replace('<section id="contact"', pricing_html + '\n        <section id="contact"')

# Update navigation links
content = content.replace('<a href="#contact" class="nav-link">Contact</a>', '<a href="#pricing" class="nav-link">Pricing</a>\n            <a href="#contact" class="nav-link">Contact</a>')

with open('index.html', 'w') as f:
    f.write(content)

# CSS for Pricing
css_addition = """
/* Pricing */
.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 4rem;
    margin-bottom: 3rem;
}

.category-title {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--text-primary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.pricing-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.2rem 0;
    border-bottom: 1px solid var(--border-color);
}

.service-name {
    font-size: 1.1rem;
    font-weight: 500;
}

.service-price {
    font-size: 1.1rem;
    color: var(--text-secondary);
    font-family: monospace;
    font-weight: 600;
}

.pricing-note p {
    font-size: 0.9rem;
    font-style: italic;
    color: var(--text-secondary);
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)
