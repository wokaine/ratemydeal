const submitForm = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    try {
        const response = await fetch('/submit', {
            method: 'PUT',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            alert('Post submitted successfully!');
            window.location.href = '/';
        } else {
            alert('There was an error submitting the post, please try again.');
        }
    } catch (error) {
        console.error(error);
        alert('There was an error submitting the post, please try again.');
    }
};

const form = document.getElementById("form");
form.addEventListener("submit", submitForm);
