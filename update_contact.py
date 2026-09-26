with open('index.html', 'r') as f:
    content = f.read()

old_contact = """                    <p>I'm always open to discussing new concepts, creative ideas, or opportunities to be part of your vision.</p>
                    <div class="contact-buttons mt-4">"""

new_contact = """                    <p>I'm always open to discussing new concepts, creative ideas, or opportunities to be part of your vision.</p>
                    
                    <div class="contact-details" style="margin: 2rem 0;">
                        <p style="margin-bottom: 0.5rem; font-size: 1.2rem; color: var(--text-primary);"><strong>Email:</strong> <a href="mailto:js500224@gmail.com" style="color: var(--text-primary); text-decoration: underline; text-underline-offset: 4px;">js500224@gmail.com</a></p>
                        <p style="margin-bottom: 0; font-size: 1.2rem; color: var(--text-primary);"><strong>Phone:</strong> <a href="tel:+919166226522" style="color: var(--text-primary); text-decoration: underline; text-underline-offset: 4px;">+91 9166226522</a></p>
                    </div>

                    <div class="contact-buttons">"""

content = content.replace(old_contact, new_contact)

with open('index.html', 'w') as f:
    f.write(content)
