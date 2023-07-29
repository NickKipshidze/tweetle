const API = "http://127.0.0.1:8000";

async function getIdentity() {
    const access_token = localStorage.getItem("access_token");
    if (!access_token) {
        throw new Error("Not signed in");
    }

    try {
        const response = await fetch(`${API}/whoami`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${access_token}`,
            },
        });

        if (response.status === 200) {
            const data = await response.json();
            return data;
        } else {
            throw new Error("Failed to access the protected route.");
        }
    } catch (error) {
        console.warn(error);
        throw error;
    }
}

getIdentity().then(response => {
    document.getElementById("username").innerText = `Signed in as ${response.username}`;
}).catch(error => {
    console.warn(error);
    window.location.href = "./index.html";
});

document.getElementById("sign-out").addEventListener("click", (event) => {
    localStorage.removeItem("access_token");
    window.location.reload();
});