function ChatInput({
    placeholder,
    message,
    setMessage,
}) {
    return (
        <div className="chat-input">
            <input
                type="text"
                placeholder={placeholder}
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />

            <button>
                Send
            </button>
        </div>
    );
}

export default ChatInput;
