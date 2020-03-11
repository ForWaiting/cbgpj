<template>
	<div class="forRecommend">
		<div class="sepcial">

		</div>
		<div  v-for="(item,index) in roleList" :key="index">
			<router-link :to="'/mweb/details/'+item.id" class="detail" style="color: #000000;">
				<div class="left">
					<img :src=item.icon alt="" style="width: 60px;height: 60px; background-color: #FFFFFF;">
				</div>
				<div class="right">
					<div class="headline">
						<span style="font-size: 16px;">{{item.format_name}} |{{item.equip_level}}级</span>
						<span >{{item.area_name}}-{{item.server_name}}<img :src=item.ic_sys alt="" style="width: 15px; height 15px; margin-left: 5px;"></span>
					</div>
					<div class="headmid">
						<span>{{item.desc_sumup_short}}</span>
						<span style="font-size: 18px; color: #E74E4B;">￥{{item.price}}</span>
					</div>
					<div class="list">
						<ul>
							<li v-for="(item,index) in item.highlights" :key='index' >{{item.name}}</li>
						</ul>
						<div class="collect">
							<span>{{item.collect_num}}人收藏</span>
						</div>
					</div>
				</div>
			</router-link>
		</div>
	</div>
</template>

<script>
	// import {
	// 	roleLists
	// } from '../data.js';
	// export default {
	// 	name: 'forRecommend',
	// 	data() {
	// 		return {
	// 			roleList:null  
	// 		}
	// 	},
	// 	created() {
	// 		this.roleList = roleLists
	// 	}
	// }
	export default{
		data(){
			return{
				roleList:null
			}
		},
		created() {
			this.$api.getroleLists().then(res=>{
				// console.log('获取成功',res);
				if(res.status==200){
					this.roleList = res.data
				}
			}).catch(err=>{
				console.log('出错了')
			})
		}
	}
</script>

<style scoped="scoped" lang="less">
	.forRecommend{
		width: 355px;
		background-color: #FFFFFF;
		border-radius: 10px 10px 0px 0px;
	}
	.detail{
		width: 355px;
		height: 90px;
		border-top: 1px solid lightgray;
		// border: 1px solid #009926;
		display: flex;
		padding: 15px 10px;
		box-sizing: border-box;
		.left{
			width: 60px;
			height: 60px;
			border: 1px solid lightgray;
			border-radius: 5px;
			margin: 0px 10px 0px 0px;
		}
		.right{
			width: 265px;
			height: 60px;
			.headline{
				display: flex;
				width: 265px;
				height: 17px;
				justify-content: space-between;
				span{
					font-size: 12px;
				}
			}
			.headmid{
				display: flex;
				width: 265px;
				height: 17px;
				margin-top: 5px;
				justify-content: space-between;
				span{
					font-size: 12px;
				}
			}
			.list{
				display: flex;
				width: 265px;
				height: 19px;
				box-sizing: border-box;
				margin-top: 3px;
				justify-content: space-between;
			}
			.list ul li {
				margin-right: 5px;
				list-style: none;
				float: left;
				height: 16px;
				text-align: center;
				font-size: 12px;
				border: 1px solid rgb(238, 131, 129);
				color: rgb(238, 131, 129);
				}
			}
			.collect{
				height: 19px;
				span{
					padding-left: 30px;
					height: 13px;
					color: #888888;
					font-size: 12px;
				}
		}
	}
</style>
