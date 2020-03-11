import jsCookie from 'js-cookie'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000';


export const getWorthWatching = ()=>{
	return axios.get('/api/v1/worthwatchings/')
}

export const getspecialRecommend = ()=>{
	return axios.get('/api/v1/specialrecommends/')
}

export const getroleLists = ()=>{
	return axios.get('/api/v1/rolelists/')
}

export const getToken = (param)=>{
	return axios.post('/tokenlogin/',param)
}

// 注册
export const regist = (param)=>{
	return axios.post('/api/v1/users/',param)
}