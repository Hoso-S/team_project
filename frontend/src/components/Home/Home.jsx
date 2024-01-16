import * as React from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Notifications from './Notifications.jsx';
import axios from 'axios';
import { Button } from '@mui/material';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8080/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default function Home() {
  const onClickTest = () => {
    const user = {
      email: "test1",
      is_activate: true,
      is_superuser: true,
      password: "p@ssword",
    };
    axiosInstance.post('/users', user)
      .then((res) => { console.log("createUsers", res); })
      .catch(console.error);
  };

  React.useEffect(() => {
    axiosInstance.get('/users/?skip=0&limit=100')
      .then((res) => { console.log("getUsers", res); })
      .catch(console.error);
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