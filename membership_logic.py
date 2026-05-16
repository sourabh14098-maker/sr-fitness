import os

# 1. Update membership.html buttons
with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<button class="plan-btn plan-btn-ghost">Get Started</button>',
    '<button class="plan-btn plan-btn-ghost" onclick="selectPlan(\'Starter\', \'₹1,499\')">Get Started</button>'
)
html = html.replace(
    '<button class="plan-btn plan-btn-solid">Join Pro →</button>',
    '<button class="plan-btn plan-btn-solid" onclick="selectPlan(\'Pro Athlete\', \'₹3,499\')">Join Pro →</button>'
)
html = html.replace(
    '<button class="plan-btn plan-btn-ghost">Go Elite</button>',
    '<button class="plan-btn plan-btn-ghost" onclick="selectPlan(\'Elite\', \'₹7,999\')">Go Elite</button>'
)

with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Append Logic to script.js
with open('script.js', 'a', encoding='utf-8') as f:
    f.write('''

// Membership Plan Logic
function selectPlan(planName, planPrice) {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  
  if (isLoggedIn !== 'true') {
    alert("Please log in or create an account to select a membership plan.");
    window.location.href = 'auth.html';
    return;
  }
  
  const planDetails = { name: planName, price: planPrice };
  localStorage.setItem('selectedMembershipPlan', JSON.stringify(planDetails));
  
  alert(`You selected the ${planName} plan!`);
  window.location.href = 'workouts.html'; // Redirect to Dashboard
}

// Display Membership on Dashboard
document.addEventListener('DOMContentLoaded', () => {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  const planDataStr = localStorage.getItem('selectedMembershipPlan');
  
  // Only inject if on a page with stats-strip (like workouts.html) and logged in
  const statsStrip = document.querySelector('.stats-strip');
  
  if (isLoggedIn === 'true' && planDataStr && statsStrip) {
    const planDetails = JSON.parse(planDataStr);
    
    // Check if we already injected it (to prevent duplicates on navigation)
    if (!document.getElementById('membership-banner')) {
      const bannerHtml = `
        <div id="membership-banner" style="background: var(--gray-800); padding: 20px 40px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto;">
          <div>
            <div style="font-size: 11px; color: var(--gray-400); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">Current Membership</div>
            <div style="font-family: 'Bebas Neue', cursive; font-size: 24px; color: var(--white);"><span style="color: var(--red);">${planDetails.name.toUpperCase()}</span> PLAN</div>
          </div>
          <div style="text-align: right;">
            <div style="font-size: 11px; color: var(--gray-400); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">Billing</div>
            <div style="font-family: 'Space Mono', monospace; font-size: 14px; color: var(--white);">${planDetails.price} / mo</div>
          </div>
        </div>
      `;
      statsStrip.insertAdjacentHTML('afterend', bannerHtml);
    }
  }
});
''')

print("Membership logic updated successfully.")
