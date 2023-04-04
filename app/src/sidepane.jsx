import React from 'react'
import './index.css'

function SidePane() {
    const [showSidePane, setShowSidePane] = React.useState(false)
    return (
        <>
            { showSidePane ? 
                (
                    <button className={`w-10 h-10 hover:bg-slate-600 hover:rounded-full ${RevealPaneButtonState(showSidePane)}`} onClick={() => setShowSidePane(!showSidePane)}>
                        <h1 className="text-white">
                            &gt;&gt;
                        </h1>
                    </button>
                )
                :
                (
                    <button className={`w-10 h-10 hover:bg-slate-600 hover:rounded-full ${RevealPaneButtonState(!showSidePane)}`} onClick={() => setShowSidePane(!showSidePane)}>
                        <h1 className="text-white">
                            &lt;&lt;
                        </h1>
                    </button>
                ) 
            }   
            <div className={`bg-slate-400 w-fit h-fit rounded-lg ease-in-out duration-300 ${PaneVisiblity(showSidePane)}`}>
                <ul>1</ul>
                <ul>2</ul>
                <ul>3</ul>
            </div>
        </>  
    )
}

function RevealPaneButtonState (state) {
    if (state) {
        return "block"
    } else {
        return "hidden"
    }
}
function PaneVisiblity (state) {
    if (state) {
        return "hidden"
    } else {
        return "flex basis-1/4"
    }
}

export default SidePane