/**
 * @file App.jsx
 * @description App component
 * @author Jonathan Faller
 * @version 1.0.1
 */

import { Fragment, useState } from 'react'
import './index.css'
import SidePane from './sidepane'
import MainContent from './mainContent'
import Navbar from './navbar'

/**
 * 
 * @returns {JSX.Element} App component
 */
function App() {
  return (
    <div className="bg-slate-800 overflow-hidden min-h-screen p-3 space-y-3">
      <Navbar />
      <div className={`flex flex-row flex-nonwrap gap-x-2`}>
        <SidePane />
        <MainContent />
      </div>
    </div>
  )
}

export default App
