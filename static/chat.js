async function sendMessage() {
    const token = localStorage.getItem("token");
    const prompt = document.getElementById("prompt").value;

    const response = await fetch("/chat/chat", {
        method: "POST",
        headers: {
            "content-type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            prompt: prompt
        })
    });

    const data = await response.json();

    if (data.response) {
    document.getElementById("response").innerText = data.response;
    document.getElementById("prompt").value = "";
    } else {
        alert(data.error || data.detail || "something went wrong");
    }
}

async function loadHistory(){
    const token = localStorage.getItem("token");

    const response = await fetch("/chat/history", {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await response.json();

    const historyDiv = document.getElementById("history");
    historyDiv.innerHTML = "";

    data.forEach(chat => {
        const item = document.createElement("div");

        item.innerHTML = `
            <hr>
            <b>You:</b> ${chat.prompt}
            <br>
            <b>AI:</b> ${chat.response}
        `;

        historyDiv.appendChild(item);
    });
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "/";
}