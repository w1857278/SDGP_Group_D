//Functionality for search bar
function SearchFunction() {
    // Get the input value and convert it to lowercase
    var input = document.getElementById("SearchInput");
    var filter = input.value.toLowerCase();

    // Get the table and table rows
    var table = document.getElementById("UserTable");
    var rows = table.getElementsByTagName("tr");

    // Loop through all table rows, hide those that don't match the search query
    for (var i = 0; i < rows.length; i++) {
      var UserName = rows[i].getElementsByTagName("td")[1];
      if (UserName) {
            var UserNameValue = UserName.textContent || UserName.innerText;
            if (UserNameValue.toLowerCase().indexOf(filter) > -1) {
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

//Filter option functionality
function applyFilters() {
    // Get filter options
    var alphabeticalFilter = document.getElementById("AlphabeticalFilter").checked;
    var staffFilter = document.getElementById("staffFilter").checked;
    // Get table and table rows
    var table = document.getElementById("UserTable");
    var rows = table.getElementsByTagName("tr");
    // Array to store row data
    var rowArray = [];
    // Loop through table rows excluding header row
    for (var i = 1; i < rows.length; i++) {
        // Store each row element with user name and their staff status
        var userName = rows[i].getElementsByTagName("td")[1].textContent.toLowerCase();
        var is_staff = rows[i].getElementsByTagName("td")[5].textContent.toLowerCase();
        rowArray.push({ element: rows[i], name: userName, is_staff: is_staff });
    }
    // Sort alphabetically by user name
    if (alphabeticalFilter) {
        rowArray.sort(function (a, b) {
            return a.name.localeCompare(b.name); 
        });
    }
    //Date Filter
    if (staffFilter) {
        rowArray = rowArray.filter(function(row) {
            return row.is_staff === 'true';
        });
    }
    // Fill table with sorted rows
    for (var x = 0; x < rowArray.length; x++) {
        table.appendChild(rowArray[x].element);
    }
  }	

//Displaying user info for table row clicked on
function displayUserInfo(userId) {
    var userInfoContainer = document.getElementById('InfoBox');
    // user Information from table row
    var selectedRow = document.getElementById('row-' + userId);
    var username = selectedRow.cells[1].textContent;
    var userFname = selectedRow.cells[2].textContent;
    var userLname = selectedRow.cells[3].textContent;
    var date_joined = selectedRow.cells[4].textContent;
    var is_staff = selectedRow.cells[5].textContent;
    var userEmail = selectedRow.cells[7].textContent.trim();
    var last_login = selectedRow.cells[8].textContent;
    // Update infoBox with user information
    userInfoContainer.innerHTML = `
    <div id="user-info-container">
        <p>
            <br>
            <br>
            <span class="user-info-item"> Username:</span> ${username}<br><br>
            <span class="user-info-item"> Staff Member:</span> ${is_staff}<br><br>
            <span class="user-info-item"> First Name:</span> ${userFname}<br><br>
            <span class="user-info-item"> Last Name:</span> ${userLname}<br><br>
            <span class="user-info-item"> Email:</span> ${userEmail}<br><br>
            <span class="user-info-item"> Date Joined:</span> ${date_joined}<br><br>
            <span class="user-info-item"> Last login:</span> ${last_login}<br><br>
        </p>
        <br>
    </div> `;
}