// BMI Calculator
function calculateBMI() {
  const gender = document.getElementById('gender').value;
  const age = parseFloat(document.getElementById('age').value);
  const height = parseFloat(document.getElementById('height').value);
  const weight = parseFloat(document.getElementById('weight').value);
  const activity = parseFloat(document.getElementById('activity').value);
  if (!age || !height || !weight) { alert('Please fill in all fields.'); return; }
  const bmi = weight / ((height / 100) ** 2);
  const bmr = gender === 'male'
    ? 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    : 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age);
  const tdee = Math.round(bmr * activity);
  let category, color, barColor, barPct, recs, idealWeight;
  const heightM = height / 100;
  idealWeight = [18.5 * heightM * heightM, 24.9 * heightM * heightM];
  if (bmi < 18.5) {
    category = 'Underweight'; color = '#999999'; barColor = '#999999'; barPct = Math.round((bmi / 18.5) * 25);
    recs = ['Increase caloric intake by 300–500 kcal above TDEE', 'Focus on compound lifts to build lean mass', 'Prioritize protein intake at 1.6–2.2g per kg bodyweight', 'Consider mass-gaining program with progressive overload'];
  } else if (bmi < 25) {
    category = 'Normal Weight'; color = '#cccccc'; barColor = '#cccccc'; barPct = Math.round(25 + ((bmi - 18.5) / 6.4) * 40);
    recs = ['Maintain current habits — you are in an optimal range', 'Body recomposition program recommended for muscle gain', 'Keep protein intake consistent at 1.6g per kg', 'Focus on performance metrics over scale weight'];
  } else if (bmi < 30) {
    category = 'Overweight'; color = '#aaaaaa'; barColor = '#aaaaaa'; barPct = Math.round(65 + ((bmi - 25) / 5) * 20);
    recs = ['Target a 500 kcal daily deficit for ~0.5kg/week loss', 'Prioritize HIIT and cardio alongside strength training', 'Track all food intake — awareness is the first step', 'Consider Fat Incinerator or Body Recomp program'];
  } else {
    category = 'Obese'; color = '#ffffff'; barColor = '#ffffff'; barPct = Math.min(95, Math.round(85 + ((bmi - 30) / 10) * 10));
    recs = ['Consult with a physician before starting intense training', 'Begin with low-impact cardio — walking, swimming, cycling', 'Create a structured caloric deficit with professional guidance', 'Focus on sustainable lifestyle habits over quick fixes'];
  }
  const resultsEl = document.getElementById('bmi-results');
  resultsEl.innerHTML = `
    <div>
      <div style="margin-bottom:2rem">
        <div style="font-size:11px;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;color:var(--gray-400);margin-bottom:0.5rem">Your BMI Score</div>
        <div style="font-family:'Bebas Neue',cursive;font-size:5rem;line-height:1;color:${color}">${bmi.toFixed(1)}</div>
        <div style="font-size:13px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:${color};margin-bottom:1.5rem">${category}</div>
        <div style="height:10px;border-radius:5px;background:var(--gray-600);overflow:hidden;margin-bottom:0.5rem">
          <div style="height:100%;width:${barPct}%;border-radius:5px;background:${barColor};transition:width 0.8s ease"></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--gray-400)">
          <span>Underweight &lt;18.5</span><span>Normal 18.5–24.9</span><span>Overweight 25–29.9</span><span>Obese 30+</span>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:2rem">
        <div style="background:rgba(255,255,255,0.04);border-radius:6px;padding:1rem;border:1px solid rgba(255,255,255,0.06)">
          <div style="font-size:10px;color:var(--gray-400);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px">Daily TDEE</div>
          <div style="font-family:'Bebas Neue',cursive;font-size:1.8rem;color:var(--white)">${tdee.toLocaleString()}</div>
          <div style="font-size:11px;color:var(--gray-400)">calories/day</div>
        </div>
        <div style="background:rgba(255,255,255,0.04);border-radius:6px;padding:1rem;border:1px solid rgba(255,255,255,0.06)">
          <div style="font-size:10px;color:var(--gray-400);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px">Ideal Weight</div>
          <div style="font-family:'Bebas Neue',cursive;font-size:1.8rem;color:var(--white)">${Math.round(idealWeight[0])}–${Math.round(idealWeight[1])}</div>
          <div style="font-size:11px;color:var(--gray-400)">kg target range</div>
        </div>
      </div>
      <div>
        <div style="font-size:11px;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;color:var(--gray-400);margin-bottom:1rem">Personalized Recommendations</div>
        <div style="display:flex;flex-direction:column;gap:10px">
          ${recs.map(r => `<div style="display:flex;align-items:flex-start;gap:10px"><span style="color:var(--red);font-size:12px;margin-top:2px;flex-shrink:0">→</span><span style="font-size:13px;color:var(--gray-400);line-height:1.5">${r}</span></div>`).join('')}
        </div>
      </div>
      <button class="calc-btn" style="margin-top:1.5rem" onclick="window.location.href='workouts.html'">View Recommended Programs →</button>
    </div>
  `;
}

