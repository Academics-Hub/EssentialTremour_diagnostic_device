/**
 * @file App.jsx
 * @description App component
 * @author Jonathan Faller
 * @version 1.0.1
 */

import { Fragment, useState } from 'react'
import './index.css'
import styles from './style'
import SidePane from './sidepane'

/**
 * 
 * @returns {JSX.Element} App component
 */
function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="bg-slate-800 overflow-hidden min-h-screen p-3 space-y-5">
      <Navbar />
      <div className={`flex flex-row flex-nonwrap gap-x-5 grow`}>
        <LeftContent />
        <RightContent />
      </div>
    </div>
  )
}

/**
 * 
 * @returns {JSX.Element} Navbar component
 */
function Navbar() {
  return (
    <div className={`${styles.paddingX} ${styles.flexCenter} bg-slate-400 rounded-lg min-h-12 h-12 w-full`}> 
        <div className={`${styles.boxWidth} flex flex-row justify-start`}>
          <h1 className='text-xl hover:text-blue-600 '>
            Essential Tremour Diagnosis 
          </h1> 
        </div>
      </div>
  )
}

/**
 * 
 * @returns {JSX.Element} LeftContent component
 */
function LeftContent() {
  return (
    <SidePane />
  )
}

/**
 * 
 * @returns {JSX.Element} RightContent component
 */

function RightContent() {
    return (
      <div className={`bg-slate-400 rounded-lg min-h-content w-full h-[90vh] ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
            yeet
        </div>
      </div>
    )
}


export default App
