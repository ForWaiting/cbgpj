<template>
  <div id="app">
    <router-view/>
	<van-tabbar v-show="$route.meta.tabbar" v-model="active" active-color="#FF0000"
	  inactive-color="#000" style="height: 48px;">
	  <van-tabbar-item to="/mweb">
	    <span>首页</span>
	    <img
	      slot="icon"
	      slot-scope="props"
	      :src="props.active? icon.active : icon.inactive"
	    >
	  </van-tabbar-item>
	  
	  <van-tabbar-item  v-if="!islog" to="/mweb/login/">
		  <span>订单</span>
		<img
		  slot="icon"
		  slot-scope="props"
		  :src="props.active == 1? icon1.active : icon1.inactive"
		>
		</van-tabbar-item>
		<van-tabbar-item  v-else to="/mweb/orders">
				  <span>订单</span>
				<img
				  slot="icon"
				  slot-scope="props"
				  :src="props.active == 1? icon1.active : icon1.inactive"
				>
				</van-tabbar-item>
		
	  <van-tabbar-item to="/mweb/user">
		  <span>我的</span>
		<img
		  slot="icon"
		  slot-scope="props"
		  :src="props.active == 2? icon2.active : icon2.inactive"
		>
		</van-tabbar-item>
	</van-tabbar>
  </div>
</template>

<script>
	export default {
	  data() {
	    return {
	      active: 0,
	      icon: {
	        active: 'img/foot_icon1c.png',
	        inactive: 'img/foot_icon1.png'
	      },
		  icon1: {
		    active: 'img/foot_icon2c.png',
		    inactive: 'img/foot_icon2.png'
		  },
		  icon2: {
		    active: 'img/foot_icon3c.png',
		    inactive: 'img/foot_icon3.png'
		  }
	    }
	  },
	  computed:{
	  	islog(){
	  		return this.$store.state.islog
	  	}
	  },
	}
</script>
<style lang="less">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
