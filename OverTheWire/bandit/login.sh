#!/usr/bin/env sh

sshpass -p 5b90576bedb2cc04c86a9e924ce42faf \
  ssh -l bandit30 -p 2220 bandit.labs.overthewire.org \
  -t "cd /tmp/tmp.sOrQHW1XdC; bash -l"

# level 14, 17
# ssh -i level26.private -l bandit26 -p 2220 bandit.labs.overthewire.org -t "bash -l"


