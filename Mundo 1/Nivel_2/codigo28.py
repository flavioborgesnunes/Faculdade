#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python se der errado foda-se pq já é quase meia noite CARAIO"

#parâmetros
senha = ""
msg['From'] = "flavioborgesnunes@gmail.com"
msg['To'] = "custodio.patricia@gmail.com"
msg['Subject'] = "Python"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')


