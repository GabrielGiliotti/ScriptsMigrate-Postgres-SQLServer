import logging
import logging.handlers
import os


# diretorio onde esta rodando o script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# os.path.dirname() - retorna string indicando caminho ate arquivo um especificado
#                   - Se passado "C:/Users/gabriel/Desktop/Tarefas", Tarefas é considerado o arquivo e o caminho
#                   - retornado sera ""C:/Users/gabriel/Desktop"

# os.path.abspath() - retorna string ate arquivo de forma absoluta e normalizada
#                   - Se passado "C:/Users/gabriel/Desktop/Tarefas", Tarefas é considerado o arquivo e o caminho
#                   - retornado sera ""C:\Users\gabriel\Desktop\Tarefas"

# __file__          - retorna o caminho para esse arquivo (logreport.py).


LOG_FILE = os.path.join(SCRIPT_DIR, u"integracao_onlinee.log")
# os.path.dirname() - Parametro 1: Path onde queremos criar um arquivo
#                   - Parametro 2: String para criar um arquivo com nome especificado atraves de uma string
#                                  (Para criar um tipo especifico de arquivo, passe o tipo junto ao nome desejado)


# nivel de log
log_level = logging.NOTSET
# Podemos setar logging em diferentes leveis, onde cada um dos leveis é representado por um valor numerico:
# CRITICAL - 50 --> logging.CRITICAL
# ERROR    - 40 --> logging.ERROR
# WARNING  - 30 --> logging.WARNING
# INFO     - 20 --> logging.INFO
# DEBUG    - 10 --> logging.DEBUG
# NOTSET   - 0  --> logging.NOTSET


fmt_template = '%(asctime)s [%(levelname)s] %(message)s .'
# Os 4 parametros que encontrei para fazer o template são:

# %(asctime)s    -  Pega o datetime do logging para informar na saida
# %(levelname)s  -  Pega o nome do level do logging a ser executado (ERROR, DEBUG, WARNING)
# %(message)s    -  Pega a menssagem passada para o logging, de acordo com o level
# %(name)s       -  Pega o nome do logging (Na documentação esta logging channel) Test: retornou o caminho do arquivo .log
# %(lineno)d     -  No caso de varios loggings serem chamados no arquivo, ajuda itendificar onde esta o problema
#                -  informando o numero da linha

# Formato da saida no log:
# 2003-07-08 16:49:45 [ERROR] Erro nos dados da chamada ...

# Prepare log infra-structure
logger = logging.getLogger(LOG_FILE)  # retorna o arquivo .log onde devem ser inseridas as mensagens de log

log_handler = logging.handlers.RotatingFileHandler(logger.name, maxBytes=20000, backupCount=3)
# Parametro 1: logger.name - Arquivo onde o log sera escrito
# Parametro 2: maxBytes    - Define o tamanho maximo que o arquivo de log pode alcancar ate criar outro arquivo
# Parametro 3: backupCount - Define quantos arquivos de log podem ser criados ao se alcançar o limite
# OBS: Os parametros 2 e 3 devem ser definidos juntos, caso contrario, será ignorado e criado apenas um arquivo sem limite

log_handler.setFormatter(logging.Formatter(fmt_template, datefmt='%d/%m/%Y %H:%M:%S'))
# logging.Formatter() - Deve funcionar como um parse para que serFormatter possa ler o formato especificado (fmt_template)
# setFormatter() - Informa para o handler utilizar o formato fmt_template (definido acima, mas pode ser definido diretamente aqui)
# e passa o formato do date time (O ultimo parametro, se nao informado, faz com que no log apareça ate os milisegundos)

log_handler.setLevel(log_level)
# setLevel() Faz com que o handler receba o level ERROR definido. Qualquer log de menor level é ignorado
# Setei para NOTSET, assim qualquer nivel de log pode ser pego

logger.addHandler(log_handler)
# Apos setados alguns do parametros do log_handler, adicionamos o log_handler (com o conteudo setado) no logger

logger.setLevel(log_level)
# Apos setados alguns do parametros do log_level, adicionamos o log_level (com o conteudo setado) no logger

logger.propagate = False
# propagate = true permite passar o handler para leveis maiores de handlers. (Não sei o efeito ou uso disso)
# caso necessario, procurar exemplos

# exemplo de utilizacao
# logger.debug("Erro na config ...")