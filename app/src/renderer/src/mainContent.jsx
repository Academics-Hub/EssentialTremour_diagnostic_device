import React from "react";
import './index.css'

function MainContent() {
    return (
      <div className={`flex w-full bg-slate-400 rounded-lg min-h-content h-[90vh] transition-all ease-linear duration-1000`}>
        <div className={`grow bg-slate-600 rounded-t-lg h-7`}>
          <h1 className='text-left ml-1 text-white'>
            Analysis of selected import
          </h1>
        </div>
      </div>
    )
}


export default MainContent