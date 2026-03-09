async function sendMessage() {
    const inputField = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");
    const empId = document.getElementById("empId").value;
    const messageText = inputField.value;

    if (messageText.trim() === "") return; 

    // Display User Message
    chatBox.innerHTML += `<div class="message user">${messageText}</div>`;
    inputField.value = ""; 
    chatBox.innerHTML += `<div class="message bot" id="loading">Thinking...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight; 

    try {
        // Fetch API - Talking to your Python Backend
        const response = await fetch("https://opensoft-bot.onrender.com/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ 
                employee_id: empId, 
                message: messageText 
            })
        });

        const data = await response.json();
        
        document.getElementById("loading").remove();

        if (response.ok) {
            chatBox.innerHTML += `<div class="message bot">${data.bot_response}</div>`;
        } else {
            chatBox.innerHTML += `<div class="message bot" style="color:red;">Error: ${data.detail}</div>`;
        }
    } catch (error) {
        document.getElementById("loading").remove();
        chatBox.innerHTML += `<div class="message bot" style="color:red;">Server is offline! Ensure your Python backend is running.</div>`;
    }
    
    chatBox.scrollTop = chatBox.scrollHeight; 
}

// Bonus usability: Press "Enter" to send
document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});