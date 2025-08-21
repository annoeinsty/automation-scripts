import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    msg = MIMEText(message)
    msg["Subject"] = "System Alert"
    msg["From"] = "alert@system.com"
    msg["To"] = "admin@system.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email", "your_password")
        server.sendmail(msg["From"], msg["To"], msg.as_string())

if __name__ == "__main__":
    send_alert("Critical Error Detected in System!")
