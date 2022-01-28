#!/bin/bash

PASS=`echo $RANDOM | md5sum | head -c 20`

# docker run -d \
#  --name x11-bridge \
#  -e MODE="tcp" \
#  -e XPRA_HTML="yes" \
#  -e DISPLAY=:14 \
#  -e XPRA_PASSWORD=$PASS \
#  --net=host \
#  jare/x11-bridge

# docker run \
#        --rm \
#        --name textgen-emacs \
#        -v $(pwd):/home/rstudio/work \
#        --volumes-from x11-bridge \
#        -e DISPLAY=:14 \
#        -t textgen emacs

docker rm x11-bridge
docker run -d \
       --name x11-bridge \
       -e MODE="ssh" \
       -v ~/.ssh/id_rsa.pub:/etc/pub-keys/me.pub \
       -e DISPLAY=:14 \
       --net=host \
       jare/x11-bridge

docker run -d \
       --rm \
       --name textgen-emacs \
       --volumes-from x11-bridge \
       -v $(pwd):/home/rstudio/work \
       -e DISPLAY=:14 \
       -it textgen emacs

# echo Password is
# echo $PASS
xpra attach --encoding=rgb --ssh="ssh -o StrictHostKeyChecking=no -p 22" ssh:xpra@localhost:14
