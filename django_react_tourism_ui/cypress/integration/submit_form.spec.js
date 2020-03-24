// Checkout Form testing end 2 end
describe('checkout form', () => {
  it('adds item to cart and submits checkout form', () => {
    cy.visit('http://localhost:3000'); // visit home page
    cy.contains('Learn more!').click(); // Visit details page
    cy.contains('Reserve').click(); // Click on reserve btn for add to cart
    cy.get('[name=name]').type('name'); // Fill the form
    cy.get('[name=email_address]').type('email@localhost')
    cy.get('[name=street_address]').type('123 Address St.');
    cy.get('[name=city]').type('City');
    cy.contains('Place order').click(); // After form is filled, click on Place order btn
    cy.get('li.error').should('have.length', 0); // make sure there are no erros
    cy.contains('Thanks for buying').should('exist'); // Make sure Thanks for buying text exists
  });
})
