import re

with open('index.html', 'r') as f:
    content = f.read()

# Insert sticky whatsapp before </body>
sticky_html = """
    <a href="https://wa.me/919166226522" target="_blank" class="whatsapp-sticky">
        <i class="fab fa-whatsapp"></i>
    </a>

    <script src="js/script.js">"""
content = content.replace('<script src="js/script.js">', sticky_html)

with open('index.html', 'w') as f:
    f.write(content)

# Append to CSS
css_addition = """
/* Sticky WhatsApp */
.whatsapp-sticky {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 60px;
    height: 60px;
    background-color: #25d366;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 35px;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
    z-index: 1000;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-decoration: none;
}

.whatsapp-sticky:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 8px 25px rgba(37, 211, 102, 0.5);
    color: white;
}

@media (max-width: 768px) {
    .whatsapp-sticky {
        width: 50px;
        height: 50px;
        font-size: 28px;
        bottom: 20px;
        right: 20px;
    }
}
"""
with open('css/style.css', 'a') as f:
    f.write(css_addition)
