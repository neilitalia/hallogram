import Client from './api'

export const GetPosts = async () => {
  const res = await Client.get('/posts')
  return res.data
}

export const CreatePost = async data => {
  const res = await Client.post('/posts', data)
  return res
}

export const DeletePost = async post_id => {
  const res = await Client.delete(`/posts/${post_id}`)
  return res
}

export const ClapPost = async post_id => {
  const res = await Client.put(`/posts/clap/${post_id}`)
  return res
}

export const UploadImage = async file => {
  const res = await Client.post('/posts/image', file)
  return res
}