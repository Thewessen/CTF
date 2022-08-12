to list:
- `smbclient -L <ip-address>`

to connect:
- `smbclient //<ip-address>/<workspace>`
_(mind the forward slashes)_

To get multiple files at once:
```
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
```
