import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Notifications from './Notifications.jsx';
export default function Home() {
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