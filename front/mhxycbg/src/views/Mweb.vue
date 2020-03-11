<template>
	<div class="mweb">
		<div class="header">
			<div class="title_left">

			</div>
			<div class="title_right1">
				<img src="img/icon_filter.png" alt="">
			</div>
			<div class="title_right2">
				<img src="img/icon_msg.png" alt="">
			</div>
		</div>
		<div class="body">
			<div class="notice_bar">
				<van-notice-bar mode="link" class="textline" @click="checkLook">
					<span style="font-size: 15px;">萌新不知道怎么交易？点击这里获取帮助</span>
				</van-notice-bar>
			</div>
			<div class="categories">
				<div>
					<router-link :to="'/mweb/rolrDetailList/'+'001'" style="color: #000000;">
						<img src="img/icon1.png" alt="">
						<p>全部角色</p>
					</router-link>
				</div>
				<div>
					<img src="img/icon2.png" alt="">
					<p>ios角色</p>
				</div>
				<div>
					<img src="img/icon3.png" alt="">
					<p>安卓角色</p>
				</div>
				<div>
					<router-link to="/mweb/fav/" style="color: #000000;">
						<img src="img/icon4.png" alt="">
						<p>我的收藏</p>
					</router-link>
				</div>
			</div>
			<div class="shortcuts">
				<div class="regist">
					<img src="img/task1.png" alt="">
					<span>登记出售</span>
				</div>
				<div class="sell">
					<img src="img/task2.png" alt="">
					<span>我的出售</span>
				</div>
			</div>
			<div class="index_zixun">
				<div class="zixun_img">
					<img src="img/worth.png" alt="" style="width: 61px;height: 20px;">
				</div>
				<div class="roll">
					<worthRecommend />
				</div>
			</div>
			<div class="recommend">
				<specialRecommend />
			</div>
			<div class="for_recommend">
				<van-divider :style="{ color: '#1989fa', borderColor: '#8F8F8F' }">
				  <span style="font-size: 16px; color: #1E1E1E;">为您推荐</span>
				</van-divider>
				<forRecommend />
			</div>
			<div class="footer" style="margin-top: 20px;" >
				<router-link :to="'/mweb/rolrDetailList/'+'001'" style="color: #000000;">
					<van-button style="height: 40px;" round type="default"><b>查看全部</b></van-button>
				</router-link>
				<div class="text" style="width: 355px; height: 45px;">
					<p style="font-size: 12px;">禁止使用爬虫采集数据和转载商业化</p>
					<span style="font-size: 12px;">服务协议 - 隐私政策</span>
					<br>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
import worthRecommend from '@/components/WorthRecommend.vue'
import specialRecommend from '@/components/SpecialRecommend.vue'
import forRecommend from '@/components/ForRecommend.vue'
export default {
  name: 'mweb',
  components: {
    worthRecommend,
	specialRecommend,
	forRecommend
  },
  methods:{
	  checkLook(){
		  this.$router.push("/mweb/help")
	  }
  }
}
</script>
<style scoped="scoped" lang="less">
	*{
		box-sizing: border-box;
	}
	.mweb {
		width: 100%;
		margin-bottom: 48px;
	}
	.header {
		display: flex;
		height: 150px;
		background: url("../../public/img/index-banner.jpg") no-repeat;
		background-size: cover;
		.title_left {
			width: 285px;
			height: 45px;
		}
		.title_right1 {
			width: 45px;
			height: 45px;
			img {
				margin-top: 8px;
				width: 30px;
				height: 30px;
			}
		}
		.title_right2 {
			width: 45px;
			height: 45px;
			img {
				margin-top: 8px;
				width: 30px;
				height: 30px;
			}
		}
	}
	.body {
		margin: -10px 0px 0px;
		padding: 10px;
		background: #F5F5F5;
		// border: 2px solid #000000;
		border-radius: 10px 10px 0px 0px;
		.notice_bar{
			width: 355px;
			height: 34px;
			border-radius: 10px;
			overflow: hidden;
			background-color: #fffaef;
			-webkit-box-align: center;
		}
		.categories {
			height: 70px;
			width: 355px;
			display: flex;
			margin: 10px 0px 0px;
			background-color: #FFFFFF;
			img {
				width: 44px;
				height: 44px;
			}
			p{
				width: 88px;
				height: 12px;
				font-size: 12px;
				margin: 3px 0px 0px;
			}
		}
		.shortcuts {
			width: 355px;
			height: 45px;
			margin: 10px 0px 0px;
			display: flex;
			border-radius: 10px;
			overflow: hidden;
			background-color: #FFFFFF;
			.regist{
				display: flex;
				width: 177.5px;
				height: 45px;
				padding: 0px 0px 0px 14px;
				img {
					width: 24px;
					height: 24px;
					margin: 10px 8px 0px 0px;
				}
				span{
					font-size: 15px;
					position: absolute;
					margin-top: 12px;
					margin-left: 30px;
				}
			}
			.sell{
				display: flex;
				width: 177.5px;
				height: 45px;
				padding: 0px 0px 0px 14px;
				img {
					width: 24px;
					height: 24px;
					margin: 10px 8px 0px 0px;
				}
				span{
					font-size: 15px;
					position: absolute;
					margin-top: 12px;
					margin-left: 30px;
				}
			}
		}
		
		.index_zixun {
			width: 355px;
			display: flex;
			height: 50px;
			border-radius: 10px;
			overflow: hidden;
			margin: 10px 0px 0px;
			padding: 6px 10px;
			background-color: #FFFFFF;
			.zixun_img{
				width: 80px;
				border-right: 1px solid #8F8F8F;
				img{
					width: 61.5px;
					height: 20.5px;
					margin-top: 8px;
				}
			}
			.roll{
				display: flex;
				overflow: hidden;
				width: 275px;
				height: 50px;
			}
		}
		.recommend{
			width: 355px;
			height: 191px;

		}
	}
</style>
