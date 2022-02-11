#!/bin/bash

docker run \
       --rm \
       --name textgen-emacs \
       -v $(pwd):/home/rstudio/work \
       -it textgen emacs
