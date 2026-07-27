function MessageBubble({ message }) {
    const isUser = message.role === "user";

    const now = new Date();
    const timeString = now.toLocaleTimeString("en-US", {
        hour: "numeric",
        minute: "2-digit",
        hour12: true,
    });

    return (
        <div className={`message-row ${message.role}`}>
            <div className="message-avatar">
                {isUser ? "K" : "🤖"}
            </div>

            <div className="message-bubble">
                <div className="message-content">
                    {message.content}
                </div>
                <div className="message-meta">
                    <span className="message-time">{timeString}</span>
                    {isUser && <span className="message-check">✓✓</span>}
                </div>
            </div>
        </div>
    );
}

export default MessageBubble;
