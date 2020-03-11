import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
	  goodFav:[],
	  islog:false
  },
  getters: {
	  getGoodFav(state){
		  return state.goodFav
	  }
  },
  mutations: {
  	  addGood(state,good){
  		  let canAdd=true;
  		  // let index="";
  		  state.goodFav.forEach((item,i)=>{
  			  if(item.id==good.id){
  				  canAdd=false;
  				  // index=i
  			  }
  		  })
  		  if(canAdd){
  			  state.goodFav.push(good);
  			  // console.log(good)
  		  }
  	  },
	  setLog(state,b){
	  		  state.islog=b
	  },
  },
  actions: {
  },
  modules: {
  }
})
