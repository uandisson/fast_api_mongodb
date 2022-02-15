# FastApi and MongoDB
CRUD with FastAPI and MongoDB

## Requisitos

- Python >=3.8
- [FastApi](https://fastapi.tiangolo.com/?target="_blank) 
- Docker

## 1 - Clone Repositorio:

    $ git clone https://github.com/uandisson/fast_api_mongodb.git
     
## 2 - Buildar o Projeto se quiser !

    $ cd fast_api_mongodb/
    $ sudo docker-compose build

    Caso der erro:

      $ docker-compose build
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.

    Instalando Composer:

    0 - sudo service docker status
    
    1 - sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    2 - sudo chmod +x /usr/local/bin/docker-compose
    3 - docker-compose --version

    Instalando Docker:

    1 - sudo apt-get update -y
    2 - sudo apt-get install -y linux-image-generic-lts-trusty linux-headers-generic-lts-trusty
    3 - sudo apt-get install -y xserver-xorg-lts-trusty libgl1-mesa-glx-lts-trusty
    4 - sudo reboot
    5 - sudo apt-get purge -y lxc-docker* && sudo apt-get -y purge docker.io*
    6 - sudo apt-get update -y && sudo apt-get install -y apt-transport-https ca-certificates
    7 - sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
    8 - sudo apt-get update -y
    9 - sudo apt-cache policy docker-engine 
    10 - sudo apt-get update -y && sudo apt-get install -y linux-image-extra-$(uname -r)
    11 - sudo apt-get install docker-engine -y
    12 - sudo service docker start   
    13 - sudo docker run hello-world
    14 - docker -v
     
## 3 - Iniciar e Debugar

    $ cd fast_api_mongodb/
    $ sudo docker-compose up

## 4 - URL -> : http://127.0.0.1:8000/docs
