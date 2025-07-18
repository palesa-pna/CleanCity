describe('Pickup Request Form', () => {
  beforeEach(() => {
    cy.visit('index.html'); // adjust if hosted elsewhere
    // optionally clear storage for a clean state
    cy.window().then(win => win.localStorage.clear());
  });

  it('submits a valid pickup request', () => {
    cy.get('[data-page="dashboard"]').click(); // login first if needed
    // For test, simulate a logged-in user
    cy.window().then((win) => {
      win.localStorage.setItem('currentUser', JSON.stringify({
        id: '1', email: 'user@cleancity.com', name: 'Demo User', role: 'user'
      }));
      win.location.reload();
    });

    cy.get('[data-page="home"]').click();
    cy.get('#pickup-form').within(() => {
      cy.get('input[name="fullName"]').type('Test User');
      cy.get('select[name="location"]').select('Nairobi');
      cy.get('select[name="wasteType"]').select('General Waste');
      cy.get('input[name="preferredDate"]').type('2025-07-20');
      cy.root().submit();
    });

    cy.get('#success-message').should('contain.text', 'Request submitted successfully!');
    // verify localStorage
    cy.window().then(win => {
      const data = JSON.parse(win.localStorage.getItem('cleancity_pickup_requests'));
      expect(data.some(r => r.name === 'Test User')).to.be.true;
    });
  });
});
