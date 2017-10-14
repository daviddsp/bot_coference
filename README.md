# Documentación bot

Simple bot que envía mensajes a grupos o canales dentro de Telegram usando como libreria [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Content

1. [Install](#install)
    1. [Clone Repo](#clone-repo)
    1. [Install Pip](#install-pip)
    1. [Install Virtualenv](#install-virtualenv)
        1. [Install package Virtualenv](#install-package-virtualenv)

2. [Run Bot](#run-bot)


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
Para activar el bot necesitamos enviarle 3 parametros los cuales se describen a continuación:
```bash
$ python bot.py [@nombrechannel] [token Telegram] [Minutos de pre alerta de mensajes]
Ejemplo:
$ python bot.py @notiserver 424006116:AAF6Z7jSyzjWWLas-qcR8OXBz4EZjs3JA9k 10
```
Para correr nuestro bot debemos agregarlo a un grupo o canal, de esta forma el bot tendra acceso como un invitado mas de nuestro chat, el script se encargará de enviar de forma masiva los mensajes para nuestro canal o grupo dependiendo de las horas de las conferencias que vienen desde el servicio de Graphql.

En los links de interes dejo como crear un canal y como asociarle un bot como es nuestro caso, la diferencia entre un canal o grupo es que el canal será publico o prívado y tiene información de cuantas personas han leido del mensaje.

Para agregar el bot a nuestro channel debes ir a la sección de Añadir mienbro como administrador y buscar nuestro bot para este ejemplo nuestro bot se llama @talks_bot, seleccionamos el bot y Telegram preguntará si quieres añadir el bot al canal, aceptas agregar el bot como un miembro del grupo y con esto tendremos nuestro bot listo para envíar mensajes a este canal.

### Start bot to Telegram
Para arrancar nuestro bot debes ir a la conversación con el bot y colocar el siguiente comando */start* el cual tiene toda la lógica que necesitaremos para manejar nuestro bot, con esto automaticamente el bot consultará de forma recurrente y antes de los 10 minutos que inicie la próxima charla el notificará sobre la nueva charla que se acerca, además posee un módulo para avisar cual es la charla que se esta realizando.

### Links of interest

*[Bots Telegram api](https://core.telegram.org/bots)
*[Bot father](https://telegram.me/botfather)
*[Create bot in python](https://github.com/python-telegram-bot/python-telegram-bot)
*[Create channel in Telegram](https://blog.kuku.io/document/how-to-create-a-channel-on-telegram/)






