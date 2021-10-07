import VueRouter from 'vue-router'
import Feed from './pages/Feed'
import Profile from './pages/Profile'

const routes = [
  { path: '/', component: Feed, name: 'Feed' },
  { path: '/profile', component: Profile, name: 'Profile' }
]

export default new VueRouter({ routes, mode: 'history' })
