#! python3
# Pegar texto de um arquivo

# Importa a biblioteca
import docx

# Funcao para o procedimento
def getDocxText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n\n'.join(fullText)