describe('Registration Form Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5500/index.html');
    cy.contains('Register').click();
  });

  it('shows required field validation', () => {
    cy.get('#register-form').within(() => {
      cy.get('button[type="submit"]').click();
    });
    cy.get('#register-name').then(input => {
      expect(input[0].checkValidity()).to.equal(false);
    });
  });

  // optional: valid registration (if your backend allows duplicates, else skip)
  it('registers a new account', () => {
    const randomEmail = `test${Date.now()}@mail.com`;
    cy.get('#register-name').type('Test User');
    cy.get('#register-email').type(randomEmail);
    cy.get('#register-password').type('abc123');
    cy.get('#register-confirm-password').type('abc123');
    cy.get('#register-form').submit();
    cy.get('#register-success').should('be.visible');
  });
});
