import { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
// import { students } from '../../assets/sampleData.js'
import { Box } from '@mui/material';
import { useRecoilState } from "recoil";
import { pathState } from "../../atoms/pathState"
import { fetchList } from '../../assets/api.js';


const columns = [
    { field: 'student_id', headerName: 'ID', width: 150, headerAlign: 'center' },
    { field: 'name', headerName: '名前', width: 150, headerAlign: 'center' },
    { field: 'dept_name', headerName: '学部', width: 150, headerAlign: 'center' },
    { field: 'tot_cred', headerName: 'tot_cred', width: 150, headerAlign: 'center' },
];

export default function Students() {
  const [, setPath] = useRecoilState(pathState);
  const [students, setStudents] = useState([]);

  useEffect(() => {
    setPath(() => "生徒");
    const fetchData = async () => {
      const res = await fetchList('students');
      setStudents(res);
    };
    fetchData();
  }, []);

  return (
    <Box>
      <DataGrid
        rows={students}
        getRowId={(row) => row.student_id}
        columns={columns}
      />
    </Box>
  );
}