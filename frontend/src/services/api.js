const BASE_URL = "http://127.0.0.1:8000";

export async function createConversation() {
    const response = await fetch(
        `${BASE_URL}/conversation`,
        {
            method: "POST",
        }
    );

    const data = await response.json();

    return data;
}

export async function sendMessage(conversationId, question, level = "Beginner") {
    const response = await fetch(
        `${BASE_URL}/chat`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                conversation_id: conversationId,
                question: question,
                level: level,
            }),
        }
    );

    const data = await response.text();

    return data;
}
