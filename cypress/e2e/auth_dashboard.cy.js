describe('Auth and Dashboard Integration', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.clearLocalStorage();
  });

  it('logs in and navigates to dashboard', () => {
    cy.get('a[data-page="login"]').click();
    cy.get('#login-form input[name="email"]').type('user@cleancity.com');
    cy.get('#login-form input[name="password"]').type('password123');
    cy.get('#login-form').submit();

    cy.get('#login-success').should('contain', 'Login successful');
    cy.get('#dashboard-page').should('be.visible');
    cy.get('#welcome-text').should('contain', 'Demo User');
  });

  it('redirects to login when accessing dashboard unauthenticated', () => {
    cy.visit('/#dashboard');
    cy.get('#login-page').should('be.visible');
  });
});
