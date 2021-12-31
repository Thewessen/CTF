# Exploiting an SMB-server

- smb-server is misconfigured, allowing user 'Anonymous' login
- _nmap_ allows us to see the protocol (smb)
- _enum4linux_, scan smb servers for users, workgroups and more
- _smbclient_, for connecting to a smbserver (get a file with `mget`)
- connect with (no password): `smbclient //[ip]/[share] -U Anonymous -p [port]`
- get any file with `mget` (e.g. .ssh/id_rsa)
- connect again ussing ssh (username jcactus)
