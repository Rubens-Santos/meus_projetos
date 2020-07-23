import pyqrcode as pqr #Bilioteca para gerar o QRcode.
import png #Para gerar o png (Imagem do QRcode)
import io

urlcode = pqr.create('https://github.com/Rubens-Santos') # O que vai ser exibido pelo Code.

#criando a imagem no seu computador

with open('code1.png', 'w') as fstream:
    urlcode.png('code1.png', scale=5)
urlcode.png('code1.png', scale=5)
buffer = io.BytesIO()
urlcode.png(buffer)
print(list(buffer.getvalue()))