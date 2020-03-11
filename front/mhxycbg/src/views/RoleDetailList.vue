<template>
	<div class="roleDetailList">
		<div class="top">
			<van-nav-bar title="商品列表">
			  <van-icon @click="goback" size="25" name="arrow-left" slot="left" />
			  <van-icon size="25" name="ellipsis" slot="right" />
			</van-nav-bar>
		</div>
		<van-dropdown-menu>
		  <van-dropdown-item v-model="value1" :options="option1" />
		  <van-dropdown-item v-model="value2" :options="option2" />
		</van-dropdown-menu>
		<div class="content">
			<forRecommend />
			<p>加载完成</p>
		</div>
	</div>
</template>

<script>
	import forRecommend from '@/components/ForRecommend.vue'
	export default{
	components: {
		forRecommend
	},
	data() {
	  return {
		value1: 0,
		value2: 'a',
		option1: [
		  { text: '操作系统', value: 0 },
		  { text: 'IOS平台', value: 1 },
		  { text: '安卓平台', value: 2 }
		],
		option2: [
		  { text: '价格排序', value: 'a' },
		  { text: '从低到高', value: 'b' },
		  { text: '从高到低', value: 'c' },
		]
	  }
	},
	  methods:{
		  goback(){
			  this.$router.go(-1)
		  },
	  }
	}
</script>

<style scoped="scoped" lang="less">

</style>
