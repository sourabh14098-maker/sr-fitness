import os
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the button
    content = content.replace('<button class="nav-cta">Join Now</button>', '<button class="nav-cta" onclick="window.location.href=\'membership.html\'">Join Now</button>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
