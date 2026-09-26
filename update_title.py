with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('<title>Joginder Verma | UI/UX Specialist</title>', '<title>Joginder Verma</title>')

with open('index.html', 'w') as f:
    f.write(content)
