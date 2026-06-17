async function login() {
    const formData = new FormData();

    formData.append("username", document.getElementById("username").value);
    formData.append("password", document.getElementById("password").value);

    const response = await fetch("/auth/login", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "/chat-page";
    } else {
        alert(data.detail || "Login Failed")
    }
}

async function signup(){
    const formData = new FormData();

    formData.append("username", document.getElementById("username").value);
    formData.append("password", document.getElementById("password").value);

    const response = await fetch("/auth/signup", {
        method: "POST",
        body: formData
    })

    const data = await response.json();

    alert(data.message || data.detail);

    if(response.ok) {
        window.location.href = "/";
    }
}