# redis

```
> info
...
db0:keys=4,expires=0,avg_ttl=0
> select 0
OK
> keys *
 1) "numb"
 2) "stor"
 3) "temp"
 4) "flag"
> get flag
<flag>
```
