describe('Dashboard Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5500/index.html');
    cy.contains('Login').click();
    cy.get('#login-email').type('user@cleancity.com');
    cy.get('#login-password').type('password123');
    cy.get('#login-form').submit();
    cy.contains('Dashboard').click();
  });

  it('shows requests table', () => {
    cy.get('#dashboard-page').should('be.visible');
    cy.get('#requests-tbody tr').should('exist');
  });

  it('filters by status', () => {
    cy.get('#statusFilter').select('Pending');
    cy.get('#filter-count').should('contain', 'Showing');
  });
});
