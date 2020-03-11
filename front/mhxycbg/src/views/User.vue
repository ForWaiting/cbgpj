<template>
  <div class="user">
	  <van-nav-bar title="我的藏宝阁" style="font-size: 16px; background-color: #FFFFFF;">
	    <van-icon name="envelop-o" size="25" color="#000000" slot="right" />
	  </van-nav-bar>
	  <div class="header">
		  <p class="avatar"><van-icon name="user-circle-o" color="#FFFFFF" size="100" /></p>
		  <div class="login"><van-button round type="info" color="#E74E4B" to="/mweb/login">
		  <span v-if="!islog" >登录</span>
		  <span v-else>
			{{$jsCookie.get('username')}}
		  </span>
		  </van-button></div> 
	  </div>
	  <div class="content_list">
		  <van-nav-bar title="我的还价" >
			  <van-icon name="cash-back-record" slot="left" size="25" color="#000000" />
		    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
		  </van-nav-bar>
		  <router-link to="/mweb/fav/">
		  <van-nav-bar title="我的收藏">
		  	<van-icon name="coupon-o" slot="left" size="25" color="#000000" />
		    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
		  </van-nav-bar>
		  </router-link>
	  </div>
	  <div class="content_list" style="margin-top: 10px;">
	  		  <van-nav-bar title="我的登记" >
	  			  <van-icon name="records" slot="left" size="25" color="#000000" />
	  		    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
	  		  </van-nav-bar>
	  		  <van-nav-bar title="我的钱包">
	  		  	<van-icon name="gold-coin-o" slot="left" size="25" color="#000000" />
	  		    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
	  		  </van-nav-bar>
			  <van-nav-bar title="我的出售">
			  	<van-icon name="bookmark-o" slot="left" size="25" color="#000000" />
			    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
			  </van-nav-bar>
	  </div>
	  <div class="content_list" style="margin-top: 10px; margin-bottom: 10px;">
	  		  <van-nav-bar title="帮助中心" >
	  			  <van-icon name="smile-comment-o" slot="left" size="25" color="#000000" />
	  		    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
	  		  </van-nav-bar>
	  		  <van-nav-bar title="意见反馈">
	  		  	<van-icon name="chat-o" slot="left" size="25" color="#000000" />
	  		    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
	  		  </van-nav-bar>
	  			  <van-nav-bar title="专属客服">
	  			  	<van-icon name="service-o" slot="left" size="25" color="#000000" />
	  			    <van-icon name="arrow" slot="right" size="25" color="#000000"/>
	  			  </van-nav-bar>
	  </div>
	  <div class="footer">
		<van-button @click="logout" size="large" round type="primary" color="linear-gradient(to right, #4bb0ff, #6149f6)">注销</van-button>
	  </div>
  </div>
</template>

<script>

export default {
	data(){
		return{
			flag:""
		}
	},
	computed:{
		islog(){
			return this.$store.state.islog
		}
	},
	created() {
		this.flag=localStorage.getItem("login")
		console.log(this.flag)
	},
	methods:{
		// logout(){
		// 	localStorage.removeItem("login")
		// 	this.$router.push("/mweb")
		// }
		logout(){
			this.$router.push('/mweb')
			this.$jsCookie.remove('username')
			this.$jsCookie.remove('refresh')
			this.$jsCookie.remove('access')
			this.$store.commit('setLog',false)
			
		}
	}
}
</script>
<style scoped="scoped" lang="less">
	.user{
		box-sizing: border-box;
	}
	.footer{
		margin-bottom: 50px;
		
	}
	.user{
		.header{
			width: 375px;
			height: 240px;
			background: url("../../public/img/header-bg.jpg") no-repeat;
			background-size: cover;
			.avatar{
				margin: 0px;
				padding-top: 40px;
				width: 375px;
				height: 90px;
			}
			.login{
				padding-top: 20px;
				width: 375px;
				height: 30px;
			}
		}
	}
</style>