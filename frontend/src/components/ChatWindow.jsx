import { useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";

function ChatWindow({ messages, loading }) {
    const messagesEndRef = useRef(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages, loading]);

    return (
        <div className="chat-window">
            {messages.length === 0 && !loading ? (
                <div className="welcome-state">
                    <div className="welcome-robot">🤖</div>
                    <h2>Welcome to RoboMentor AI</h2>
                    <p>
                        I'm your personal robotics tutor. Ask me anything about
                        Arduino, Raspberry Pi, sensors, electronics, or programming!
                    </p>
                    <div className="welcome-topics">
                        <span className="topic-chip">🔌 Arduino</span>
                        <span className="topic-chip">🍓 Raspberry Pi</span>
                        <span className="topic-chip">📡 Sensors</span>
                        <span className="topic-chip">🤖 Robotics</span>
                        <span className="topic-chip">💡 Electronics</span>
                    </div>
                </div>
            ) : (
                <>
                    {messages.length > 0 && (
                        <div className="date-divider">
                            <span className="date-pill">Today</span>
                        </div>
                    )}

                    {messages.map((message, index) => (
                        <MessageBubble key={index} message={message} />
                    ))}
                </>
            )}

            {loading && (
                <div className="thinking-row">
                    <div className="thinking-avatar">🤖</div>
                    <div className="thinking-bubble">
                        <div className="thinking-dots">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                        <span className="thinking-text">RoboMentor is thinking...</span>
                    </div>
                </div>
            )}

            <div ref={messagesEndRef}></div>
        </div>
    );
}

export default ChatWindow;
