import VueRouter from 'vue-router'
import Feed from './pages/Feed'
import Profile from './pages/Profile'
import NewPost from './components/NewPost'

const routes = [
  { path: '/', component: Feed, name: 'Feed' },
  { path: '/profile', component: Profile, name: 'Profile' },
  { path: '/newpost', component: NewPost, name: 'NewPost'}
]

export default new VueRouter({ routes, mode: 'history' })
