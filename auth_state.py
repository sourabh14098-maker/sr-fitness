import os

# 1. Update script.js
with open('script.js', 'a', encoding='utf-8') as f:
    f.write('''
// Handle Navbar User State
document.addEventListener('DOMContentLoaded', () => {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  const userDataStr = localStorage.getItem('fitzoneUser');
  
  if (isLoggedIn === 'true' && userDataStr) {
    const user = JSON.parse(userDataStr);
    const navCta = document.querySelector('.nav-cta');
    
    if (navCta) {
      const initial = user.name ? user.name.charAt(0).toUpperCase() : 'U';
      const firstName = user.name ? user.name.split(' ')[0] : 'User';
      
      const profileHtml = `
        <div class="user-profile">
          <div class="user-avatar">${initial}</div>
          <span class="user-name">${firstName}</span>
          <button class="logout-btn" onclick="handleLogout()">Logout</button>
        </div>
      `;
      navCta.outerHTML = profileHtml;
    }
  }
});

function handleLogout() {
  localStorage.setItem('isLoggedIn', 'false');
  window.location.href = 'index.html';
}
''')

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

profile_css = '''
  /* USER PROFILE */
  .user-profile { display: flex; align-items: center; gap: 12px; }
  .user-avatar { width: 34px; height: 34px; background: var(--white); color: var(--black); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Space Mono', monospace; font-size: 16px; font-weight: 700; }
  .user-name { font-family: 'DM Sans', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: var(--white); display: block; }
  .logout-btn { background: transparent; border: 1px solid rgba(255,255,255,0.2); color: var(--gray-400); padding: 6px 12px; border-radius: 4px; font-size: 10px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer; transition: all 0.2s; margin-left: 8px; }
  .logout-btn:hover { border-color: var(--red); color: var(--red); }
  
'''

# Insert before RESPONSIVE DESIGN if possible
if '/* RESPONSIVE DESIGN */' in css:
    css = css.replace('/* RESPONSIVE DESIGN */', profile_css + '/* RESPONSIVE DESIGN */')
else:
    css += profile_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated script.js and style.css successfully.")
