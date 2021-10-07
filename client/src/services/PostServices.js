import Client from './api'

export const GetPosts = async () => {
  try {
    const res = Client.get('/posts')
    return res.data
  } catch (error) {
    throw error
  }
}

export const CreatePost = async () => {
  try {
    const res = Client.get('/posts')
    return res.data
  } catch (error) {
    throw error
  }
}

export const DeletePost = async post_id => {
  try {
    const res = Client.get(`/posts/${post_id}`)
    return res.data
  } catch (error) {
    throw error
  }
}
