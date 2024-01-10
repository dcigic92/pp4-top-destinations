const buttonsCommentEdit = document.getElementsByClassName("btn-edit-comment");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitCommentButton = document.getElementById("submitButton");

const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
const deleteCommentButtons = document.getElementsByClassName("btn-delete-comment");
const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");

const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const deletePostButtons = document.getElementsByClassName("btn-delete-post");
const deletePostConfirm = document.getElementById("deletePostConfirm");

for (let button of buttonsCommentEdit) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitCommentButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

for (let button of deleteCommentButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteCommentConfirm.href = `delete_comment/${commentId}`;
      deleteCommentModal.show();
    });
  }

  for (let button of deletePostButtons) {
    button.addEventListener("click", (e) => {
      let postId = e.target.getAttribute("post_id");
      deletePostConfirm.href = `delete_post/${postId}`;
      deletePostModal.show();
    });
  }
