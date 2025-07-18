describe('Feedback Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5500/index.html');
    cy.contains('Login').click();
    cy.get('#login-email').type('user@cleancity.com');
    cy.get('#login-password').type('password123');
    cy.get('#login-form').submit();
    cy.contains('Feedback').click();
  });

  it('submits feedback successfully', () => {
    cy.get('#requestId').type('REQ001');
    cy.get('#reason').select('Missed Pickup');
    cy.get('#comments').type('Test feedback from Cypress');
    cy.get('#feedback-form').submit();
    cy.get('#feedback-success').should('be.visible');
  });
});
