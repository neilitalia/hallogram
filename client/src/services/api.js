import Axios from 'axios'

export const BASE_URL = 'http://localhost:8080/api'
const Client = Axios.create({ baseURL: BASE_URL })

export default Client
