function Sidebar({ heading }) {
    return (
        <aside className="sidebar">
            <h2>{heading}</h2>

            <button>+ New Chat</button>

            <ul>
                <li>Conversation 1</li>
                <li>Conversation 2</li>
                <li>Conversation 3</li>
            </ul>
        </aside>
    );
}

export default Sidebar;
