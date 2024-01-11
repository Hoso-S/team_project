// import { useState } from 'react'
// import './App.css'
import Login from './components/Login/Login'
import Home from './components/Home/Home'
import { useRecoilState } from "recoil";
import { loginState } from "./atoms/loginState"

function App() {
  // ログイン状態
  const [isLogin, ] = useRecoilState(loginState)

  return (
    <>
        {!isLogin ? <Login /> : <Home />} 
    </>
  )
}

export default App
