import { createTheme } from '@mui/material/styles'

const defaultStyle = {
    components: {
        MuiDataGrid: {
          styleOverrides: {
            columnHeader: {
              backgroundColor: 'lightblue', // ここでヘッダの背景色を設定
            },
          },
        },
    },
}

export default createTheme({
  ...defaultStyle,
})