import os
import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract CSS
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if css_match:
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_match.group(1).strip())
    html = html.replace(css_match.group(0), '<link rel="stylesheet" href="style.css">')

# Extract JS
js_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if js_match:
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js_match.group(1).strip())
    html = html.replace(js_match.group(0), '<script src="script.js"></script>')

# Update Navigation Links
nav_replacements = [
    ('href="#home"', 'href="index.html"'),
    ('href="#programs"', 'href="workouts.html"'),
    ('href="#diet"', 'href="diet.html"'),
    ('href="#trainers"', 'href="trainers.html"'),
    ('href="#bmi"', 'href="bmi.html"'),
    ('href="#membership"', 'href="membership.html"')
]
for old, new in nav_replacements:
    html = html.replace(old, new)

# Define sections
sections = {
    'index': r'(<!-- HERO -->.*?</section>)',
    'workouts': r'(<!-- PROGRAMS -->.*?</section>\s*<!-- ANALYSIS DASHBOARD -->.*?</section>)',
    'diet': r'(<!-- DIET PLANS -->.*?</section>)',
    'trainers': r'(<!-- TRAINERS -->.*?</section>)',
    'bmi': r'(<!-- BMI CALCULATOR -->.*?</section>)',
    'membership': r'(<!-- MEMBERSHIP -->.*?</section>)'
}

extracted_sections = {}
for name, pattern in sections.items():
    match = re.search(pattern, html, re.DOTALL)
    if match:
        extracted_sections[name] = match.group(1)
        # Remove from main html for now
        html = html.replace(match.group(1), f'<!-- INSERT_{name.upper()} -->')

# Generate each page
for name in sections.keys():
    page_html = html
    # Remove all markers and insert the correct one
    for n in sections.keys():
        if n == name:
            page_html = page_html.replace(f'<!-- INSERT_{n.upper()} -->', extracted_sections[n])
        else:
            page_html = page_html.replace(f'<!-- INSERT_{n.upper()} -->', '')
    
    # Update title
    title = 'SR FITNESS — ' + (name.capitalize() if name != 'index' else 'Forge Your Ultimate Self')
    page_html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', page_html)
    
    # Update active nav link
    page_html = re.sub(r'class="active"', '', page_html)
    page_html = page_html.replace(f'href="{name}.html"', f'href="{name}.html" class="active"')
    if name == 'index':
         page_html = page_html.replace('href="index.html"', 'href="index.html" class="active"')
    
    filename = f'{name}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        # cleanup empty lines
        clean_html = os.linesep.join([s for s in page_html.splitlines() if s.strip() != ''])
        f.write(clean_html)

print("Split completed successfully!")
