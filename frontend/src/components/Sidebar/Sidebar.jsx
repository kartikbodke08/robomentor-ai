function Sidebar() {
    const conversations = [
        { title: "New Conversation", time: "10:30 AM", active: true },
        { title: "Arduino Basics", time: "Yesterday" },
        { title: "Robot Navigation", time: "Yesterday" },
        { title: "Sensor Calibration", time: "2 days ago" },
        { title: "AI in Robotics", time: "3 days ago" },
        { title: "PID Control", time: "4 days ago" },
    ];

    return (
        <aside className="sidebar">
            <button className="new-chat-btn">+ New Chat</button>

            <p className="sidebar-label">Conversations</p>

            <div className="conversation-list">
                {conversations.map((chat, index) => (
                    <div
                        key={index}
                        className={`conversation-item ${chat.active ? "active" : ""}`}
                    >
                        <div className="conv-icon">💬</div>
                        <div className="conv-info">
                            <div className="conv-title">{chat.title}</div>
                            <div className="conv-time">{chat.time}</div>
                        </div>
                        {chat.active && (
                            <span className="conv-menu">⋮</span>
                        )}
                    </div>
                ))}
            </div>

            <div className="sidebar-bottom">
                <button className="sidebar-settings-btn">
                    <span>⚙️</span>
                    Settings
                </button>
            </div>
        </aside>
    );
}

export default Sidebar;
