describe('Register Page', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.get('a[data-page="register"]').click();
  });

  it('registers new user successfully', () => {
    const randomEmail = `test${Date.now()}@cleancity.com`;
    cy.get('#register-form input[name="name"]').type('New User');
    cy.get('#register-form input[name="email"]').type(randomEmail);
    cy.get('#register-form input[name="password"]').type('pass123');
    cy.get('#register-form input[name="confirmPassword"]').type('pass123');
    cy.get('#register-form').submit();

    cy.get('#register-success').should('contain', 'Registration successful');
  });

  it('shows validation errors for missing fields', () => {
    cy.get('#register-form').submit();
    cy.get('#register-error').should('contain', 'Name is required');
  });
});
