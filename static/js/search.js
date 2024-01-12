// Wait for the DOM content to be loaded before executing the code inside the function
document.addEventListener("DOMContentLoaded", function () {
  // Add a submit event listener to the element with the id "search-form"
  document
    .getElementById("search-form")
    .addEventListener("submit", function (e) {
      // Prevent the default form submission behavior
      e.preventDefault();
      // Get the value of the input field with the id "search-input" and store it in the variable searchTerm
      var searchTerm = document.getElementById("search-input").value;
      // Fetch the searchPostsUrl with the search term as a query parameter
      fetch(searchPostsUrl + "?search_term=" + searchTerm)
        // Convert the response to text
        .then((response) => response.text())
        // Process the data returned from the fetch request
        .then((data) => {
          // Set the innerHTML of the element with the id "content-area" to the fetched data
          document.getElementById("content-area").innerHTML = data;
        })
        // Handle any errors that occur during the fetch request
        .catch((error) => console.error("Error:", error));
      // Redirect the user to the searchPostsUrl with the search term as a query parameter
      window.location.href = searchPostsUrl + "?search_term=" + searchTerm;
    });
});