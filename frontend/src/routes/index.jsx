import {
    Routes, Route, Navigate
} from "react-router-dom";
import { useRecoilState } from "recoil";
import { loginState } from "../atoms/loginState"
import Login from '../components/Login/Login.jsx'
import Home from '../components/Home/Home.jsx'
import CourseSection from '../components/CourseSection/CourseSection.jsx'

function Router() {
    const [isLogin, ] = useRecoilState(loginState)
    return (
        <Routes> {/*Routesで囲む*/}
            <Route path="/" element={ isLogin ? <Home /> : <Navigate replace to="/login" />} /> {/*RouteにHomeを設定する*/}
            <Route path="/login" element={<Login />} />
            <Route path="/course-section" element={ <CourseSection /> } />
        </Routes>
    )
}

export default Router