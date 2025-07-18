describe('Navigation Bar', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('shows auth links when logged out', () => {
    cy.get('#auth-links').should('be.visible');
    cy.get('#user-links').should('not.be.visible');
  });

  it('shows user links after login', () => {
    cy.login('user@cleancity.com', 'password123');
    cy.get('#user-links').should('be.visible');
    cy.get('#auth-links').should('not.be.visible');
  });

  it('hamburger menu toggles', () => {
    cy.get('#hamburger').click();
    cy.get('#nav-menu').should('have.class', 'active');
    cy.get('#hamburger').click();
    cy.get('#nav-menu').should('not.have.class', 'active');
  });
});
