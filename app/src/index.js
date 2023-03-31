import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function ContentList () {
    return (
        <nav className="contentList">
            <div>
                <font size="6"><h2> First content list </h2></font>
                    <font size="5">
                        <ul>
                            <li><a href="https://github.com/JonoLF/LearningReact">Project Git</a></li>
                            <li><a href="https://scrimba.com/learn/learnreact">React tutorial scrimba</a></li>
                            <li>"some random text, lol"</li>
                        </ul>
                    </font>
            </div>
        </nav>
    )
}

function Header () {
    return (
        <header>
            <nav class='Header'>
                <font size="8"><h1> Essential Tremour Diagnostic </h1></font> 
            </nav>
        </header>
    )
}

function Footer () {
    return (
        <footer> 
            <nav className='Footer'>
                <small>© 2023 Faller development. All rights reserved.</small>
            </nav>
        </footer>
    )
}

function Page () {
    return (
        <div class='background'>
            <Header />   
            <ContentList />
            <Footer />
        </div>
    )
}
const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(
    <div>
        <Page />
    </div>
)
