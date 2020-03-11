<template>
	<div class="help_list">
		<van-tabs v-model="active">
		  <van-tab title="购买问题">
			  <div class="stage">
				<ul>
					<router-link :to="'/mweb/help/'+helpDetail.li_1.id">
						<li>{{helpDetail.li_1.title}}</li>
					</router-link>
					<router-link :to="'/mweb/help/'+helpDetail.li_2.id">
						<li>{{helpDetail.li_2.title}}</li>
					</router-link>
					<router-link :to="'/mweb/help/'+helpDetail.li_3.id">
						<li>{{helpDetail.li_3.title}}</li>
					</router-link>
					<router-link :to="'/mweb/help/'+helpDetail.li_4.id">
						<li>{{helpDetail.li_4.title}}</li>
					</router-link>
				</ul>
			  </div>
		  </van-tab>
		  <van-tab title="出售问题">
			  <div class="stage">
			  	<ul>
			  		<li>1.什么样的角色才能出售？</li>
			  		<li>2.角色出售流程？</li>
			  		<li>3.角色上架后会展示哪些信息？</li>
			  		<li>4.售出后怎么收款？</li>
			  	</ul>
			  </div>
		  </van-tab>
		  <van-tab title="其它问题">
			  <div class="stage">
			  	<ul>
			  		<li>1.交易收费规则</li>
			  		<li>2.支持交易的平台及服务器</li>
			  		<li>3.怎样修改绑定手机</li>
			  		<li>4.藏宝阁钱包</li>
					<li>5.运营主体说明</li>
			  	</ul>
			  </div>
		  </van-tab>
		</van-tabs>
	</div>
</template>

<script>
	export default{
		name:"helpList",
		props:["helpDetail"],
		data(){
			return{
				active:0
			}
		},
	}
</script>

<style scoped="scoped" lang="less">
	.stage{
		margin-top: 10px;
		ul li{
			padding: 10px;
			text-align: left;
			font-size: 14px;
			color: #1E1E1E;
			background-color: #FFFFFF;
			width: 355px;
			height: 23px;
		}
	}	
</style>
