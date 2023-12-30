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
    

// JavaScript code to give auto suggest functionality to the input box, based on user input.    
function updateRecyclerSuggestions() {
    var input = document.getElementById('recyclerinputbox').value;
    var datalist = document.getElementById('recycleAutoSuggest');
    datalist.innerHTML = '';
    var suggestPath = itemSuggestsUrl;

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
document.getElementById('recyclerinputbox').addEventListener('keyup', updateRecyclerSuggestions);
}
