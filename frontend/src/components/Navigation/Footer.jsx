import Typography from '@mui/material/Typography';
export default function Footer(props) {
    return (
        <Typography variant="body2" color="text.secondary" align="center" {...props}>
            {`Copyright © コラボレイティブ開発特論2023 G4 ${new Date().getFullYear()}.`}
        </Typography>
    )
}