describe('Pickup Request Form', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.login('user@cleancity.com', 'password123');
    cy.get('a[data-page="dashboard"]').click();
  });

  it('submits pickup request successfully', () => {
    cy.get('a[data-page="home"]').click();
    cy.get('#pickup-form input[name="fullName"]').type('Test User');
    cy.get('#pickup-form select[name="location"]').select('Nairobi');
    cy.get('#pickup-form select[name="wasteType"]').select('General Waste');
    cy.get('#pickup-form input[name="preferredDate"]').type('2025-08-01');
    cy.get('#pickup-form').submit();

    cy.get('#success-message').should('contain', 'Request submitted');
  });

  it('validates required fields', () => {
    cy.get('#pickup-form').submit();
    cy.get('#name-error').should('contain', 'Full name is required');
    cy.get('#location-error').should('contain', 'Please select a location');
    cy.get('#waste-error').should('contain', 'Please select a waste type');
  });
});
