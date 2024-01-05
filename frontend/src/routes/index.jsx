import {
    createBrowserRouter,
} from "react-router-dom";
import Login from '../components/Login.jsx'
import Home from '../components/Home'

const Router = createBrowserRouter([
    {
        path: "/",
        element: <Login />,
    },
    {
        path: "/home",
        element: <Home />,
    },
]);

export default Router