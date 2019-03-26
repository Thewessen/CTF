#!/usr/bin/env sh

sshpass -p 56a9bf19c63d650ce78e6ec0354ee45e \
  ssh -l bandit32 -p 2220 bandit.labs.overthewire.org \
  -t "cd /tmp/tmp.sOrQHW1XdC; bash -l"

# level 14, 17
# ssh -i level26.private -l bandit26 -p 2220 bandit.labs.overthewire.org -t "bash -l"


