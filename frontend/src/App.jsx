// import { useState } from 'react'
// import './App.css'
import Router from './routes'
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
// import Login from './components/Login/Login'
// import Home from './components/Home/Home'
import Navigation from './components/Navigation/Navigation'
import { useRecoilState } from "recoil";
import { loginState } from "./atoms/loginState"
import theme from './assets/theme'

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {`Copyright © コラボレイティブ開発特論2023 G4 ${new Date().getFullYear()}.`}
    </Typography>
  );
}

function App() {
  // ログイン状態
  const [isLogin, ] = useRecoilState(loginState)

  return (
    <>
      <ThemeProvider theme={theme}>
        <Box sx={{ display: 'flex' }}>
          <CssBaseline />
          {isLogin && <Navigation />}
          <Box
            component="main"
            sx={{
              backgroundColor: (theme) =>
                theme.palette.mode === 'light'
                  ? theme.palette.grey[100]
                  : theme.palette.grey[900],
              flexGrow: 1,
              height: '100vh',
              overflow: 'auto',
            }}
          >
            <Toolbar />
            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
              <Grid container spacing={3}>
                <Router />
              </Grid>
              <Copyright sx={{ pt: 4 }} />
            </Container>
          </Box>
        </Box>
      </ThemeProvider>
    </>
  )
}

export default App
