import os,time,glob
import logging, shutil

# Criação dos caminho para consutar e mover os arquivos (Observação colocar o seu diretorio da sua maquina).
path = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsFrom/*.*"
pathremove = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsFrom"
mover = "C:\\Users\\Desenvolvimento\\Desktop\\home\\backupsTo"

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

# Função da verificação do tempo do arquivo
def info_tempo(in_tempo):
    print("Útima modificação: %s" % time.ctime(os.path.getmtime(in_tempo)))
    print("Criado: %s" % time.ctime(os.path.getctime(in_tempo)))

# Função da verificação do tamanho do arquivo
def info_tamanho(in_tamanho):
    tamanho = os.stat(in_tamanho)
    print("Tamanho do arquivio :", (round (tamanho.st_size / (1024*1024),3)),"Mb")

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




































