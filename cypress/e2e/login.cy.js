describe('Login Page', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.get('a[data-page="login"]').click();
  });

  it('logs in with valid credentials', () => {
    cy.get('#login-form input[name="email"]').type('user@cleancity.com');
    cy.get('#login-form input[name="password"]').type('password123');
    cy.get('#login-form').submit();

    cy.get('#login-success').should('contain', 'Login successful');
    cy.get('#dashboard-page').should('be.visible');
  });

  it('shows error for invalid credentials', () => {
    cy.get('#login-form input[name="email"]').type('invalid@cleancity.com');
    cy.get('#login-form input[name="password"]').type('wrongpass');
    cy.get('#login-form').submit();

    cy.get('#login-error').should('contain', 'Invalid email or password');
  });
});
