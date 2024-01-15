import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import { DataGrid } from '@mui/x-data-grid';
import { courseSection } from '../../assets/sampleData.js'
import { Box } from '@mui/material';

// const rows = [
//     { id: 1, col1: 'Hello', col2: 'World' },
//     { id: 2, col1: 'DataGridPro', col2: 'is Awesome' },
//     { id: 3, col1: 'MUI', col2: 'is Amazing' },
// ];

const columns = [
    { field: 'course_id', headerName: 'コースID', width: 150, headerAlign: 'center' },
    { field: 'sec_id', headerName: 'セクションID', width: 150, headerAlign: 'center' },
    { field: 'semester', headerName: 'セメスター', width: 150, headerAlign: 'center' },
    { field: 'year', headerName: '年度', width: 150, headerAlign: 'center' },
    { field: 'building', headerName: '建物', width: 150, headerAlign: 'center' },
    { field: 'room_number', headerName: '部屋番号', width: 150, headerAlign: 'center' },
    { field: 'time_slot_id', headerName: 'タイムスロット', width: 150, headerAlign: 'center' },
];

export default function Home() {
  return (
    <>
      <Box>
        <Accordion>
          <AccordionSummary
            expandIcon={<ArrowDropDownIcon />}
            aria-controls="panel1-content"
            id="panel1-header"
          >
            <Typography>検索</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
              malesuada lacus ex, sit amet blandit leo lobortis eget.
            </Typography>
          </AccordionDetails>
        </Accordion>
      </Box>
      <Box>
        <DataGrid rows={courseSection} getRowId={(row) => `${row.course_id}-${row.sec_id}`} columns={columns} />
      </Box>
    </>
  );
}