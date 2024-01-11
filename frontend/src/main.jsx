import ReactDOM from 'react-dom/client'
import {
  RouterProvider,
} from "react-router-dom";
import Router from './routes'
import { RecoilRoot } from "recoil";

ReactDOM.createRoot(document.getElementById('root')).render(
  <RecoilRoot>
    <RouterProvider router={Router} />
  </RecoilRoot>
)
