const submitForm = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    const message = document.getElementById("usernameWarning");
    fetch('/sign-up/submit', {
        method: 'PUT',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.exists) {
            message.innerHTML = "Username already taken!";
            message.style.color = "red";
        }
        else {
            message.innerHTML = "";
            window.location.href = "/";
        }
    })
    .catch(error => console.error("Error:", error));
};

const form = document.getElementById("form");
form.addEventListener("submit", submitForm);
