import React from 'react'
import './index.css'

function SidePane () {
    const [showSidePane, setShowSidePane] = React.useState(false)
    return (
        <>
            <div className={`relative bg-slate-400 w-fill h-fill rounded-lg ${PaneVisiblity(showSidePane)}`}>
                <div className='flex bg-slate-600 w-full h-7 rounded-t-lg absolute'>
                    <h1 className='truncate basis-5/6 text-white text-left ml-1 '>
                        Imported Files
                    </h1>
                    <button className={`text-right w-6 h-6 hover:rounded-full hover:animate-pulse ${RevealPaneButtonState(showSidePane)}`} onClick={() => (setShowSidePane(!showSidePane)) }>
                        <h1 className="text-white font-semibold ">
                            &lt;&lt;
                        </h1>
                    </button>
                </div>
                <div className='truncate static pt-7 mx-2'>
                    <ul>1</ul>
                    <ul>2</ul>
                    <ul>3</ul>
                </div>
            </div>
            <div className={`w-fit h-fit rounded-lg ease-in-out duration-300`}>
                <button className={`w-5 h-5 hover:rounded-full hover:animate-pulse ${RevealPaneButtonState(!showSidePane)}`} onClick={() => (setShowSidePane(!showSidePane)) }>
                    <h1 className="text-white font-semibold">
                        &gt;&gt;
                    </h1>
                </button>
            </div>   
        </>  
    )
    //accessor for showSidePane
    function RevealPaneButtonState (state) {
        if (state) {
            return "block"
        } else {
            return "hidden"
        }
    }
    //identity a function that returns a string based on the state of showSidePane
    
    function PaneVisiblity (state) {
        if (state) {
            return "flex basis-1/4"
        } else {
            return "hidden"
        }
    }
}

export default SidePane