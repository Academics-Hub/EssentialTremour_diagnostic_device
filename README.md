# EssentialTremour_diagnostic_device

## DOCUMENTATION
### src/main.jsx
This file contains the main code for the application. It is the entry point for the application.
#### 1. Importing modules
- `React` - This is the main module for the application. It is used to create the user interface for the application.
- `ReactDOM` - This module is used to render the user interface created using the `React` module.
- `App` - This is the main component for the application. It is used to create the user interface for the application.
- `index.css` - This is the stylesheet for the application. It is used to style the user interface for the application.

#### 2. Rendering the user interface
The second step is to render the user interface created using the `App` component. The user interface is rendered using the `ReactDOM.render()` method. The `ReactDOM.render()` method takes two arguments. The first argument is the user interface created using the `App` component. The second argument is the element in the HTML document where the user interface is to be rendered. In this case, the user interface is rendered in the element with the `id` of `root`.

### src/App.jsx
This file contains the code for the main component of the application. It is used to create the user interface for the application.

#### 1. Importing modules
- `React` - This is the main module for the application. It is used to create the user interface for the application.
- `index.css` - This is the stylesheet for the application. It is used to style the user interface for the application.

#### 2. Functions
- `App()` - This function is used to create the user interface for the application.
  - Returns
    - `<Navbar />`
    - `<LeftContent />`
    -  `<RightContent />`
- `Navbar()` - This function is used to create the navigation bar for the application. 
- `LeftContent()` - This function is used to create the left content for the application.
- `RightContent()` - This function is used to create the right content for the application.

### src/index.css
This file contains the code for the stylesheet for the application. It is used to style the user interface for the application.
- Contains the tailwindcss directives for the application.
```css 
@tailwind base;
@tailwind components;
@tailwind utilities;
```
### src/app.py
This file contains the code for the backend of the application. It is used to create the API for the application.

#### 1. Importing modules
- `flask` - This is the main module for the application. It is used to create the API for the application.
- `pandas` - This module is used to read the data from the CSV file.
- `numpy` - This module is used to perform mathematical operations on the data.
- `app.src.arduino` - This module is used to connect to the Arduino device. It is used to read the data from the Arduino device.


