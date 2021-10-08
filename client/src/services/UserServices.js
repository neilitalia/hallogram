import Client from './api'

export const GetUser = async user_id => {
  const res = await Client.get(`/users/${user_id}`)
  return res.data
}

export const GetAllUsers = async () => {
  const res = await Client.get('/users')
  return res.data
}

export const CreateUser = async data => {
  const res = await Client.post('/users', data)
  return res
}

export const DeleteUser = async user_id => {
  const res = await Client.delete(`/users/${user_id}`)
  return res.data
}
