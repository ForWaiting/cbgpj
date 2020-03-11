import Vue from 'vue'
import VueRouter from 'vue-router'
import Mweb from '../views/Mweb.vue'
import Orders from '../views/Orders.vue'
import User from '../views/User.vue'
import Details from '../views/Details.vue'
import Login from '../views/Login.vue'
import MyFav from '../views/MyFav.vue'
import Help from '../views/Help.vue'
import HelpDetails from '../views/HelpDetails.vue'
import RoleDetailList from '../views/RoleDetailList.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/mweb',
    name: 'mweb',
    component: Mweb,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/mweb/login/',
    name: 'login',
    component: Login
  },
  {
    path: '/mweb/fav/',
    name: 'myfav',
    component: MyFav
  },
  {
    path: '/mweb/orders/',
    name: 'orders',
    component: Orders,
	// meta:{
	// 	tabbar:true,
	// 	auth:true
	// }
  },
  {
    path: '/mweb/details/:id/',
    name: 'details',
    component: Details
  },
  {
    path: '/mweb/user/',
    name: 'user',
    component: User,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/mweb/help/',
    name: 'help',
    component: Help
  },
  {
    path: '/mweb/help/:id/',
    name: 'helpDetails',
    component: HelpDetails
  },
  {
    path: '/mweb/rolrDetailList/:id/',
    name: 'roleDetails',
    component: RoleDetailList
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach(function(t,f,n){
	// console.log(t,f,n);
	let r = localStorage.getItem("login");
	if(t.meta.auth){
		if(r){
			n();
		}else{
			n("/mweb/login?t="+t.path)
		}
	}else{
		n();
	}
})
export default router
