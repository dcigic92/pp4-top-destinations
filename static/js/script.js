// Edit comment constants
// Get all elements with the class "btn-edit-comment"
const buttonsCommentEdit = document.getElementsByClassName("btn-edit-comment");

// Get the element with the id "id_body"
const commentText = document.getElementById("id_body");

// Get the element with the id "commentForm"
const commentForm = document.getElementById("commentForm");

// Get the element with the id "submitButton"
const submitCommentButton = document.getElementById("submitButton");


// Delete comment constants
// Create a new Bootstrap Modal instance with the element that has the id "deleteCommentModal"
const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));

// Get all elements with the class "btn-delete-comment"
const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");

// Get the element with the id "deleteCommentConfirm"
const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");


// Delete post constants
// Create a new Bootstrap Modal instance with the element that has the id "deletePostModal"
const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));

// Get all elements with the class "btn-delete-post"
const deletePostButtons = document.getElementsByClassName("btn-delete-post");

// Get the element with the id "deletePostConfirm"
const deletePostConfirm = document.getElementById("deletePostConfirm");


// Edit comment
// Loop through each button in the buttonsCommentEdit array
for (let button of buttonsCommentEdit) {
    // Add a click event listener to each button
    button.addEventListener("click", (e) => {
        // Get the comment ID from the "comment_id" attribute of the clicked button
        let commentId = e.target.getAttribute("comment_id");
        // Get the comment content from the element with the ID "comment{commentId}" and store it in the variable commentContent
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        // Set the value of the commentText input field to the commentContent
        commentText.value = commentContent;
        // Change the text of the submitCommentButton to "Update"
        submitCommentButton.innerText = "Update";
        // Set the action attribute of the commentForm to "edit_comment/{commentId}"
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}


// Delete comment
// Loop through each button in the deleteCommentButtons array
for (let button of deleteCommentButtons) {
    // Add a click event listener to each button
    button.addEventListener("click", (e) => {
        // Get the comment ID from the "comment_id" attribute of the clicked button
        let commentId = e.target.getAttribute("comment_id");
        // Set the href attribute of the deleteCommentConfirm link to "delete_comment/{commentId}"
        deleteCommentConfirm.href = `delete_comment/${commentId}`;
        // Show the deleteCommentModal
        deleteCommentModal.show();
    });
}

// Delete post
// Loop through each button in the deletePostButtons array
for (let button of deletePostButtons) {
    // Add a click event listener to each button
    button.addEventListener("click", (e) => {
        // Get the post ID from the "post_id" attribute of the clicked button
        let postId = e.target.getAttribute("post_id");
        // Set the href attribute of the deletePostConfirm link to "delete_post/{postId}"
        deletePostConfirm.href = `delete_post/${postId}`;
        // Show the deletePostModal
        deletePostModal.show();
    });
}
