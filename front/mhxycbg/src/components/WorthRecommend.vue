<template>
	<div class="recommend">
		<div class="connent">
			<van-swipe style="height: 45px;" vertical :autoplay="3000" :touchable="false" :show-indicators="false">
				<van-swipe-item v-for="(item,index) in watchList" :key="index"> <a :href=item.video_url style="color: #000000;"><span>{{item.title}}</span></a></van-swipe-item>
			</van-swipe>
		</div>
		<div class="con_img">
			<van-swipe style="height: 45px;" vertical :autoplay="3000" :touchable="false" :show-indicators="false">
				<van-swipe-item v-for="(item,index) in watchList" :key="index"><a :href=item.video_url><img :src=item.img alt=""></a></van-swipe-item>
			</van-swipe>
		</div>

	</div>
</template>

<script>
	// import {
	// 	worthWatching
	// } from '../data.js';
	// export default {
	// 	name: 'worthRecommend',
	// 	data() {
	// 		return {
	// 			watchList: null,
	// 		}
	// 	},
	// 	created() {
	// 		this.watchList = worthWatching;
	// 		// console.log(this.watchList)
	// 	}
	// }
	export default {
		data() {
			return {
				watchList: null,
			}
		},
		created() {
			this.$api.getWorthWatching().then(res=>{
				console.log('值得看获取成功',res)
				if(res.status==200){
					this.watchList=res.data
					console.log('++++++',res.data)
				}
			}).catch(err=>{
				console.log('获取失败')
			})
		}
	}
</script>

<style scoped="scoped" lang="less">
	.recommend{
		display: flex;
		.connent{
			box-sizing: border-box;
			margin-right: 5px;
			padding: 5px;
			width: 192.5px;
			font-size: 14px;
		}
		.con_img{
			width: 50px;
			height: 39px;
			img{
				width: 50px;
				height: 39px;
			}
		}
		
	}
</style>
