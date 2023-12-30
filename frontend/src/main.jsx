import ReactDOM from 'react-dom/client'
import {
  RouterProvider,
} from "react-router-dom";
import Router from './routes'

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={Router} />
)
