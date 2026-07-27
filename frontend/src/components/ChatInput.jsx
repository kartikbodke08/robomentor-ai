function ChatInput({ input, setInput, onSend, loading }) {
    const handleKeyDown = (e) => {
        if (e.key === "Enter" && !e.shiftKey && !loading) {
            e.preventDefault();
            onSend && onSend();
        }
    };

    return (
        <div className="chat-input-area">
            <div className="chat-input-wrapper">
                <div className="chat-input-container">
                    <input
                        type="text"
                        className="chat-input"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={handleKeyDown}
                        placeholder={loading ? "RoboMentor is thinking..." : "Ask RoboMentor anything..."}
                        disabled={loading}
                    />
                    <button className="input-icon-btn" title="Attach file">📎</button>
                    <button className="input-icon-btn" title="Voice input">🎙️</button>
                </div>

                <button
                    className="send-button"
                    onClick={() => !loading && onSend && onSend()}
                    disabled={loading || !input.trim()}
                >
                    ✈️ Send
                </button>
            </div>
            <p className="input-disclaimer">
                RoboMentor AI can make mistakes. Please verify important information.
            </p>
        </div>
    );
}

export default ChatInput;
