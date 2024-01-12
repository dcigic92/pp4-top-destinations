
document.addEventListener("DOMContentLoaded", function () {
    document
      .getElementById("search-form")
      .addEventListener("submit", function (e) {
        e.preventDefault();
        var searchTerm = document.getElementById("search-input").value;
        fetch(searchPostsUrl + "?search_term=" + searchTerm)
          .then((response) => response.text())
          .then((data) => {
            document.getElementById("content-area").innerHTML = data;
          })
          .catch((error) => console.error("Error:", error));
        window.location.href = searchPostsUrl + "?search_term=" + searchTerm;
      });
  });
  