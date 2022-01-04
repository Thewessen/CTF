# Getting info from samba share

- check if the server is running smb ports (`nmap -A -p- <ip>`)
- check the name of the shares using enum4linux (`enum4linux -A <ip>`)
- try misconfig of smbserver by login in as Anonymous user without providing a password
  (`smbclient //<ip>/<share-name> -U Anonymous`)
- use cmds like: ls, cd and mget
  TODO: I couldn't find a way to `cat` a file while logged in. `mget`
  (download) and cat locally worked.

_for this specific learning path_
- download the ssh private key
- connect through ssh using `ssh -i <key> cactus@<ip>`
- `cat smb.txt`
