import * as React from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Notifications from './Notifications.jsx';
import axios from 'axios';
import { Button } from '@mui/material';

const axiosInstance = axios.create({
  baseURL: '/api/',
  headers: {
    'Content-Type': 'application/json',
  },
});
console.log("@@@@@@@@@@@@@@@@");


export default function Home() {
  const user = {
    email: "test1",
    is_active: true,
    is_superuser: true,
    password: "p@ssword",
  };
  const onClickTest = () => {

    axiosInstance.post('users', user)
      .then((res) => { console.log("createUsers", res); })
      .catch(console.error);
  };

  React.useEffect(() => {
    axiosInstance.get('users/?skip=0&limit=100')
      .then((res) => { console.log("getUsers", res); })
      .catch(console.error);

      
    // fetch("api/users",{
    //   body: JSON.stringify(user),
    //   method: 'POST',
    //   headers: {
    //     Accept: 'application/json',
    //     'Content-Type': 'application/json',
    //   },
    //   credentials: 'same-origin',
    //   mode: 'same-origin',
    //   // redirect: 'follow',
    // }).then(res=>res.json()).then(console.log).catch(console.error);
  }, []);

  return (
    <>
      <Grid item xs={12}>
        <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
          <Notifications />
        </Paper>
      </Grid>
      <Grid container spacing={3}>
        {/* 最近のお知らせ */}
        <Grid item xs={12}>
          <Button variant="contained" onClick={onClickTest}>Test</Button>
        </Grid>
      </Grid>
    </>
  );
}