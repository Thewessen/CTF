#!/usr/bin/env sh

sshpass -p c9c3199ddf4121b10cf581a98d51caee \
  ssh -l bandit33 -p 2220 bandit.labs.overthewire.org \
  -t "cd /tmp/tmp.sOrQHW1XdC; bash -l"

# level 14, 17
# ssh -i level26.private -l bandit26 -p 2220 bandit.labs.overthewire.org -t "bash -l"


