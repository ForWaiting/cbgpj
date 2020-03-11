<template>
	<div class="detail">
		<div class="top">
			<van-nav-bar title="商品详情">
			  <van-icon @click="goback" size="25" name="arrow-left" slot="left" />
			  <van-icon size="25" name="ellipsis" slot="right" />
			</van-nav-bar>
		</div>
		<div class="content">
			<roleGoods />
			<h1>详情页商品id为{{$route.params.id}}</h1>
		</div>
		<div class="footer">
			<van-goods-action>
			  <van-goods-action-icon @click="addMyFav" icon="star-o" text="收藏" />
			  <van-goods-action-icon icon="refund-o" text="还价" />
			  <van-goods-action-icon icon="service-o" text="客服" />
			  <van-goods-action-button type="danger" text="立即购买" />
			</van-goods-action>
		</div>
	</div>
</template>

<script>
	import {roleLists} from '../data.js'
	import roleGoods from '@/components/roleGoods.vue'
	export default{
		name: 'Deatils',
		data(){
			return{
				datas:null,	
				dataList:""
			}
		},
		created() {
			this.dataList = roleLists
			for(let i=0; i<this.dataList.length;i++){
				if (this.dataList[i].id == this.$route.params.id){
					this.datas = this.dataList[i]
				}
			}
		},
		components: {
			roleGoods
		},
		methods:{
		  goback(){
			  this.$router.go(-1)
		  },
		  addMyFav(){
			this.$toast("收藏成功")
			this.$store.commit("addGood",{
				id:this.datas.id,
				icon:this.datas.icon,
				format_name:this.datas.format_name,
				equip_level:this.datas.equip_level,
				area_name:this.datas.area_name,
				server_name:this.datas.server_name,
				desc_sumup_short:this.datas.desc_sumup_short,
				price:this.datas.price,
				highlights:this.datas.highlights,
				collect_num:this.datas.collect_num,
				ic_sys:this.datas.ic_sys,
				sale_data:this.datas.sale_data
			})
		  }
		}
	}
</script>

<style>
</style>
