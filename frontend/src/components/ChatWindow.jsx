function ChatWindow({ message }) {
    return (
        <main className="chat-window">
            <p>
                {message || "Start chatting with RoboMentor AI..."}
            </p>
        </main>
    );
}

export default ChatWindow;
