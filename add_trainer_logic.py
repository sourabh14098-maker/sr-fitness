with open('script.js', 'a', encoding='utf-8') as f:
    f.write('''

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
''')
print("Successfully appended trainer logic to script.js")