// Diet tabs
function switchDiet(type) {
  document.querySelectorAll('.diet-tab').forEach((t, i) => {
    t.classList.toggle('active', ['bulk', 'cut', 'maintain'][i] === type);
  });
  document.querySelectorAll('.diet-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('diet-' + type).classList.add('active');
}

// Auth tabs
function switchAuth(type) {
  document.querySelectorAll('.auth-tab').forEach((t, i) => {
    t.classList.toggle('active', ['login', 'signup'][i] === type);
  });
  document.querySelectorAll('.auth-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('auth-' + type).classList.add('active');
}

// Live feed rotation
const feeds = [
  'Hydrate every 15 minutes of intense cardio.',
  '12 members completed Strength Forge today.',
  'New: Mobility Matrix program — starts Monday.',
  'Tip: Sleep 7–9 hours for optimal recovery.',
  'Priya Nair has 2 coaching slots available this week.',
  '🔥 Record broken: 847 sessions completed today.',
];
let fi = 0;
setInterval(() => {
  fi = (fi + 1) % feeds.length;
  const el = document.getElementById('live-text');
  el.style.opacity = 0;
  setTimeout(() => { el.textContent = feeds[fi]; el.style.opacity = 1; }, 300);
}, 4000);

// Authentication Logic
function showAuthMsg(msg, isError) {
  const msgEl = document.getElementById('auth-msg');
  if (!msgEl) return;
  msgEl.textContent = msg;
  msgEl.style.display = 'block';
  msgEl.style.backgroundColor = isError ? 'rgba(232, 52, 26, 0.1)' : 'rgba(76, 175, 80, 0.1)';
  msgEl.style.color = isError ? '#e8341a' : '#4caf50';
  msgEl.style.borderColor = isError ? 'rgba(232, 52, 26, 0.3)' : 'rgba(76, 175, 80, 0.3)';
}

function handleSignup(e) {
  e.preventDefault();
  const name = document.getElementById('signup-name').value;
  const email = document.getElementById('signup-email').value;
  const password = document.getElementById('signup-password').value;

  if (!name || !email || !password) {
    showAuthMsg("All fields are required.", true);
    return;
  }

  if (password.length < 6) {
    showAuthMsg("Password must be at least 6 characters.", true);
    return;
  }

  const user = { name, email, password };
  localStorage.setItem('fitzoneUser', JSON.stringify(user));

  showAuthMsg("Account created successfully!", false);

  // Switch to login tab automatically after 1 second
  setTimeout(() => {
    switchAuth('login');
    document.getElementById('auth-msg').style.display = 'none';
    document.getElementById('login-email').value = email;
  }, 1000);
}

function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;

  const savedUserData = localStorage.getItem('fitzoneUser');
  if (!savedUserData) {
    showAuthMsg("No account found. Please create one.", true);
    return;
  }

  const savedUser = JSON.parse(savedUserData);

  if (email === savedUser.email && password === savedUser.password) {
    localStorage.setItem('isLoggedIn', 'true');
    window.location.href = 'workouts.html'; // Redirect to Dashboard/Workouts
  } else {
    showAuthMsg("Invalid email or password.", true);
  }
}


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


// Program Enrollment Logic
function enrollProgram(programName) {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  if (isLoggedIn !== 'true') {
    // Custom styled alert or just redirect
    showAuthMsg("Please log in to join a program.", true);
    setTimeout(() => {
      window.location.href = 'auth.html';
    }, 1500);
    return;
  }

  localStorage.setItem('enrolledProgram', programName);

  // Show a nice temporary overlay message or update UI
  updateEnrolledUI();
}

function updateEnrolledUI() {
  const enrolled = localStorage.getItem('enrolledProgram');
  if (!enrolled) return;

  document.querySelectorAll('.program-card').forEach(card => {
    const nameEl = card.querySelector('.program-name');
    const arrowEl = card.querySelector('.program-arrow');
    if (nameEl && nameEl.textContent.trim() === enrolled) {
      card.style.borderColor = 'var(--red)';
      card.style.background = 'rgba(232, 52, 26, 0.03)';
      if (arrowEl) {
        arrowEl.innerHTML = '<span style="color:var(--red);font-size:11px;font-weight:700;letter-spacing:0.1em;">✓ ENROLLED</span>';
      }
    } else {
      card.style.borderColor = 'rgba(255,255,255,0.05)';
      card.style.background = 'transparent';
      if (arrowEl) arrowEl.textContent = '→';
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  // Attach click listeners to all program cards
  document.querySelectorAll('.program-card').forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', () => {
      const nameEl = card.querySelector('.program-name');
      if (nameEl) {
        enrollProgram(nameEl.textContent.trim());
      }
    });
  });

  // Initialize UI if already enrolled
  updateEnrolledUI();
});


