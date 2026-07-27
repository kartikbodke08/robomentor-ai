import "./App.css";

import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

import { useState } from "react";

function App() {
    const [message, setMessage] = useState("");

    return (
        <div className="app">
            <Header title="🤖 RoboMentor AI" />

            <div className="main-content">
                <Sidebar heading="Conversations" />

                <div className="chat-section">
                    <ChatWindow message={message} />

                    <ChatInput
                        placeholder="Ask RoboMentor anything..."
                        message={message}
                        setMessage={setMessage}
                    />
                </div>
            </div>
        </div>
    );
}

export default App;
