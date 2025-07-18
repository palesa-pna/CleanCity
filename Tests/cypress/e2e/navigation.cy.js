describe('Navigation Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5500/index.html'); // adjust to your local server
  });

  it('loads Home page and shows nav bar', () => {
    cy.get('nav.navbar').should('exist');
    cy.contains('Home').should('have.class', 'active');
  });

  it('navigates to Register page', () => {
    cy.contains('Register').click();
    cy.get('#register-page').should('be.visible');
  });

  it('navigates to Login page', () => {
    cy.contains('Login').click();
    cy.get('#login-page').should('be.visible');
  });

  it('navigates to Awareness page', () => {
    cy.contains('Awareness').click();
    cy.get('#awareness-page').should('be.visible');
    cy.contains('Waste Management Awareness').should('exist');
  });
});
