import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './Title';

// Generate Order Data
function createData(id, date, content, from) {
  return { id, date, content, from };
}

const rows = [
  createData(
    0,
    '2023/12/28',
    'HOME画面を作りました',
    'やました',
  ),
];

export default function Notifications() {
  return (
    <React.Fragment>
      <Title>最近のお知らせ</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>日付</TableCell>
            <TableCell>内容</TableCell>
            <TableCell align="right">発信者</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.content}</TableCell>
              <TableCell align="right">{row.from}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}