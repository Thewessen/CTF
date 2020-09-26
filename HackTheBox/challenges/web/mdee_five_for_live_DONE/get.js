const axios = require('axios');
const FormData = require('form-data');
const {md5} = require('../../../tools/md5.js');

const data = new FormData()
const reg = /\<h3 align=\'center\'\>(.*)<\/h3\>/

axios.get('http://docker.hackthebox.eu:32089/')
  .then(resp => {
    // const string = resp.data.match(reg)[1];
    // const hash = md5(string)
    data.append('hash', 'aoehusanotehae')
    console.log(data.getHeaders());
    const payload = {
      method: 'post',
      headers: data.getHeaders(),
      url: 'http://docker.hackthebox.eu:32089/',
      data,
    } 
    axios(payload)
      .then(resp => console.log(resp.data));
  });
