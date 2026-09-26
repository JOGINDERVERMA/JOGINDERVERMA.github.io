import re

with open('index.html', 'r') as f:
    content = f.read()

# Use regex to find and replace the pricing section
pattern = r'<section id="pricing" class="section pricing">.*?</section>'

new_pricing_html = """<section id="pricing" class="section pricing">
            <div class="container">
                <div class="section-header fade-in-up">
                    <h2>06. Services & Packages</h2>
                </div>
                
                <div class="package-grid">
                    
                    <div class="package-card fade-in-up">
                        <div class="package-header">
                            <h3>Brand Starter</h3>
                            <p>Perfect for new businesses needing a solid digital footprint.</p>
                            <div class="package-price">$350</div>
                        </div>
                        <ul class="package-features">
                            <li><i class="fas fa-check"></i> Logo Design</li>
                            <li><i class="fas fa-check"></i> Social Media Setup</li>
                            <li><i class="fas fa-check"></i> 4x Post Designs</li>
                            <li><i class="fas fa-check"></i> Google My Business (GMB)</li>
                        </ul>
                        <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Package</a>
                    </div>

                    <div class="package-card popular fade-in-up delay-1">
                        <div class="popular-badge">Most Popular</div>
                        <div class="package-header">
                            <h3>Web Presence</h3>
                            <p>Get your business online with a standard CMS website.</p>
                            <div class="package-price">$750</div>
                        </div>
                        <ul class="package-features">
                            <li><i class="fas fa-check"></i> Website UI/UX Design</li>
                            <li><i class="fas fa-check"></i> Basic Website (CMS)</li>
                            <li><i class="fas fa-check"></i> Basic SEO Setup</li>
                            <li><i class="fas fa-check"></i> Mobile Responsive</li>
                        </ul>
                        <a href="https://wa.me/919166226522" class="btn solid-btn package-btn" target="_blank">Book Package</a>
                    </div>

                    <div class="package-card fade-in-up delay-2">
                        <div class="package-header">
                            <h3>Complete Custom</h3>
                            <p>Tailored HTML/CSS development for unique experiences.</p>
                            <div class="package-price">From $1,200</div>
                        </div>
                        <ul class="package-features">
                            <li><i class="fas fa-check"></i> Custom UI/UX Design</li>
                            <li><i class="fas fa-check"></i> Custom HTML/CSS Website</li>
                            <li><i class="fas fa-check"></i> Advanced SEO Setup</li>
                            <li><i class="fas fa-check"></i> Performance Tuning</li>
                        </ul>
                        <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Package</a>
                    </div>

                </div>
                
                <div class="pricing-note fade-in-up">
                    <p style="text-align: center; margin-top: 3rem;">* Need individual services? Logo Design ($150) | Post Design ($25) | GMB ($75). Contact me for custom quotes.</p>
                </div>
            </div>
        </section>"""

content = re.sub(pattern, new_pricing_html, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

# Add CSS for package cards
css_addition = """
/* Package Cards */
.package-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 3rem;
    align-items: center;
}

.package-card {
    background: var(--bg-color);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 3rem 2rem;
    position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.package-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.06);
}

.package-card.popular {
    border: 2px solid var(--text-primary);
    transform: scale(1.05);
    box-shadow: 0 20px 50px rgba(0,0,0,0.08);
}

.package-card.popular:hover {
    transform: scale(1.05) translateY(-10px);
}

.popular-badge {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--text-primary);
    color: var(--bg-color);
    padding: 0.5rem 1.5rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.package-header {
    text-align: center;
    margin-bottom: 2.5rem;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 2rem;
}

.package-header h3 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
}

.package-header p {
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    height: 45px;
}

.package-price {
    font-size: 2.5rem;
    font-weight: 700;
    font-family: monospace;
}

.package-features {
    list-style: none;
    flex: 1;
    margin-bottom: 2.5rem;
}

.package-features li {
    font-size: 1rem;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    color: var(--text-secondary);
}

.package-features i {
    color: var(--text-primary);
    margin-right: 12px;
    font-size: 0.9rem;
}

.package-btn {
    width: 100%;
    text-align: center;
}

@media (max-width: 992px) {
    .package-card.popular {
        transform: scale(1);
    }
    .package-card.popular:hover {
        transform: translateY(-10px);
    }
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)
