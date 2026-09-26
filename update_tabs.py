import re

with open('index.html', 'r') as f:
    content = f.read()

pattern = r'<section id="pricing" class="section pricing">.*?</section>'

new_pricing_html = """<section id="pricing" class="section pricing">
            <div class="container">
                <div class="section-header fade-in-up" style="text-align: center; margin-bottom: 2rem;">
                    <h2>06. Services & Packages</h2>
                </div>
                
                <div class="pricing-tabs fade-in-up">
                    <button class="tab-btn active" data-tab="tab-seo">SEO & Marketing</button>
                    <button class="tab-btn" data-tab="tab-design">Design</button>
                    <button class="tab-btn" data-tab="tab-dev">Development</button>
                </div>
                
                <!-- SEO TAB -->
                <div class="tab-content active" id="tab-seo">
                    <div class="package-grid">
                        <div class="package-card">
                            <div class="package-header">
                                <h3>Basic Setup</h3>
                                <p>One-time setup for local visibility.</p>
                                <div class="package-price">$49 <span class="inr-price">/ ₹3,999</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">One-off</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Google My Business (GMB) Setup</li>
                                <li><i class="fas fa-check"></i> Basic Keyword Research</li>
                                <li><i class="fas fa-check"></i> On-Page SEO Review</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Now</a>
                        </div>

                        <div class="package-card popular">
                            <div class="popular-badge">Most Popular</div>
                            <div class="package-header">
                                <h3>Local SEO Growth</h3>
                                <p>Monthly retainer to dominate local search.</p>
                                <div class="package-price">$29 <span class="inr-price">/ ₹2,499</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">per month</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Monthly GMB Updates</li>
                                <li><i class="fas fa-check"></i> Local Directory Listings</li>
                                <li><i class="fas fa-check"></i> Review Management</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn solid-btn package-btn" target="_blank">Subscribe</a>
                        </div>

                        <div class="package-card">
                            <div class="package-header">
                                <h3>Full SEO Power</h3>
                                <p>Comprehensive SEO for serious organic traffic.</p>
                                <div class="package-price">$99 <span class="inr-price">/ ₹7,999</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">per month</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Advanced Technical SEO</li>
                                <li><i class="fas fa-check"></i> Monthly Content Strategy</li>
                                <li><i class="fas fa-check"></i> Backlink Building</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Subscribe</a>
                        </div>
                    </div>
                </div>

                <!-- DESIGN TAB -->
                <div class="tab-content" id="tab-design">
                    <div class="package-grid">
                        <div class="package-card">
                            <div class="package-header">
                                <h3>Logo & Branding</h3>
                                <p>Professional identity for your business.</p>
                                <div class="package-price">$49 <span class="inr-price">/ ₹3,999</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">One-off</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Custom Logo Design</li>
                                <li><i class="fas fa-check"></i> Brand Color Palette</li>
                                <li><i class="fas fa-check"></i> High-Res Files included</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Now</a>
                        </div>

                        <div class="package-card popular">
                            <div class="popular-badge">Most Popular</div>
                            <div class="package-header">
                                <h3>Social Media Pack</h3>
                                <p>Keep your social feeds fresh every month.</p>
                                <div class="package-price">$29 <span class="inr-price">/ ₹2,499</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">per month</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> 4x Custom Post Designs</li>
                                <li><i class="fas fa-check"></i> Story & Reel Templates</li>
                                <li><i class="fas fa-check"></i> Profile Optimization</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn solid-btn package-btn" target="_blank">Subscribe</a>
                        </div>

                        <div class="package-card">
                            <div class="package-header">
                                <h3>UI/UX Design</h3>
                                <p>High-end conceptual design for your app/web.</p>
                                <div class="package-price">$99 <span class="inr-price">/ ₹7,999</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">Per Project</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Wireframing & Prototyping</li>
                                <li><i class="fas fa-check"></i> User-Centered Layouts</li>
                                <li><i class="fas fa-check"></i> Figma Source Files</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Now</a>
                        </div>
                    </div>
                </div>

                <!-- DEV TAB -->
                <div class="tab-content" id="tab-dev">
                    <div class="package-grid">
                        <div class="package-card">
                            <div class="package-header">
                                <h3>Basic HTML Web</h3>
                                <p>A blazing fast, custom coded static website.</p>
                                <div class="package-price">$99 <span class="inr-price">/ ₹7,999</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">One-off</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Custom HTML/CSS/JS</li>
                                <li><i class="fas fa-check"></i> 3-5 Pages</li>
                                <li><i class="fas fa-check"></i> Mobile Responsive</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Now</a>
                        </div>

                        <div class="package-card popular">
                            <div class="popular-badge">Most Popular</div>
                            <div class="package-header">
                                <h3>CMS / WordPress</h3>
                                <p>Easily manageable website for businesses.</p>
                                <div class="package-price">$149 <span class="inr-price">/ ₹11,999</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">One-off</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Full WordPress Setup</li>
                                <li><i class="fas fa-check"></i> Premium Theme Integration</li>
                                <li><i class="fas fa-check"></i> Blog & Contact Form</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn solid-btn package-btn" target="_blank">Book Now</a>
                        </div>

                        <div class="package-card">
                            <div class="package-header">
                                <h3>Web Maintenance</h3>
                                <p>Ongoing technical support and bug fixing.</p>
                                <div class="package-price">$49 <span class="inr-price">/ ₹3,999</span></div>
                                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">per month</div>
                            </div>
                            <ul class="package-features">
                                <li><i class="fas fa-check"></i> Security & Backup Management</li>
                                <li><i class="fas fa-check"></i> Monthly Content Updates</li>
                                <li><i class="fas fa-check"></i> Bug Fixing & Troubleshooting</li>
                            </ul>
                            <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Subscribe</a>
                        </div>
                    </div>
                </div>

            </div>
        </section>"""

content = re.sub(pattern, new_pricing_html, content, flags=re.DOTALL)
with open('index.html', 'w') as f:
    f.write(content)

# CSS for tabs
css_addition = """
/* Tabs */
.pricing-tabs {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
    flex-wrap: wrap;
}

.tab-btn {
    padding: 0.8rem 2.5rem;
    border: 1px solid var(--border-color);
    background: transparent;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 500;
    transition: all 0.3s ease;
    font-family: inherit;
    color: var(--text-primary);
}

.tab-btn:hover {
    background: rgba(0,0,0,0.03);
}

.tab-btn.active {
    background: var(--text-primary);
    color: var(--bg-color);
    border-color: var(--text-primary);
}

.tab-content {
    display: none;
    animation: fadeIn 0.5s ease;
}

.tab-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)

# JS for tabs
js_addition = """
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
"""
with open('js/script.js', 'a') as f:
    f.write(js_addition)

