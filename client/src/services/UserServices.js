import Client from './api'

export const GetUser = async user_id => {
  try {
    const res = await Client.get(`/users/${user_id}`)
    return res.data
  } catch (error) {
    throw error
  }
}

export const GetAllUsers = async () => {
  try {
    const res = await Client.get('/users')
    return res.data
  } catch (error) {
    throw error
  }
}

export const CreateUser = async data => {
  try {
    const res = await Client.post('/users', data)
    return res.data
  } catch (error) {
    throw error
  }
}

export const DeleteUser = async user_id => {
  try {
    const res = await Client.delete(`/users/${user_id}`)
    return res.data
  } catch (error) {
    throw error
  }
}
