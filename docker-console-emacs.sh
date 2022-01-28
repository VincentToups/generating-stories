#!/bin/bash

docker run \
       --rm \
       --gpus device=GPU-60f0b2bf-caf9-a427-0f4f-b50165a07d72\
       --name textgen-emacs \
       -v $(pwd):/home/rstudio/work \
       -it textgen emacs
