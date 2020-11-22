FROM ubuntu:20.04

# install vim & curl
RUN apt update && apt-get update && \
    apt install vim -y && \
    apt-get install curl zsh sudo wget -y

# install git & pip
RUN printf '6\n79\n' | apt install software-properties-common dirmngr gnupg-agent -y && \
    printf '\n' | add-apt-repository ppa:git-core/ppa && \
    apt update && \
    apt install git python3-pip -y

# install psql
# RUN apt update && apt install postgresql postgresql-contrib

# setting TIMEZONE
RUN apt-get install -y tzdata && dpkg-reconfigure tzdata && printf '6\n79\n' | dpkg-reconfigure tzdata

# pythonコマンドでpython3を実行できるようにシンボリックを貼る
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# install postgres command
RUN apt install postgresql postgresql-contrib -y

ADD requirements.txt .
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

WORKDIR /api

CMD ["bash"]