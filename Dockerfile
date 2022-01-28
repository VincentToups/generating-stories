FROM rocker/verse
RUN apt update && apt install -y python3-pip
RUN pip3 install happytransformer
RUN apt update && apt install -y emacs
RUN pip3 install jupyter jupyterlab
RUN apt update && apt install openssh-server sudo -y
RUN mkdir /home/rstudio/.ssh
RUN pip3 install pandas dfply beautifulsoup4
COPY docker-key.pub /home/rstudio/.ssh/
USER rstudio
CMD jupyter lab --port 8787 --ip 0.0.0.0 
