const submitComment = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    var pathArray = window.location.pathname.split('/');
    const post_id = pathArray[3];
    console.log(post_id);
    try {
        const response = await fetch(`/posts/view/${post_id}/submit_comment`, {
            method: 'PUT',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            console.log('Comment submitted successfully!');
            window.location.href = `/posts/view/${post_id}`;
        } else {
            console.log('There was an error submitting the comment, please try again.');
        }
    } catch (error) {
        console.error(error);
        console.log('There was an error submitting the comment, please try again.');
    }
};

const form = document.getElementById("form");
form.addEventListener("submit", async event =>{
    submitComment(event)
});