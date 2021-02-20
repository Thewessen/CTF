# PHP-console

Cookie should be presented in get-request:

```
curl -H 'Cookie: php-console-server=5; php-console-client=eyJwaHAtY29uc29sZS1jbGllbnQiOjV9' <url>
```

To authorize the console:

```
curl 'http://178.128.40.63:31384/' \
  -H 'DNT: 1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36' \
  --compressed
```
