import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp-relay.brevo.com"
login = "a6cfe1001@smtp-brevo.com"
# Satır 7'yi şu şekilde güncelleyin:
SMTP_KEY = "BURAYA_ANAHTARINIZI_GELECEK"
sender_email = "mertmertkil@gmail.com"
receiver_email = "karef64382@flownue.com"

text = "merhaba bu eposta python ile gönderildi"
message = MIMEText(text, "plain")
message["Subject"] = "merhaba"
message["From"] = sender_email
message["To"] = receiver_email

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("E-posta başarıyla gönderildi.")
