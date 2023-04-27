import React, { Component } from 'react'
import './index.css'
import * as fs from 'node:fs/promises'

function SidePane () {
    const [showSidePane, setShowSidePane] = React.useState(false)
    return (
        <>
            <div className={`relative bg-slate-400 w-fill h-fill rounded-lg ${PaneVisiblity(showSidePane)}`}>
                <div className='flex bg-slate-600 w-full h-7 rounded-t-lg absolute'>
                    <h1 className='truncate basis-5/6 text-white text-left ml-1 '>
                        Imported Files
                    </h1>
                    <button className={`absolute right-0 mr-1 text-right w-6 h-6 hover:rounded-full hover:animate-pulse ${RevealPaneButtonState(showSidePane)}`} onClick={() => (setShowSidePane(!showSidePane)) }>
                        <h1 className="text-white font-semibold ">
                            &lt;&lt;
                        </h1>
                    </button>
                </div>
                <div className='truncate static pt-7 mx-2'>
                    <Folder files='./'/>
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

class Folder extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
    };
  }

  componentDidMount() {
    const folderPath = './';
    fs.readdir(folderPath, (err, files) => {
      if (err) {
        console.error(err);
        return;
      }
      this.setState({ files });
    });
  }

  render() {
    const { files } = this.state;
    return (
      <div>
        <h1>Folder Contents</h1>
        <ul>
          {files.map((file) => (
            <li key={file}>{file}</li>
          ))}
        </ul>
      </div>
    );
  }
}


export default SidePane