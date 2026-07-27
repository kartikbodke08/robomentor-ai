function Header() {
    return (
        <header className="header">
            <div className="header-brand">
                <div className="logo-icon">
                    <div className="robot-antenna"></div>
                    <div className="robot-face">
                        <div className="robot-eyes">
                            <span className="robot-eye"></span>
                            <span className="robot-eye"></span>
                        </div>
                        <span className="robot-mouth"></span>
                    </div>
                </div>
                <div className="header-text">
                    <h1>RoboMentor AI</h1>
                    <p>Your Personal Robotics Tutor</p>
                </div>
            </div>

            <div className="header-actions">
                <button className="settings-icon" title="Settings">⚙️</button>
                <div className="user-avatar" title="Profile">K</div>
            </div>
        </header>
    );
}

export default Header;
