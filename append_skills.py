import re

with open('index.html', 'r') as f:
    content = f.read()

skills_section = """
        <div class="divider"></div>

        <section id="skills" class="section skills">
            <div class="container">
                <div class="section-header fade-in-up">
                    <h2>05. Skills & Expertise</h2>
                </div>
                <div class="skills-grid fade-in-up">
                    <div class="skill-category">
                        <h3>Design</h3>
                        <ul class="skill-list">
                            <li>UI/UX Design</li>
                            <li>User Experience (UX)</li>
                            <li>Web Design</li>
                            <li>Responsive Layouts</li>
                        </ul>
                    </div>
                    <div class="skill-category">
                        <h3>Frontend</h3>
                        <ul class="skill-list">
                            <li>HTML5 & CSS3</li>
                            <li>JavaScript (ES6+)</li>
                            <li>React.js</li>
                            <li>Bootstrap & jQuery</li>
                        </ul>
                    </div>
                    <div class="skill-category">
                        <h3>Development & Tools</h3>
                        <ul class="skill-list">
                            <li>WordPress Development</li>
                            <li>Frontend Architecture</li>
                            <li>Problem Solving</li>
                            <li>Creative Coding</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert skills section before contact section
content = content.replace('<section id="contact"', skills_section + '\n        <section id="contact"')

# Update navigation links
nav_addition = '\n            <a href="#skills" class="nav-link">Skills</a>'
content = content.replace('<a href="#contact" class="nav-link">Contact</a>', '<a href="#skills" class="nav-link">Skills</a>\n            <a href="#contact" class="nav-link">Contact</a>')

with open('index.html', 'w') as f:
    f.write(content)