// Trainer Booking Logic
function bookTrainer(trainerName) {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  if (isLoggedIn !== 'true') {
    showAuthMsg("Please log in to book a trainer.", true);
    setTimeout(() => {
      window.location.href = 'auth.html';
    }, 1500);
    return;
  }

  localStorage.setItem('bookedTrainer', trainerName);
  updateBookedTrainerUI();
}

function updateBookedTrainerUI() {
  const booked = localStorage.getItem('bookedTrainer');
  if (!booked) return;

  document.querySelectorAll('.trainer-card').forEach(card => {
    const nameEl = card.querySelector('.trainer-name');
    if (nameEl && nameEl.textContent.trim() === booked) {
      card.style.borderColor = 'var(--red)';
      card.style.boxShadow = '0 0 20px rgba(232,52,26,0.1)';

      // Check if badge already exists
      if (!card.querySelector('.booked-badge')) {
        const badge = document.createElement('div');
        badge.className = 'booked-badge';
        badge.innerHTML = '✓ BOOKED';
        badge.style.position = 'absolute';
        badge.style.top = '16px';
        badge.style.right = '16px';
        badge.style.background = 'var(--red)';
        badge.style.color = 'var(--black)';
        badge.style.padding = '4px 8px';
        badge.style.borderRadius = '4px';
        badge.style.fontSize = '10px';
        badge.style.fontWeight = '700';
        badge.style.letterSpacing = '0.1em';
        badge.style.zIndex = '10';

        // ensure parent is relative
        card.style.position = 'relative';
        card.appendChild(badge);
      }
    } else {
      card.style.borderColor = 'rgba(255,255,255,0.05)';
      card.style.boxShadow = 'none';
      const badge = card.querySelector('.booked-badge');
      if (badge) badge.remove();
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  // Attach click listeners to all trainer cards
  document.querySelectorAll('.trainer-card').forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', () => {
      const nameEl = card.querySelector('.trainer-name');
      if (nameEl) {
        bookTrainer(nameEl.textContent.trim());
      }
    });
  });

  // Initialize UI if already booked
  updateBookedTrainerUI();
});


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
