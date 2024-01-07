/* Set the width of the sidebar to 250px (show it) */
function openNav() {
    document.getElementById("sidePanel").style.width = "250px";
    document.getElementById("sidePanel").style.height = "60%";
  }
  
  /* Set the width of the sidebar to 0 (hide it) */
  function closeNav() {
    document.getElementById("sidePanel").style.width = "0";
    document.getElementById("sidePanel").style.height = "0";
  }
  
// JavaScript code to save the selected options in the dropdown menus, so that they are still selected when the page is refreshed.
window.onload = function() {
    // Check if there are saved selections
    var raidType = localStorage.getItem('switch');
    var itemType = localStorage.getItem('itemType');

    if (document.getElementById('switch').checked === false) {
        document.getElementById('idSubmit').innerHTML = 'BOOM!';
        raidTool.disabled = this.checked;
    } else if (document.getElementById('switch').checked === true) {
        document.getElementById('idSubmit').innerHTML = 'CHOP!';
        raidTool.disabled = this.checked;
        raidTool.value = 'None';
    }

    // If there are, set the selected options
    if (raidType) {
        document.getElementById('raidType').value = raidType;
    }
    if (itemType) {
        document.getElementById('itemType').value = itemType;
    }

    // When an option is selected, save the selection
    document.getElementById('switch').onchange = function() {
        localStorage.setItem('switch', this.value);
    }
    document.getElementById('itemType').onchange = function() {
        localStorage.setItem('itemType', this.value);
    }


    document.getElementById('switch').onchange = function() {
        var submitButton = document.getElementById('idSubmit');
        var submitBtn = document.querySelector('.submitBtn');
        var raidType = this;
        var raidTool = document.getElementById('raidTool');
        raidTool.disabled = this.checked;

        if (raidType.checked === false) {
            submitButton.innerHTML = 'BOOM!';
        } else if (raidType.checked === true) {
            submitButton.innerHTML = 'CHOP!';
            raidTool.value = 'None';
        }
    
    }
}

// JavaScript code to give auto suggest functionality to the input box, based on user input.    
function updateSuggestions() {
    var input = document.getElementById('inputbox').value;
    var datalist = document.getElementById('autoSuggest');
    datalist.innerHTML = '';

    // Gets the value of the item type dropdown menu, and sets the path to the JSON file containing the items.
    var itemType = document.getElementById('itemType').value;
    var suggestPath;
    if (itemType === 'deployable') {
        var suggestPath = deployableSuggestsUrl;
    } else if (itemType === 'vehicle') {
        var suggestPath = vehicleSuggestsUrl;
    } else if (itemType === 'building') {
        var suggestPath = buildingSuggestsUrl;
    }

    // Fetches the JSON file containing all the items, and filters the list based on user input.
    fetch(suggestPath)
        .then(response => response.json())
        .then(suggestions => {
            var filteredSuggestions = suggestions.filter(function(suggestion) {
                return suggestion.toLowerCase().includes(input.toLowerCase());
            });

            filteredSuggestions.forEach(function(suggestion) {
                var option = document.createElement('option');
                option.value = suggestion;
                datalist.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));
};
// Calls the updateSuggestions function when the user either types in the box or changes the item type.
document.getElementById('inputbox').addEventListener('keyup', updateSuggestions);
document.getElementById('itemType').addEventListener('change', updateSuggestions);
