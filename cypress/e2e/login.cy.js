describe('Login Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5500/index.html');
    cy.contains('Login').click();
  });

  it('logs in with demo user', () => {
    cy.get('#login-email').type('user@cleancity.com');
    cy.get('#login-password').type('password123');
    cy.get('#login-form').submit();
    cy.get('#user-links').should('be.visible');
  });

  it('shows dashboard link after login', () => {
    cy.get('#login-email').type('user@cleancity.com');
    cy.get('#login-password').type('password123');
    cy.get('#login-form').submit();
    cy.contains('Dashboard').should('exist');
  });
});
