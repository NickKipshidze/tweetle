const API = "http://127.0.0.1:8000";

document.getElementById("signup-form").addEventListener("submit", (event) => {
    event.preventDefault();

    fetch(`${API}/signup`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        }),
    }).then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            throw new Error("Invalid credentials");
        }
    }).then(data => {
        window.location.href = "./login.html";
    }).catch(error => {
        console.warn(error);
    });
});