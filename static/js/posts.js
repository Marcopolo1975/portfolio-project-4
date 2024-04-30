const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_post");
const commentForm = document.getElementById("postForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated posts's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `postText` input/textarea with the post's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_post/{postId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("post_id");
        let postContent = document.getElementById(`post${postId}`).postForm;
        postText.value = postContent;
        submitButton.postForm = "Update";
        postForm.setAttribute("action", `edit_post/${postId}`);
    });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("post_id");
        deleteConfirm.href = `delete_post/${postId}`;
        deleteModal.show();
    });
}