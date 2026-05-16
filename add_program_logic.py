with open('script.js', 'a', encoding='utf-8') as f:
    f.write('''

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
''')
print("Successfully appended program logic to script.js")
