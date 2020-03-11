<template>
	<div class="help">
		<div class="top">
			<van-nav-bar title="帮助中心">
			  <van-icon @click="goback" size="25" name="arrow-left" slot="left" />
			  <van-icon size="25" name="ellipsis" slot="right" />
			</van-nav-bar>
		</div>
		<div class="header">
			<helpList :helpDetail="help_data" />
		</div>
	</div>
</template>

<script>
	import helpList from '@/components/HelpList.vue'
	import {
		helpData
	} from '../data.js';
	export default {
	  name:"help",
	  components:{
		  helpList
	  },
	  data() {
	    return {
	      active: 0,
		  help_data:""
	    };
	  },
	  created() {
	  	this.help_data=helpData
		console.log(this.help_data)
	  },
	  methods:{
		  goback(){
			  this.$router.go(-1)
		  }
	  }
	}
	
</script>

<style scoped="scoped" lang="less">
	.help{
		width: 375px;
		height: 667px;
		background-color: #F5F5F5;
	}

</style>
