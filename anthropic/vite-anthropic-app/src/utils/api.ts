import axios, { AxiosInstance } from "axios";

const axiosInstance: AxiosInstance = axios.create({
    baseURL: 'http://localhost:5000',
    headers: {
        'Content-Type': 'application/json',
    }
})

export const getReply = async (message: string) => {
    try {
        const payload = {
            'message': message
        }

        const response = await axiosInstance.post('/', payload)
        return response.data
    } catch (error) {
        console.error('Error getting reply: ', error)
        throw error
    }
}

