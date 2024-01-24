import { useEffect, useState } from 'react';
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
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { DataGrid } from '@mui/x-data-grid';
import { Box } from '@mui/material';
import { useRecoilState } from "recoil";
import { pathState } from "../../atoms/pathState"
// import dayjs from 'dayjs';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions } from '@mui/material';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';
import { fetchList } from '../../assets/api.js';

const columns = [
    { field: 'dept_name', headerName: '学部名', headerAlign: 'center' },
    //{ field: 'course_id', headerName: 'コースID', width: 150, headerAlign: 'center' },
    { field: 'title', headerName: '講義名', headerAlign: 'center' },
    { field: 'name', headerName: '教員名', headerAlign: 'center' },
    { field: 'sec_id', headerName: 'セクションID', headerAlign: 'center' },
    { field: 'semester', headerName: 'セメスター', headerAlign: 'center' },
    { field: 'year', headerName: '年度', headerAlign: 'center' },
    { field: 'building', headerName: '建物', headerAlign: 'center' },
    { field: 'room_number', headerName: '部屋番号', headerAlign: 'center' },
    // { field: 'time_slot_id', headerName: 'タイムスロット', headerAlign: 'center' },
];

export default function CourseSection() {
  const [, setPath] = useRecoilState(pathState);
  useEffect(() => {
    setPath(() => "科目");
    fetchData();
  }, []);

  const [rows, setRows] = useState([]);

  const fetchData = async () => {
    const courses = await fetchList('courses');
    const sections = await fetchList('sections');
    const instructors = await fetchList('instructors');
    const courseSections = sections.map((section) => {
      const course = courses.find((course) => course.course_id === section.course_id);
      return {
        ...course,
        ...section,
      };
    });
    const courseSectionInstructor = courseSections.map((courseSection) => {
      const instructor = instructors.find((instructor) => instructor.instructor_id === courseSection.instructor_id);
      return {
        ...courseSection,
        ...instructor,
      };
    });
    setRows(courseSectionInstructor);
  }

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

  const [openDialog, setOpenDialog] = useState(false);
  const [selectedRow, setSelectedRow] = useState({});
  const [calculatedRowData, setCalculatedRowData] = useState({});
  const [rowData, setRowData] = useState([]);

  const handleRowClick = async (params) => {
    console.log(params.row);
    const takes = await fetchList('takes');
    console.log({takes});
    const sectionTakes = takes.filter((take) => take.course_id === params.row.course_id && take.sec_id === params.row.sec_id && take.semester === params.row.semester && take.year === params.row.year);

    // 集計
    const gradeCounts = { A: 0, B: 0, C: 0, D: 0, E: 0, F: 0 };
    sectionTakes.forEach(take => {
      gradeCounts[take.grade]++;
    });
    const gradeCountsArray = Object.entries(gradeCounts).map(([grade, count]) => ({
      name: grade,
      value: count
    }));

    // 生徒情報をマージ
    const students = await fetchList('students');
    console.log({students});
    const takesData = sectionTakes.map((take) => {
      const student = students.find((student) => take.student_id === student.student_id);
      return {
        ...take,
        ...student,
      };
    });
    console.log({takesData});
    setSelectedRow(params.row);
    setCalculatedRowData(gradeCountsArray);
    setRowData(takesData);
    setOpenDialog(true);
  };

  const handleCloseDialog = () => {
    setOpenDialog(false);
  };

  return (
    <>
      <Box sx={{ mb: 3 }}>
        <Accordion>
          <AccordionSummary
            expandIcon={<ArrowDropDownIcon />}
            aria-controls="panel1-content"
            id="panel1-header"
          >
            <Typography>登録</Typography>
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
                    登録
                  </Button>
                </Box>
              </Grid>
            </Box>
          </AccordionDetails>
        </Accordion>
      </Box>
      <Box>
        <DataGrid
          rows={rows}
          getRowId={(row) => `${row.course_id}-${row.sec_id}`}
          columns={columns}
          onRowClick={handleRowClick} 
        />
        <Dialog open={openDialog} onClose={handleCloseDialog}>
          <DialogTitle>成績分布</DialogTitle>
          <DialogContent>
            <DialogContentText>
              {`講義: ${selectedRow.title || ''}`}
              <br />
              {`年度: ${selectedRow.year || ''}`}
              <br />
              {`セメスター: ${selectedRow.semester || ''}`}
              <br />
              {`教員: ${selectedRow.name || ''}`}
              {/* その他のデータ... */}
              <BarChart width={480} height={300} data={calculatedRowData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#1976d2" />
              </BarChart>
              <TableContainer component={Paper}>
                <Table sx={{ width: 480 }} aria-label="simple table">
                  <TableHead>
                    <TableRow>
                      <TableCell align="center">名前</TableCell>
                      <TableCell align="center">学部</TableCell>
                      <TableCell align="center">成績</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {rowData.map((row) => (
                      <TableRow
                        key={row.student_id}
                        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                      >
                        <TableCell align="left">{row.name}</TableCell>
                        <TableCell align="left">{row.dept_name}</TableCell>
                        <TableCell align="right">{row.grade}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleCloseDialog}>閉じる</Button>
          </DialogActions>
        </Dialog>
      </Box>
    </>
  );
}