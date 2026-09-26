import re

with open('index.html', 'r') as f:
    content = f.read()

# Update Contact section
old_contact = """                    <a href="mailto:js500224@gmail.com" class="btn solid-btn mt-4">Get in Touch</a>"""
new_contact = """                    <div class="contact-buttons mt-4">
                        <a href="mailto:js500224@gmail.com" class="btn solid-btn">Email Me</a>
                        <a href="https://wa.me/919166226522" target="_blank" class="btn outline-btn">WhatsApp</a>
                    </div>"""
content = content.replace(old_contact, new_contact)

# Update Footer social links
old_footer = """                <a href="https://www.linkedin.com/in/joginderdevwork/" target="_blank" class="social-icon">LinkedIn</a>"""
new_footer = """                <a href="https://www.linkedin.com/in/joginderdevwork/" target="_blank" class="social-icon">LinkedIn</a>
                <a href="https://wa.me/919166226522" target="_blank" class="social-icon">WhatsApp</a>"""
content = content.replace(old_footer, new_footer)

with open('index.html', 'w') as f:
    f.write(content)

# Append to CSS
css_addition = """
.contact-buttons {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)

