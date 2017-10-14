# Documentación bot

Simple bot que envía mensajes a grupos o canales dentro de Telegram usando como libreria [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Content

1. [Install](#install)
    1. [Clone Repo](#clone-repo)
    1. [Install Pip](#install-pip)
    1. [Install Virtualenv](#install-virtualenv)
        1. [Install package Virtualenv](#install-package-virtualenv)
    1. [Run Bot](#run-bot)    
2. [Basico Usage](#basic-usage)


## Install

### Clone Repo

```bash
$ git clone https://github.com/daviddsp/bot_coference
```

### Install Pip

En caso de usar sistema operativo como Debian/Ubuntu o macOS seguir los siguientes pasos:

```bash
$ apt-get update
```
Instalación de PIP
```bash
$ apt-get -y install python-pip
```
Comprobación de la instalación 
```bash
$ pip --help
```
Verificación de la versión
```bash
$ pip -V
```

En caso de utilizar Windows seguir el siguiente [tutorial](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)


### Install Virtualenv

Para este bot necesitaremos tener un virtualenv instalado en nuestro OS para instalar todas las dependencias necesarias para correr nuestro bot.

```bash
$ sudo pip install virtualenv 
```
Luego nos movemos a nuestro directorio del bot con el siguiente comando válido para Linux o macOS
```bash
$ cd bot_coference
```
Dentro de nuestro directorio debemos crear nuestro virtualenv
```bash
$ virtualenv env_bot
```
Activar env
```bash
$ source env_bot/bin/activate 
```
Para desactivar (No necesario)
```bash
$ deactivate
```
#### Install package Virtualenv
```bash
$ pip install -r requirements.txt
```

### Run bot
```bash
$ python bot.py
```




