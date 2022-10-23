# Projeto Backup com python
 
Iae pessoal esse projeto foi desenvolvido para um processo seletivo para uma empresa, e eles me passaram esse desafio de construir um script de backup, e me deram a liberdade de construir com liguem que eu quiser, eu que não sou bobo nem nada, fui logo de `Python`🐍

Vou mostrar como construir esse script, bora lá 👨‍💻

Primeiro passei os `importes` para esse projeto, e passei as variáveis com os caminhos das pastas, **presta atenção se você vai usar esse projeto, altere para o diretório das suas pastas**.
~~~Python

import os,time,glob
import logging, shutil

# Criação dos caminho para consutar e mover os arquivos (Observação colocar o seu diretorio da sua maquina).
path = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsFrom/*.*"
pathremove = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsFrom"
mover = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsTo"

~~~


Em seguida fiz a criação dos logs que vai criar o arquivo `backupsFrom.log` na pasta `valcann`

~~~Python
# Criação dos logs
logging.basicConfig(
    filename=".\\valcann\\backupsFrom.log",
    level=logging.DEBUG,
    format="%(asctime)s :: %(filename)s :: %(levelname)s  :: %(lineno)d :: %(message)s",
    filemode='a'
)

# As informação que são gerados para o arquivo de log
logging.info("Informação do tamanho do arquivo ")
logging.info("Útima modificação do arquivo")
logging.debug("Removendo todos os arquivos com data de criação superior a 3 dias")
logging.info("Gero copia dos arquivos para backupsTo")
~~~
