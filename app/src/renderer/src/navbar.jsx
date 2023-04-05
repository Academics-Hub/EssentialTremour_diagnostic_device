import React from "react";
import './index.css'

function Navbar() {
    return (
      <div className={`bg-slate-600 rounded-lg min-h-12 h-12 w-full`}> 
          <div className={`flex flex-row justify-start`}>
            <h1 className='ml-2 pt-2 text-3xl font-semibold text-white'>
              Essential Tremour Diagnosis 
            </h1> 
          </div>
        </div>
    )
}

export default Navbar;