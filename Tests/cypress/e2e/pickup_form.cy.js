describe('Pickup Request Form', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5500/index.html'); // Adjust if hosted elsewhere
    cy.window().then(win => win.localStorage.clear()); // Clear storage for a clean state
  });

  it('submits a valid pickup request', () => {
    // Simulate logged-in user
    cy.window().then(win => {
      win.localStorage.setItem('currentUser', JSON.stringify({
        id: '1', email: 'user@cleancity.com', name: 'Demo User', role: 'user'
      }));
    });

    cy.reload(); // Reload page after setting localStorage

    cy.get('#pickup-form').within(() => {
      cy.get('input[name="fullName"]').type('Test User');
      cy.get('select[name="location"]').select('Nairobi');
      cy.get('select[name="wasteType"]').select('General Waste');
      cy.get('input[name="preferredDate"]').type('2025-07-20');
      cy.root().submit();
    });

    cy.get('#success-message').should('contain.text', 'Request submitted successfully!');

    cy.window().then(win => {
      const data = JSON.parse(win.localStorage.getItem('cleancity_pickup_requests'));
      expect(data.some(r => r.name === 'Test User')).to.be.true;
    });
  });
});
