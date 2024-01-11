import {
    createBrowserRouter,
} from "react-router-dom";
import Login from '../components/Login/Login.jsx'
import Home from '../components/Home/Home.jsx'
import CourseSection from '../components/CourseSection/CourseSection.jsx'

const Router = createBrowserRouter([
    {
        path: "/",
        element: <Login />,
    },
    {
        path: "/home",
        element: <Home />,
    },
    {
        path: "/course-section",
        element: <CourseSection />,
    },
]);

export default Router