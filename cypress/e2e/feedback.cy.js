describe('Feedback Page', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.login('user@cleancity.com', 'password123');
    cy.get('a[data-page="feedback"]').click();
  });

  it('submits feedback successfully', () => {
    cy.get('#feedback-form select[name="requestId"]').select('REQ001');
    cy.get('#feedback-form select[name="reason"]').select('Delayed pickup');
    cy.get('#feedback-form textarea[name="comments"]').type('Pickup was delayed by 2 days.');
    cy.get('#feedback-form').submit();

    cy.get('#feedback-success').should('contain', 'Feedback submitted');
  });

  it('validates required fields', () => {
    cy.get('#feedback-form').submit();
    cy.get('#requestId-error').should('contain', 'Request ID is required');
    cy.get('#reason-error').should('contain', 'Please select a reason');
  });
});
