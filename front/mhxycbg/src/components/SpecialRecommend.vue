<template>
	<div class="specialRecommend">
		<div class="sepcial">
			<van-divider :style="{ color: '#1989fa', borderColor: '#8F8F8F' }">
			  <span style="font-size: 16px; color: #1E1E1E;">专题推荐</span>
			</van-divider>
		</div>
		<div class="content">
			<div class="topics" v-for="(item,index) in specialList" :key="index" style="backgroundColor:rgb(199, 224, 234)">
				<div class="text">
					<div class="firstline" style="color:rgb(50, 221, 168)">{{item.title}}</div>
					<div class="secondline" style="color:rgb(236, 109, 90)">{{item.sub_title}}</div>
				</div>
				<div class="roleimg">
					<img :src=item.icon alt="">
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	// import {
	// 	specialRecommend
	// } from '../data.js';
	// export default {
	// 	name: 'specialRecommend',
	// 	data() {
	// 		return {
	// 			specialList:null 
	// 		}
	// 	},
	// 	created() {
	// 		this.specialList = specialRecommend
	// 		console.log(this.specialList)
	// 	}
	// }
	export default {
		data() {
			return {
				specialList:null 
			}
		},
		created() {
			this.$api.getspecialRecommend().then(res=>{
				// console.log('专题推荐获取成功',res)
				if(res.status==200){
					this.specialList = res.data
				}
			}).catch(err=>{
				console.log('专题推荐数据异常')
			})
		}
	}
</script>

<style scoped="scoped" lang="less">
	.specialRecommend{
		width: 355px;
		height: 191px;
		background-color: #FFFFFF;
		margin-top: 10px;
		border-radius: 10px;
		padding: 10px;
		.sepcial{
			.van-divider--content-center{
				margin: 0px;
			}
		}
		.content{
			display: flex;
			flex-wrap: wrap;
			width: 335px;
			height: 150px;
			box-sizing: border-box;
			background-color: #FFFFFF;
			.topics{
				display: flex;
				width: 155px;
				height: 70px;
				margin-left: 8px;
				border-radius: 10px;
				overflow: hidden;
				.text{
					padding-top: 6px;
					margin-right: 10px;
					width: 85px;
					height: 64px;
					.firstline{
						font-size: 16px;
					}
					.secondline{
						font-size: 12px;
					}
				}
				.roleimg{
					img{
						padding-top: 6px;
						width: 74px;
						height: 65px;
					}
				}
			}
		}
	}
</style>
