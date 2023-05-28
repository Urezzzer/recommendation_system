import axios from 'axios'
import config from '../config'

const API_URL = config.api

class Service {

    async getInit() {
        return axios.get(API_URL + 'init').then((res, err) => {
            if (res.data) {
                return res.data
            }
            return Promise.resolve(res,err)
        })
    }

    //personal_recommendations
    async getPersonalRecommendations(user_id) {
        return axios.post(API_URL + 'personal_recommendations', user_id).then((res, err) => {
            if (res.data) {
                return res.data
            }
            return Promise.resolve(res,err)
        })
    }

    //similar_user_based_recommendations
    async getSimilarUserBasedRecommendations(user_id) {
        return axios.post(API_URL + 'similar_user_based_recommendations', user_id).then((res, err) => {
            if (res.data) {
                return res.data
            }
            return Promise.resolve(res,err)
        })
    }

    //expand_recommendations
    async getExpandRecommendations(user_id) {
        return axios.post(API_URL + 'expand_recommendations', user_id).then((res, err) => {
            if (res.data) {
                return res.data
            }
            return Promise.resolve(res,err)
        })
    }

    //search_results
    async getSearchResults(data) {
        return axios.post(API_URL + 'search_results', { ...data }).then((res, err) => {
            if (res.data) {
                return res.data
            }
            return Promise.resolve(res,err)
        })
    }

    //create_new_user
    async getCreateUser(data) {
        return axios.post(API_URL + 'create_new_user', { ...data }).then((res, err) => {
            if (res.data) {
                return res.data
            }
            return Promise.resolve(res,err)
        })
    }
}
export default new Service()