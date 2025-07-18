describe('Dashboard Page', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.login('user@cleancity.com', 'password123'); // use a custom command
  });

  it('displays pickup requests table', () => {
    cy.get('a[data-page="dashboard"]').click();
    cy.get('#requests-tbody tr').should('have.length.greaterThan', 0);
    cy.get('#filter-count').should('contain', 'Showing');
  });

  it('filters by status', () => {
    cy.get('#statusFilter').select('Pending');
    cy.get('#requests-tbody tr').each(($tr) => {
      cy.wrap($tr).contains('Pending');
    });
  });

  it('filters by location', () => {
    cy.get('#locationFilter').select('Nairobi');
    cy.get('#requests-tbody tr').each(($tr) => {
      cy.wrap($tr).contains('Nairobi');
    });
  });
});
