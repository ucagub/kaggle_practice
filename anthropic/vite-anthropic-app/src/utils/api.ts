import axios, { AxiosInstance, AxiosResponse } from 'axios';

// const axiosInstance = axios.create({
const axiosInstance: AxiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    headers: {
        'Content-Type': 'application/json',
    }
})

export const getReply = async (message: string): Promise<string> => {
    try {
        const payload = {
            'message': message
        }

        const response: AxiosResponse = await axiosInstance.post('/', payload)
        return response.data
    } catch (error) {
        console.error('Error getting reply: ', error)
        throw error
    }
}

