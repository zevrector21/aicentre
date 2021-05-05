// $(document).bind("contextmenu",function(e) {
//  	e.preventDefault();
// });
// document.onkeydown = function (e) {
//     if (event.keyCode == 123) {
//         return false;
//     }
//     if (e.ctrlKey && e.shiftKey && (e.keyCode == 'I'.charCodeAt(0) || e.keyCode == 'i'.charCodeAt(0))) {
//         return false;
//     }
//     if (e.ctrlKey && e.shiftKey && (e.keyCode == 'C'.charCodeAt(0) || e.keyCode == 'c'.charCodeAt(0))) {
//         return false;
//     }
//     if (e.ctrlKey && e.shiftKey && (e.keyCode == 'J'.charCodeAt(0) || e.keyCode == 'j'.charCodeAt(0))) {
//         return false;
//     }
//     if (e.ctrlKey && (e.keyCode == 'U'.charCodeAt(0) || e.keyCode == 'u'.charCodeAt(0))) {
//         return false;
//     }
//     if (e.ctrlKey && (e.keyCode == 'S'.charCodeAt(0) || e.keyCode == 's'.charCodeAt(0))) {
//         return false;
//     }
// }

function downloadCSV(csv, filename) {
  var csvFile;
  var downloadLink;

  // CSV file
  csvFile = new Blob([csv], {type: "text/csv"});

  // Download link
  downloadLink = document.createElement("a");

  // File name
  downloadLink.download = filename;

  // Create a link to the file
  downloadLink.href = window.URL.createObjectURL(csvFile);

  // Hide download link
  downloadLink.style.display = "none";

  // Add the link to DOM
  document.body.appendChild(downloadLink);

  // Click download link
  downloadLink.click();
}

function exportTableToCSV(filename) {
  var csv = [];
  var rows = document.querySelectorAll("table tr");
  for (var i = 0; i < rows.length; i++) {
      var row = [], cols = rows[i].querySelectorAll("td, th");
      
      for (var j = 0; j < cols.length; j++) 
          row.push(cols[j].innerText);
      
      csv.push(row.join(","));        
  }
  // Download CSV file
  downloadCSV(csv.join("\n"), filename);
}