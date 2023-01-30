const likePost = async (post_id) => {
    try {
        const response = await fetch(`/posts/${post_id}/like`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            alert('Post liked successfully!');
            window.location.href = '/posts';
        } else {
            alert('There was an error liking the post, please try again.');
        }
    } catch (error) {
        console.error(error);
        alert('There was an error liking the post, please try again.');
    }
};

const dislikePost = async (post_id) => {
    try {
        const response = await fetch(`/posts/${post_id}/dislike`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            alert('Post disliked successfully!');
            window.location.href = '/posts';
        } else {
            alert('There was an error disliking the post, please try again.');
        }
    } catch (error) {
        console.error(error);
        alert('There was an error disliking the post, please try again.');
    }
};

const likeButtons = document.querySelectorAll('.like');
const dislikeButtons = document.querySelectorAll('.dislike');

likeButtons.forEach(likeButton => {
    likeButton.addEventListener('click', async event => {
        const post_id = event.target.getAttribute('post-id');
        likePost(post_id);
    });
});

dislikeButtons.forEach(dislikeButton => {
    dislikeButton.addEventListener('click', async event => {
        const post_id = event.target.getAttribute('post-id');
        dislikePost(post_id);
    });
});