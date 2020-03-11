<template>
	<div class="help_details">
		<div class="top">
			<van-nav-bar title="帮助中心">
			  <van-icon @click="goback" size="25" name="arrow-left" slot="left" />
			  <van-icon size="25" name="ellipsis" slot="right" />
			</van-nav-bar>
		</div>
		<div class="title">
			<h1>详情页id为{{$route.params.id}}</h1>
		</div>
		
	</div>
</template>

<script>
	import {
		helpData
	} from '../data.js';
	export default{
		data(){
			return{
				helpData1:""
			}
		},
		created() {
			this.helpData1=helpData
		},
		methods:{
		  goback(){
			  this.$router.go(-1)
		  }
		}
	}
</script>

<style>
</style>
