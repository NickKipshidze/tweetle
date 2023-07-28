async function signIn(event) {
    event.preventDefault();
    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/token", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(
                {
                    username: username,
                    password: password
                }
            ),
        });

        if (response.status == 200) {
            const { access_token } = await response.json();
            localStorage.setItem("access_token", access_token);
            alert("Sign-in successful");
        }
    } catch (error) {
        console.warn(error);
        alert("Sign-in failed. Please check your credentials.");
    }
}

async function getProtectedRoute() {
    const access_token = localStorage.getItem("access_token");
    if (!access_token) {
        alert("You need to sign in first.");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/protected_route", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${access_token}`,
            },
        });
        const data = await response.json();
        alert(data.message);
    } catch (error) {
        console.error(error);
        alert("Failed to access the protected route.");
    }
}

const signinForm = document.getElementById("signinForm");
signinForm.addEventListener("submit", signIn);

document.getElementById("test-login").addEventListener("click", (event) => {
    getProtectedRoute();
});

document.getElementById("sign-out").addEventListener("click", (event) => {
    localStorage.removeItem("access_token");
});