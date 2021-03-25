function createTable (tableData) {
  const table = document.createElement('table').appendChild(
    tableData.reduce((tbody, rowData) => {
      tbody.appendChild(
        rowData.reduce((tr, cellData) => {
          tr.appendChild(
            document
              .createElement('td')
              .appendChild(document.createTextNode(cellData))
          )
          return tr
        }, document.createElement('tr'))
      )
      return tbody
    }, document.createElement('tbody'))
  )

  document.body.appendChild(table)
}
