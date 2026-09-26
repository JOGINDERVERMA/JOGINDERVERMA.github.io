with open('index.html', 'r') as f:
    content = f.read()

# Update desktop nav
content = content.replace('<a href="#pricing" class="nav-link">Pricing</a>\n            <a href="#contact" class="nav-link">Contact</a>',
                          '<a href="#pricing" class="nav-link">Pricing</a>\n            <a href="blog.html" class="nav-link">Blog</a>\n            <a href="#contact" class="nav-link">Contact</a>')

# Update mobile nav
content = content.replace('<a href="#pricing" class="mobile-link">06. Pricing</a>\n            <a href="#contact" class="mobile-link">07. Contact</a>',
                          '<a href="#pricing" class="mobile-link">06. Pricing</a>\n            <a href="blog.html" class="mobile-link">07. Blog</a>\n            <a href="#contact" class="mobile-link">08. Contact</a>')

with open('index.html', 'w') as f:
    f.write(content)
