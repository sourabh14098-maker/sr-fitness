import os
import glob
import re

# 1. Read membership.html
with open('membership.html', 'r', encoding='utf-8') as f:
    membership_html = f.read()

# 2. Extract auth section
auth_pattern = r'(<!-- CLIENT PORTAL.*?)</section>\s*<!-- FOOTER -->'
match = re.search(auth_pattern, membership_html, re.DOTALL)
if match:
    auth_section = match.group(1) + '</section>\n\n'
    # Remove from membership.html
    new_membership_html = membership_html.replace(auth_section, '')
    with open('membership.html', 'w', encoding='utf-8') as f:
        f.write(new_membership_html)
else:
    print("Auth section not found in membership.html")
    # If not found, maybe I already ran this. Let's assume it's in membership.html for now.

# 3. Create auth.html by using membership.html as a template
# We will replace the membership-section and stats-strip with auth-section
template_match = re.search(r'(.*?<!-- STATS STRIP -->).*?(<!-- FOOTER -->.*)', new_membership_html, re.DOTALL)
if template_match:
    auth_html = template_match.group(1) + '\n\n' + auth_section + template_match.group(2)
    # Fix the active class in nav
    auth_html = auth_html.replace('href="membership.html" class="active"', 'href="membership.html"')
    # Add active class to nothing, or maybe keep it simple
    # Change title
    auth_html = auth_html.replace('<title>SR FITNESS — Membership</title>', '<title>SR FITNESS — Portal</title>')
    
    # Actually, we should completely remove stats-strip from auth.html to make it clean
    auth_html = re.sub(r'<!-- STATS STRIP -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>', '', auth_html, flags=re.DOTALL)
    
    with open('auth.html', 'w', encoding='utf-8') as f:
        f.write(auth_html)

# 4. Update all navigation buttons to point to auth.html
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("window.location.href='membership.html'", "window.location.href='auth.html'")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
