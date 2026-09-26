with open('index.html', 'r') as f:
    content = f.read()

old_skills = """                            <li>WordPress Development</li>
                            <li>Frontend Architecture</li>
                            <li>Problem Solving</li>
                            <li>Creative Coding</li>"""

new_skills = """                            <li>WordPress Development</li>
                            <li>Frontend Architecture</li>
                            <li>Problem Solving</li>
                            <li>Bug & Error Fixing</li>"""

content = content.replace(old_skills, new_skills)

with open('index.html', 'w') as f:
    f.write(content)
