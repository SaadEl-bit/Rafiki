import os
import re

app_dir = 'h:/Study/Projects/M3allem/Github/Rafiki/frontend/app'

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix unclosed img tags
    # regex to match <img ... > where it might span multiple lines
    content = re.sub(r'<img([^>]*?)(?<!/)>', r'<img\1 />', content)
    
    # Fix unclosed input tags
    content = re.sub(r'<input([^>]*?)(?<!/)>', r'<input\1 />', content)
    
    # Fix unclosed br tags
    content = re.sub(r'<br([^>]*?)(?<!/)>', r'<br\1 />', content)

    # Fix unclosed hr tags
    content = re.sub(r'<hr([^>]*?)(?<!/)>', r'<hr\1 />', content)

    # Fix unclosed path tags
    content = re.sub(r'<path([^>]*?)(?<!/)>', r'<path\1 />', content)
    
    # Fix unclosed circle tags
    content = re.sub(r'<circle([^>]*?)(?<!/)>', r'<circle\1 />', content)

    # Fix stroke-* attributes to camelCase
    content = re.sub(r'stroke-width=', r'strokeWidth=', content)
    content = re.sub(r'stroke-dasharray=', r'strokeDasharray=', content)
    content = re.sub(r'stroke-dashoffset=', r'strokeDashoffset=', content)
    content = re.sub(r'stroke-linecap=', r'strokeLinecap=', content)
    content = re.sub(r'stroke-linejoin=', r'strokeLinejoin=', content)
    
    # Fix for= to htmlFor=
    content = re.sub(r' for="', r' htmlFor="', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk(app_dir):
    for file in files:
        if file.endswith('.js') or file.endswith('.jsx'):
            fix_file(os.path.join(root, file))

print("JSX fix complete.")
