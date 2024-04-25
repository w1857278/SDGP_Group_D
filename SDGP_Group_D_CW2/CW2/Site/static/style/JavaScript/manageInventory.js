//Functionality for search bar
function SearchFunction() {
    // Get the input value and convert it to lowercase
    var input = document.getElementById("SearchInput");
    var filter = input.value.toLowerCase();
    // Get the table and table rows
    var table = document.getElementById("InventoryTable");
    var rows = table.getElementsByTagName("tr");
    // Loop through all table rows, hide those that don't match the search query
    for (var i = 0; i < rows.length; i++) {
      var DeviceName = rows[i].getElementsByTagName("td")[1];
      if (DeviceName) {
            var DeviceNameValue = DeviceName.textContent || DeviceName.innerText;
            if (DeviceNameValue.toLowerCase().indexOf(filter) > -1) {
              rows[i].style.display = "";
            } else {
              rows[i].style.display = "none";
            }
      }
    }
}	

//Display filter options
function toggleFilterOptions(event){
  event.preventDefault();
  var FilterOptions = document.getElementById("FilterOptions");
  if(FilterOptions.style.display === "none" || FilterOptions.style.display === ""){
      FilterOptions.style.display = "block";
  } else {
      FilterOptions.style.display = "none";
  }
}

//Equipment Count
function toggleEquipCount(event) {
  event.preventDefault();
  var equipmentCountContainer = document.getElementById('equipmentCountContainer');
  if(equipmentCountContainer.style.display === "none" || equipmentCountContainer.style.display === ""){
      equipmentCountContainer.style.display = "block";
  } else {
      equipmentCountContainer.style.display = "none";
  }
  var table = document.getElementById('InventoryTable');
  var rowCount = table.rows.length;
  var totalQuantity = 0;

  for (var i = 1; i < rowCount; i++) {
      var row = table.rows[i];
      var quantityCell = row.cells[2];
      var quantity = parseInt(quantityCell.textContent.trim(), 10);
      if (!isNaN(quantity)) {
          totalQuantity += quantity;
      }
  }

  // Display the total quantity
  var equipmentCountDiv = document.getElementById('eqCountText');
  equipmentCountDiv.textContent = 'Number of Devices: ' + totalQuantity;
  
}

//Filter option functionality
function applyFilters() {
  // Get filter options
  var alphabeticalFilter = document.getElementById("AlphabeticalFilter").checked;
  var quantityFilter = document.getElementById("QuantityFilter").checked;
  // Get table and table rows
  var table = document.getElementById("InventoryTable");
  var rows = table.getElementsByTagName("tr");
  // Array to store row data
  var rowArray = [];
  // Loop through table rows excluding header row
  for (var i = 1; i < rows.length; i++) {
      // Store each row element with device name and quantity
      var deviceName = rows[i].getElementsByTagName("td")[1].textContent.toLowerCase();
      var deviceQuantity = parseInt(rows[i].getElementsByTagName("td")[2].textContent);
      rowArray.push({ element: rows[i], name: deviceName, quantity: deviceQuantity });
  }
  // Sort alphabetically by device name
  if (alphabeticalFilter) {
      rowArray.sort(function (a, b) {
          return a.name.localeCompare(b.name); 
      });
  }
  //Sort by quantity - low to high
  if (quantityFilter) {
      rowArray.sort(function (a, b) {
          return a.quantity - b.quantity; 
      });
  }
  // Fill table with sorted rows
  for (var x = 0; x < rowArray.length; x++) {
      table.appendChild(rowArray[x].element);
  }
}	

//Displaying device info for table row clicked on
function displayDeviceInfo(deviceId) {
  var deviceInfoContainer = document.getElementById('InfoBox');
  // Device Information from table row
  var selectedRow = document.getElementById('row-' + deviceId);
  var deviceName = selectedRow.cells[1].textContent;
  var deviceQuantity = selectedRow.cells[2].textContent;
  var deviceType = selectedRow.cells[3].textContent;
  var deviceAudit = selectedRow.cells[4].textContent;
  var deviceLocation = selectedRow.cells[5].textContent;
  var deviceStatus = selectedRow.cells[7].textContent;
  var deviceComments = selectedRow.cells[8].textContent;
  // Update infoBox with device information
  deviceInfoContainer.innerHTML = `
  <div id="device-info-container">
      <p>
          <br>
          <span class="device-info-item"> Name:</span> ${deviceName}<br>
          <span class="device-info-item"> Quantity:</span> ${deviceQuantity}<br>
          <span class="device-info-item"> Type:</span> ${deviceType}<br>
          <span class="device-info-item"> Audit:</span> ${deviceAudit}<br>
          <span class="device-info-item"> Location:</span> ${deviceLocation}<br>
          <span class="device-info-item"> Status:</span> ${deviceStatus}<br>
          <span class="device-info-item"> Comments:</span> ${deviceComments}<br>
      </p>
      <br>
      <h3>Device Instance(s): </h3>
      <ul id="instance-list"></ul>
  </div> `;
  //URL for getting the device instances
  fetch(`/get_device_instances/${deviceId}`)
  .then(response => response.json())
  .then(data => { 
      const instanceList = document.getElementById('instance-list');
      // Loop through instances (if any) and adds them to the list
      data.forEach(instance => {
          const listItem = document.createElement('li'); //Same layout as the device info above
          listItem.innerHTML = `
              <span class="device-info-item"> Instance Name:</span> ${instance.deviceDetailName}<br>
              <span class="device-info-item"> Serial Number:</span> ${instance.deviceSerial}<br>
              <span class="device-info-item"> RAM:</span> ${instance.deviceRAM}<br>
              <span class="device-info-item"> CPU:</span> ${instance.deviceCPU}<br>
              <span class="device-info-item"> GPU:</span> ${instance.deviceGPU}<br>
              <br>`;
          instanceList.appendChild(listItem);
      });
  })
  .catch(error => console.error('Error fetching device instances:', error));
}