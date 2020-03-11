<template>
	<div class="login">
		<div class="top">
			<van-nav-bar title="登录"
			  @click-left="onClickLeft"
			  @click-right="onClickRight">
			  <van-icon name="arrow-left" slot="left" size="25" color="#000" />
			  <van-icon name="home-o" slot="right" size="25" color="#000" />
			</van-nav-bar>
			<van-tabs >
			  <van-tab title="网易用户登录">
				  <van-field v-model="loginEmail" type="email" label="网易用户" placeholder="请输入用户名" required />
				  <van-field v-model="loginPassword" type="password" label="账号密码" placeholder="请输入密码" required />
				  <br>
				  <br>
				  <van-button size="large" round type="primary" color="linear-gradient(to right, #4bb0ff, #6149f6)" @click="login">登录</van-button>
			  </van-tab>
			  <van-tab title="网易用户账号注册">
				  <van-field v-model="registerEmail" type="email" label="网易用户" placeholder="请输入用户" required />
				  <van-field v-model="registerPassword" type="password" label="账号密码" placeholder="请输入密码" required />
				  <van-field v-model="registerPassword1" type="password" label="确认密码" placeholder="请输入确认密码" required />
				  <br>
				  <br>
				  <van-button size="large" round type="primary" color="linear-gradient(to right, #4bb0ff, #6149f6)" @click="register">注册</van-button>
			  </van-tab>
			</van-tabs>
		</div>
	</div>
</template>

<script>
// export default {
// 	 data() {
// 	    return {
// 	      active: 0,
// 		  loginEmail:"",
// 		  loginPassword:"",
// 		  registerEmail:"",
// 		  registerPassword:"",
// 		  registerPassword1:""
		  
// 	    };
// 	  },
// 	  methods: {
// 		onClickLeft() {
// 		  this.$router.go(-1);
// 		},
// 		onClickRight() {
// 		  this.$router.push("/mweb");
// 		},
// 		login(){
// 			localStorage.setItem("login",true);
// 			if(this.$route.query.t){
// 				this.$router.push(this.$route.query.t);
// 			}else{
// 				this.$route.push("/mweb")
// 			}
// 		},
// 		register(){
			
// 		}
// 	  }
// }
export default{
	data(){
		return{
			loginEmail:null,
			loginPassword:null,
		    registerEmail:null,
		    registerPassword:null,
		    registerPassword1:null,
		}
	},
	methods:{
		onClickLeft() {
		  this.$router.go(-1);
		},
		onClickRight() {
		  this.$router.push("/mweb");
		},
		login(){
			this.$api.getToken({
				username:this.loginEmail,
				password:this.loginPassword,
			}).then(res=>{
				console.log('得到Token',res)
				this.$jsCookie.set('refresh',res.data.refresh);
				this.$jsCookie.set('access',res.data.access);
				this.$jsCookie.set('username',this.loginEmail);
				this.$router.push("/mweb/")
				this.$store.commit('setLog',true)
			}).catch(err=>{
				this.$toast('登录错误')
			})
		},
		register(){
			this.$api.regist({
				username:this.registerEmail,
				password:this.registerPassword,
				password2:this.registerPassword1
			}).then(res=>{
				this.$toast('注册成功')
				this.$router.push('/mweb/')
			}).catch(err=>{
				this.$toast('注册失败')
			})
		}
	}
}
</script>

<style>
</style>
