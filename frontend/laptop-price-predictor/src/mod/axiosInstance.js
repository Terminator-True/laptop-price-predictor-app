import axios from "axios";


const instance = axios.create({
    baseURL: "127.0.0.1:5000",
    timeout: 5000,

});


export default instance;