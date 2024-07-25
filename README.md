![Screenshot_4](https://user-images.githubusercontent.com/21342727/197424567-5cc16a1c-ad82-4ff9-9871-fcd185a74978.png)

 
Iae pessoal esse projeto foi desenvolvido para um processo seletivo para uma empresa, e eles me passaram esse desafio de construir um script de backup, e me deram a liberdade de construir com liguem que eu quiser, eu que não sou bobo nem nada, fui logo de `Python`🐍


**Esse projeto é o seguite, é um servidor centralizado de backup, o qual recebe arquivos de todos os demais servidores, move os dados para um volume temporário, para que deste volume os dados sejam copiados por uma ferramenta de backup externa. Escrever um script, para automatizar as seguintes ações:**

+ Listar todos arquivos (nome, tamanho, data de criação, data da última modificação) localizados no caminho /home/valcann/backupsFrom;
+ Salvar o resultado no arquivo backupsFrom.log em /home/valcann/;
+ Remover todos os arquivos com data de criação superior a 3 (três) dias;
+ Copiar todos os arquivos os arquivos com data de criação menor ou igual a 3 (três) dias em homevalcann/backupsTo;
+ Salvar o resultado no arquivo backupsTo.log em /home/valcann/.

> Se você usa Windows recomendo usar o 🗂**BulkFileChanger** para alterar as datas dos arquivos e assim você conseguir observar que o script funcionar. 


▶️Vou mostrar como construir esse script, bora lá 👨‍💻

Primeiro passei os `imports` para esse projeto, e passei as variáveis com os caminhos das pastas, **presta atenção se você vai usar esse projeto, altere para os diretórios das suas pastas que vai usar**. 
~~~Python

import os,time,glob
import logging, shutil

# Criação dos caminho para consutar e mover os arquivos (Observação colocar o seu diretorio da sua maquina).
path = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsFrom/*.*"
pathremove = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsFrom"
mover = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsTo"
~~~


Em seguida fiz a criação dos logs que vai criar um arquivo `backupsFrom.log` na pasta `valcann` para mostrar as informação de quando roteador o script.

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


Depois criei duas função para listar um vai verificar o tempo do arquivo, verificando a última modificação e quando foi criada, e a outra mostar o tamanho do arquivo em megabytes.
~~~Python
# Função da verificação do tempo do arquivo
def info_tempo(in_tempo):
    print("Útima modificação: %s" % time.ctime(os.path.getmtime(in_tempo)))
    print("Criado: %s" % time.ctime(os.path.getctime(in_tempo)))

# Função da verificação do tamanho do arquivo
def info_tamanho(in_tamanho):
    tamanho = os.stat(in_tamanho)
    print("Tamanho do arquivio :", (round (tamanho.st_size / (1024*1024),3)),"Mb")
~~~


Aqui é a magia do script onde criei `duas array` para ser percorrida dentro do `for` fazer as condicionais de remover todos os arquivos com data de criação superior a 3 dias.
~~~Python
# Metodo para apagar os arquivos com data de criação superior a 3 dias
now = time.time()
antigo = []
novo = []
for f in os.listdir(pathremove):
    fn = os.path.join(pathremove, f)
    mtime = os.stat(fn).st_mtime
    if mtime > now - 1 * 86400:
        novo.append(fn)
    elif mtime < now - 3 * 86400:
        antigo.append(fn)
if novo:
    for fn in antigo:
        os.remove(fn)

~~~

E por fim passo as informação no terminal, e copiar todos os arquivos com data de criação menor ou igual a 3 dias.
~~~Python 
# Percorre os arquivos para ter a informação no terminal
for info_arquivos  in glob.glob(path):
    print("Nome do arquivo: ", os.path.basename(info_arquivos ))
    info_tempo(info_arquivos)
    info_tamanho(info_arquivos)
    print("\n")

# percorre os arquivos para mover para pasta de backup
files = os.listdir(pathremove)
for file in files:
    new_path = shutil.copy(f"{pathremove}/{file}", mover)
    print("Arquivos movidos para: ", new_path)
~~~



