import "./App.css";

import Header from "./components/Header";
import Sidebar from "./components/Sidebar/Sidebar";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

import { useState, useEffect } from "react";
import { createConversation, sendMessage } from "./services/api";

function App() {
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [conversationId, setConversationId] = useState(null);

    useEffect(() => {
        async function initializeConversation() {
            try {
                const data = await createConversation();
                setConversationId(data.conversation_id);
                console.log("Conversation Created:", data.conversation_id);
            } catch (err) {
                console.error("Failed to initialize conversation:", err);
            }
        }

        initializeConversation();
    }, []);

    const handleSend = async () => {
        if (!input.trim() || !conversationId || loading) {
            return;
        }

        const inputPrompt = input;
        setInput("");

        setMessages((previous) => [
            ...previous,
            {
                role: "user",
                content: inputPrompt,
            },
        ]);

        setLoading(true);

        try {
            const response = await sendMessage(
                conversationId,
                inputPrompt,
                "Beginner"
            );

            const aiText =
                typeof response === "string"
                    ? response
                    : response?.answer || String(response);

            setMessages((previous) => [
                ...previous,
                {
                    role: "assistant",
                    content: aiText,
                },
            ]);
        } catch (err) {
            console.error("Failed to send message:", err);
            setMessages((previous) => [
                ...previous,
                {
                    role: "assistant",
                    content:
                        "Sorry, something went wrong while connecting to RoboMentor. Please try again.",
                },
            ]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="app">
            <Header />

            <div className="main-content">
                <Sidebar />

                <div className="chat-section">
                    <ChatWindow messages={messages} loading={loading} />

                    <ChatInput
                        input={input}
                        setInput={setInput}
                        onSend={handleSend}
                        loading={loading}
                    />
                </div>
            </div>
        </div>
    );
}

export default App;
