import Axios from 'axios'

export const BASE_URL = 'http://localhost:5000/api'
const Client = Axios.create({ baseURL: BASE_URL })

export default Client
