from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# E-Mail Einstellungen
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "homehelp.sender@gmail.com"
EMAIL_PASSWORD = "dhbvjrguugqelgzj"  # <-- App-Passwort hier einfügen

@app.route("/")
def home():
    return render_template("index.html", site_name="HOMEHELP")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")

    email_body = f"""Neue Nachricht von HOMEHELP:

Name: {name}
Telefon: {phone}
Nachricht:
{message}
"""

    msg = MIMEText(email_body)
    msg["Subject"] = "Neue Anfrage über HOMEHELP"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        server.quit()
        return render_template("success.html", name=name)
    except Exception as e:
        return f"<h2>Fehler beim Versenden: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

