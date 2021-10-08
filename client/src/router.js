import VueRouter from 'vue-router'
import Feed from './pages/Feed'
import Profile from './pages/Profile'
import Welcome from './pages/Welcome'

const routes = [
  { path: '/', component: Feed, name: 'Feed' },
  { path: '/profile', component: Profile, name: 'Profile' },
  { path: '/welcome', component: Welcome, name: 'Welcome'}
]

export default new VueRouter({ routes, mode: 'history' })
