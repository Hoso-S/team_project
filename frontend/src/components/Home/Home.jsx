import { useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Notifications from './Notifications.jsx';
import axios from 'axios';
// import { Button } from '@mui/material';
import { useRecoilState } from "recoil";
import { pathState } from "../../atoms/pathState.js"

axios.defaults.withCredentials = true;
// const axiosApiInstance = axios.create({
//   baseURL: 'http://localhost:8080/api',
//   headers: {
//     'Content-Type': 'application/json',
//   },
// });

// const axiosPostInstance = axios.create({
//   baseURL: 'http://localhost:8080/api',
//   headers: {
//     'Content-Type': 'application/json',
//     'X-CSRF-TOKEN': sessionStorage.getItem('csrftoken'),
//   },
//   credentials: "same-origin"
// });

// const axiosAuthInstance = axios.create({
//   baseURL: 'http://localhost:8080/api',
//   headers: {
//     'Content-Type': 'application/json',
//     'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
//   },
// });

// const axiosLoginInstance = axios.create({
//   baseURL: 'http://localhost:8080/api',
//   headers: {
//     'Content-Type': 'application/x-www-form-urlencoded',
//     'X-CSRF-TOKEN': sessionStorage.getItem('csrftoken'),
//   },
//   credentials: "same-origin"
// });

export default function Home() {
  const [, setPath] = useRecoilState(pathState);
  useEffect(() => {
    setPath(() => "ホーム");
  }, []);

  // const onClickLogin = () => {
  //   const body = "grant_type=&username=test1&password=p%40ssword&scope=&client_id=&client_secret=";
  //   axiosLoginInstance.post('/login/access-token', body)
  //     .then((res) => { 
  //       console.log("login", res);
  //       sessionStorage.setItem('token', res.data.access_token);
  //       // document.cookie = `csrf-token=${res.data.csrf_token}`;
  //     })
  //     .catch(console.error);
  // };
  
  // const onClickTest = () => {
  //   const user = {
  //     email: "test1",
  //     is_active: true,
  //     is_superuser: true,
  //     password: "p@ssword",
  //   };
  //   axiosPostInstance.post('/users', user)
  //     .then((res) => { console.log("createUsers", res); })
  //     .catch(console.error);
  // };

  // const onClickGetClassroom = () => {
  //   axiosAuthInstance.get('/classrooms')
  //     .then((res) => { console.log("classrooms", res); })
  //     .catch(console.error);
  // };

  return (
    <>
      <Grid item xs={12}>
        <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
          <Notifications />
        </Paper>
      </Grid>
    </>
  );
}