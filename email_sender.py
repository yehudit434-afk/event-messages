import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from config import ENV_FILE
from constants import ERROR_EMAIL_SUBJECT, ERROR_EMAIL_BODY

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
    msg = MIMEText(ERROR_EMAIL_BODY.format(error=error), "html")
    msg["Subject"] = ERROR_EMAIL_SUBJECT
    msg["From"] = SENDER_EMAIL
    msg["To"] = SENDER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
