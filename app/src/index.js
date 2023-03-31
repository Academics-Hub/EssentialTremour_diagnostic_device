import React from 'react';
import ReactDOM from 'react-dom/client';

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

function ReactLogo () {
    return (
            <img src={require("./react-logo.png")} alt="React logo" width="80px" height="80px"/>
    )
}

function Header () {
    return (
        <header>
            <nav className='Header'>
                <font size="8"><h1> <ReactLogo /> REACT INFO SITE </h1></font> 
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
        <div>
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
