import axios from 'axios';

const axiosAuthInstance = axios.create({
    baseURL: '/api/',
    headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
    },
});

export const fetchList = async (type) => {
    try {
        const res = await axiosAuthInstance.get(`/${type}/`);
        // console.info(`fetchList ${type} response`, res.data);  // レスポンスデータ
        return res.data;
    } catch (error) {
        console.error(error);
        throw error;
    }
}
