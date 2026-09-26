import re

with open('index.html', 'r') as f:
    content = f.read()

# Regex to replace the entire pricing section
pattern = r'<section id="pricing" class="section pricing">.*?</section>'

new_pricing_html = """<section id="pricing" class="section pricing">
            <div class="container">
                <div class="section-header fade-in-up">
                    <h2>06. Services & Packages</h2>
                </div>
                
                <div class="package-grid">
                    
                    <div class="package-card fade-in-up">
                        <div class="package-header">
                            <h3>Growth Retainer</h3>
                            <p>Perfect for keeping your brand active and updated.</p>
                            <div class="package-price">$49 <span class="inr-price">/ ₹3,999</span></div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">per month</div>
                        </div>
                        <ul class="package-features">
                            <li><i class="fas fa-check"></i> 4x Social Media Post Designs</li>
                            <li><i class="fas fa-check"></i> Google My Business (GMB) Updates</li>
                            <li><i class="fas fa-check"></i> Basic SEO Monitoring</li>
                            <li><i class="fas fa-check"></i> Website Maintenance</li>
                        </ul>
                        <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Monthly</a>
                    </div>

                    <div class="package-card popular fade-in-up delay-1">
                        <div class="popular-badge">Most Popular</div>
                        <div class="package-header">
                            <h3>Complete Digital</h3>
                            <p>An all-in-one package to aggressively grow your online presence.</p>
                            <div class="package-price">$99 <span class="inr-price">/ ₹7,999</span></div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">per month</div>
                        </div>
                        <ul class="package-features">
                            <li><i class="fas fa-check"></i> 10x Social Media Post Designs</li>
                            <li><i class="fas fa-check"></i> Advanced SEO & GMB Optimization</li>
                            <li><i class="fas fa-check"></i> Priority Website Updates</li>
                            <li><i class="fas fa-check"></i> UI/UX Design Consultation</li>
                        </ul>
                        <a href="https://wa.me/919166226522" class="btn solid-btn package-btn" target="_blank">Book Monthly</a>
                    </div>

                    <div class="package-card fade-in-up delay-2">
                        <div class="package-header">
                            <h3>Website Setup</h3>
                            <p>A full website creation package with ongoing yearly support.</p>
                            <div class="package-price">$199 <span class="inr-price">/ ₹14,999</span></div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 5px;">per year</div>
                        </div>
                        <ul class="package-features">
                            <li><i class="fas fa-check"></i> Custom UI/UX Website Design</li>
                            <li><i class="fas fa-check"></i> Basic CMS or HTML Website</li>
                            <li><i class="fas fa-check"></i> Annual Domain & Hosting Setup</li>
                            <li><i class="fas fa-check"></i> Foundational SEO Setup</li>
                        </ul>
                        <a href="https://wa.me/919166226522" class="btn outline-btn package-btn" target="_blank">Book Yearly</a>
                    </div>

                </div>
                
                <div class="pricing-note fade-in-up">
                    <p style="text-align: center; margin-top: 3rem;">* Need one-off services? Logo Design ($25 / ₹1,999) | Post Design ($5 / ₹499) | GMB Setup ($15 / ₹999). Contact me for details.</p>
                </div>
            </div>
        </section>"""

content = re.sub(pattern, new_pricing_html, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
