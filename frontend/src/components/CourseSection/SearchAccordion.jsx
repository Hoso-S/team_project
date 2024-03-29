import { useState } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import TextField from '@mui/material/TextField';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Button from '@mui/material/Button';
import { Box } from '@mui/material';
// import dayjs from 'dayjs';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

// const rows = [
//     { id: 1, col1: 'Hello', col2: 'World' },
//     { id: 2, col1: 'DataGridPro', col2: 'is Awesome' },
//     { id: 3, col1: 'MUI', col2: 'is Amazing' },
// ];

export default function Home() {
  const onClickSearch = () => {
    console.log('search');
  }

  const [semester, setSemester] = useState('');
  const handleSemesterChange = (event) => {
    setSemester(event.target.value);
  };

  const [year, setYear] = useState(null)
  const handleYearChange = (newValue) => {
    setYear(newValue)
  }

  return (
    <Accordion>
        <AccordionSummary
        expandIcon={<ArrowDropDownIcon />}
        aria-controls="panel1-content"
        id="panel1-header"
        >
        <Typography>検索</Typography>
        </AccordionSummary>
        <AccordionDetails>
        <Box sx={{ display: 'flex' }}>
            <Grid container>
            <Grid item xs={12} sm={12}>
                <FormControl fullWidth>
                <TextField id="course-name" label="コース名" variant="standard" />
                </FormControl>
            </Grid>
            <Grid item xs={12} sm={12} sx={{ mt: 2 }}>
                {/* <TextField id="year" label="年度" variant="standard" /> */}
                <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                    label="年度"
                    value={year}
                    onChange={handleYearChange}
                    views={['year']}
                    slot={{ textField: { variant: 'outlined' } }}
                />
                </LocalizationProvider>
            </Grid>
            <Grid item xs={12} sm={12} sx={{ mt: 2 }}>
                <FormControl sx={{ minWidth: 180 }}>
                <InputLabel id="semester-select-label">セメスター</InputLabel>
                <Select
                    labelId="semester-select-label"
                    value={semester}
                    onChange={(handleSemesterChange)}
                >
                    <MenuItem value={1}>Spring</MenuItem>
                    <MenuItem value={2}>Summer</MenuItem>
                    <MenuItem value={3}>Fall</MenuItem>
                    <MenuItem value={4}>Winter</MenuItem>
                </Select>
                </FormControl>
            </Grid>
            <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
                <Button
                variant="contained"
                onClick={onClickSearch}
                sx={{ mt: 3, ml: 1 }}
                >
                検索
                </Button>
            </Box>
            </Grid>
        </Box>
        </AccordionDetails>
    </Accordion>
  );
}