describe('Pruebas E2E aplicación videojuegos', () => {

  it('Carga la página principal', () => {
    cy.visit('/')
    cy.contains('Videojuegos')
  })

  it('Carga API correctamente', () => {
    cy.request('/api')
      .its('status')
      .should('eq', 200)
  })
    
  it('Comprueba navegación', () => {

    cy.visit('/')
    cy.get('body').should('be.visible')

  })

})