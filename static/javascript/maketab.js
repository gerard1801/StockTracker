function createTable (tableData, headers) {
  const table = document.createElement('table');
  var thead = document.createElement('thead');
  var row = document.createElement('tr');
  table.appendChild(thead);
  thead.appendChild(row);
  for (var i=0; i<headers.length; i++) {
      var celhead = document.createElement('th');
      celhead.innerHTML = headers[i]
      row.appendChild(celhead)
  }
  table.appendChild(
    tableData.reduce((tbody, rowData) => {
      tbody.appendChild(
        rowData.reduce((tr, cellData) => {
          tr.appendChild(
            document.createElement('td').appendChild(document.createTextNode(cellData)))
          return tr },
            document.createElement('tr')))
      return tbody },
        document.createElement('tbody')))
  document.body.appendChild(table)
}
