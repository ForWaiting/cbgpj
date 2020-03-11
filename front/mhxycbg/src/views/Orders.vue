<template>
  <div class="orders">
	  <div class="top">

			<van-nav-bar title="订单"
			@click-left="onClickLeft"
			>
			 <van-icon name="arrow-left" slot="left" size="25" color="#000" />
			  <van-icon name="envelop-o" size="25" color="#000000" slot="right" />
			</van-nav-bar>
			<van-tabs>
			  <van-tab title="全部">内容 1</van-tab>
			  <van-tab title="待付款">内容 2</van-tab>
			  <van-tab title="已取消">内容 3</van-tab>
			</van-tabs>
	  </div>
  </div>
</template>
<script>
	export default {
	  // data() {
	  //   return {
	  //     active: 0
	  //   };
	  // }

	  methods:{
	  	onClickLeft() {
	  	  this.$router.go(-1);
	  	},
	}
}
</script>