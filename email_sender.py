import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from config import ENV_FILE

load_dotenv(ENV_FILE)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
GROUP_EMAIL = os.getenv("GROUP_EMAIL")


def send_email(subject: str, body: str) -> None:
    """Sends an email to the Google Group with BCC to sender."""
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = GROUP_EMAIL
    msg["Bcc"] = SENDER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)


def send_error_email(error: str) -> None:
    """Sends an error notification email to the sender."""
    msg = MIMEText(f"<html dir='rtl'><body><h3>⚠️ שגיאה בסקריפט שליחת ברכות</h3><pre>{error}</pre></body></html>", "html")
    msg["Subject"] = "⚠️ שגיאה בסקריפט שליחת ברכות"
    msg["From"] = SENDER_EMAIL
    msg["To"] = SENDER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
