import { useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { instructors } from '../../assets/sampleData.js'
import { Box } from '@mui/material';
import { useRecoilState } from "recoil";
import { pathState } from "../../atoms/pathState.js"

const columns = [
    { field: 'instructor_id', headerName: 'ID', width: 150, headerAlign: 'center' },
    { field: 'name', headerName: '名前', width: 150, headerAlign: 'center' },
    { field: 'dept_name', headerName: '学部', width: 150, headerAlign: 'center' },
    { field: 'salary', headerName: '給与', width: 150, headerAlign: 'center' },
];

export default function Instructors() {
    const [, setPath] = useRecoilState(pathState);
    useEffect(() => {
        setPath(() => "教員");
    }, []);

  return (
    <Box>
      <DataGrid
        rows={instructors}
        getRowId={(row) => row.instructor_id}
        columns={columns}
      />
    </Box>
  );
}