import Client from './api'

export const GetPosts = async () => {
  const res = await Client.get('/posts')
  return res.data
}

export const CreatePost = async () => {
  const res = await Client.get('/posts')
  return res
}

export const DeletePost = async post_id => {
  const res = await Client.get(`/posts/${post_id}`)
  return res
}
