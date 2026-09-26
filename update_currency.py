import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace prices in HTML
content = content.replace('<div class="package-price">$350</div>', 
                          '<div class="package-price">$350 <span class="inr-price">/ ₹28,999</span></div>')

content = content.replace('<div class="package-price">$750</div>', 
                          '<div class="package-price">$750 <span class="inr-price">/ ₹59,999</span></div>')

content = content.replace('<div class="package-price">From $1,200</div>', 
                          '<div class="package-price">From $1,200 <span class="inr-price">/ ₹99,999</span></div>')

# Replace footnote prices
old_footnote = "* Need individual services? Logo Design ($150) | Post Design ($25) | GMB ($75). Contact me for custom quotes."
new_footnote = "* Need individual services? Logo Design ($150 / ₹11,999) | Post Design ($25 / ₹1,999) | GMB ($75 / ₹5,999). Contact me for custom quotes."
content = content.replace(old_footnote, new_footnote)


with open('index.html', 'w') as f:
    f.write(content)

# CSS for the secondary currency
css_addition = """
.inr-price {
    font-size: 1.2rem;
    color: var(--text-secondary);
    font-weight: 500;
    font-family: 'Inter', sans-serif;
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)
