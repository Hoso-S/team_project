import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Snackbar from '@mui/material/Snackbar';
import Alert from '@mui/material/Alert';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import {
  useNavigate,
} from "react-router-dom";
import { useRecoilState } from "recoil";
import { loginState } from "../../atoms/loginState"
import axios from 'axios';

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default function Login() {
  const [, setIsLogin] = useRecoilState(loginState)

  const navigate = useNavigate();

  const [openSnackbar, setOpenSnackbar] = React.useState(false);

  const handleSubmit = async (event) => {
    setOpenSnackbar(false);

    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // console.log({
    //   email: data.get('email'),
    //   password: data.get('password'),
    // });

    const axiosLoginInstance = axios.create({
      baseURL: 'http://localhost:8080/api',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      credentials: "same-origin"
    });

    const body = `grant_type=&username=${data.get('email')}&password=${data.get('password')}&scope=&client_id=&client_secret=`;

    try {
      const res = await axiosLoginInstance.post('/login/access-token', body)
      console.log("login", res);
      sessionStorage.setItem('token', res.data.access_token);
      setIsLogin(() => true);
      navigate('/');
    } catch (error) {
      console.log("error on login", error);
      setOpenSnackbar(true)
    }
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Snackbar
            anchorOrigin={{ horizontal: 'center', vertical: 'top'}}
            open={openSnackbar}
            onClose={() => setOpenSnackbar(false)}
          >
            <Alert
              severity="error"
              variant="filled"
              sx={{ width: '100%' }}
            >
            認証情報に誤りがあります
            </Alert>
          </Snackbar>
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Log in
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Log In
            </Button>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}