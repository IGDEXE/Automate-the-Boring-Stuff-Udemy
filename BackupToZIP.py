#! python3
# Salva todo o conteudo da pasta em um ZIP

# Importa as bibliotecas necessarias
import zipfile, os

# Funcao para fazer o procedimento
def backupToZip(folder):
    folder = os.path.abspath(folder) # Pega o caminho absoluto da pasta

    # Cria um nome unico
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Cria o arquivo ZIP
    print('Criando %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Verifica todos os arquivos e subpastas
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adicionando arquivos %s...' % (foldername))
        # Adiciona a pasta atual ao ZIP
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        # Adiciona todos os arquivos nessa pasta no ZIP
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # Nao faz backup dos arquivos de Backup
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Concluido.')

# Exemplo de uso:
backupToZip('C:\\INFRA') # Chama a funcao e passa de parametro uma pasta
