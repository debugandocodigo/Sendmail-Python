import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP do Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Porta para conexão TLS

# Conta de e-mail
email_user = "seuemail@gmail.com"  # Substituir pelo seu e-mail
email_password = "suasenha"  # Substituir pela sua senha

# Destinatário
to_email = "emaldestino@email.com"  # Substituir pelo e-mail do destinatário

# Criar mensagem de e-mail
subject = "Email enviado usando Python"
body = "Esse é um e-mail enviado usando Python"

msg = MIMEMultipart()  # Cria uma instância da classe MIMEMultipart
msg["From"] = email_user  # Configura o remetente
msg["To"] = to_email  # Configura o destinatário
msg["Subject"] = subject  # Configura o assunto

msg.attach(MIMEText(body, "plain"))  # Adiciona o corpo da mensagem ao objeto MIMEMultipart

# Conectar-se ao servidor SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Iniciar conexão TLS (Transport Layer Security)
    server.starttls()

    # Fazer login na conta
    server.login(email_user, email_password)

    # Enviar e-mail
    server.sendmail(email_user, to_email, msg.as_string())

print("E-mail enviado com sucesso.")
