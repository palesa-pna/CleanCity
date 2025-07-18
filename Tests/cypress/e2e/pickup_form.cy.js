describe('Pickup Request Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5500/index.html');
    // login first
    cy.contains('Login').click();
    cy.get('#login-email').type('user@cleancity.com');
    cy.get('#login-password').type('password123');
    cy.get('#login-form').submit();
    cy.contains('Home').click();
  });

  it('submits a pickup request', () => {
    cy.get('#pickup-form').within(() => {
      cy.get('#fullName').type('Cypress User');
      cy.get('#location').select('Nairobi');
      cy.get('input[name="wasteType"][value="General"]').check();
      cy.get('#preferredDate').type('2025-08-01');
      cy.get('button[type="submit"]').click();
    });
    cy.get('#success-message').should('be.visible');
  });
});
