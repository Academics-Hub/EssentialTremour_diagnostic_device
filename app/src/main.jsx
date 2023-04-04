/**
 * @fileoverview Main entry point for the application.
 * @author Jonathan Faller
 * @version 1.0.1
 * @module main
 * @requires react
 * @requires react-dom
 * @requires App
 * @requires index.css
 */

import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

/**
 * Renders the application.
 */
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
