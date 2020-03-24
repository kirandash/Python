describe('filters items', () => {
  it('filters items by using search', () => {
    cy.visit('http://localhost:3000'); // Visit home page
    cy.contains('Difficulty Rating').should('exist'); 
    cy.contains('Learn more!').should('exist'); // Check if home page content exists

    cy.get('input[name=search]').type('hiking'); // Fill the data for form
    cy.contains('Apply').click(); // Click Apply Filter
    cy.contains('Learn more!').should('exist'); // Check if result appears witih learn more btn
  });
})
