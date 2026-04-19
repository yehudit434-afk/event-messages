import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "yehudit434@gmail.com"
APP_PASSWORD = "pujd ygfv ieiy xrpn"
GROUP_EMAIL = "omesi-family@googlegroups.com"

msg = MIMEText("כאן תכתבי את תוכן ההודעה")
msg["Subject"] = "נושא ההודעה"
msg["From"] = SENDER_EMAIL
msg["To"] = GROUP_EMAIL
msg["Bcc"] = SENDER_EMAIL

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    print("ההודעה נשלחה בהצלחה!")
