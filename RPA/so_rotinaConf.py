"""
#Simulação de rotina de conferência diária de arquivos!
#Python DS
#Tutorial para uso do código: https://youtu.be/meMV1fed0PM
"""
#Importação de bibliotecas
#============================
import os, glob, datetime, shutil
#BIBLIOTECAS DE TRABALHO COM SISTEMA OPERACIONAL


#Preparação do ambiente
#============================
"""
CUIDADOS IMPORTANTES:
1. Inscrição no canal Python DS
2. Curtir o vídeo
3. Ativar as notificações
:-)
"""
#Definição do diretório
caminho = r'D:\Python\so\subdir'
os.chdir(caminho)

print(f'Analisando diretório: "{caminho}"')
print('='*60)

#Definição da data de execução
hoje = datetime.datetime.now()
#Captura apenas a data em formato string
hoje = str(hoje)[:10]


#Rotina de conferência
#============================
#Uso da data para criação de diretórios personalizados
conferidos = 'conf_'+hoje #Um novo diretório para cada dia



#Análise do conteúdo do diretório original
tipos = '*.txt' #Extensão dos arquivos desejados
arquivos = glob.glob(tipos) #Procura arquivos no diretório atual

print('='*60)

print('Conteúdo do diretório:')
for arquivo in arquivos:
    print(arquivo)

print('='*60)    

#Criação de um diretório (diário) para conferência
#Verifica se o diretório novo já existe
if os.path.exists(conferidos):
    print('Diretório de conferência já existe')
else:
    print('Diretório inexistente. Criando...')
    #CRIA O DIRETÓRIO NOVO, SE ELE NÃO EXISTIR
    os.mkdir(conferidos) 

print('='*60)


#ESTA ETAPA SIMULA A CONFERÊNCIA
#Cópia dos arquivos ORIGINAIS
"""
Para cada arquivo na pasta
    * Copia o arquivo com um novo nome
    * Insere uma linha adicional confirmando a conferência
"""
for k in range(0, len(arquivos)):
    #Novo nome => Nome original + conf + data atual
    novoNome = arquivos[k][:-4]+'_conf_'+hoje+'.txt'
    shutil.copy(arquivos[k], f'{conferidos}\{novoNome}')

    #Adição de conteúdo aos arquivos copiados (CONFERÊNCIA)
    with open(f'{conferidos}\{novoNome}', 'a') as file:
        #Adiciona uma linha ao final do arquivo
        file.write(f'\nConferido em: {hoje}')

print('Análise concluída!')
print('='*60)
