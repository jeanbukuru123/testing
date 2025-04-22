import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email account credentials
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"

# List of recipients
recipients = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]

# Email content
subject = "Hello from Python!"
body_template = "Hi {name},\n\nThis is an automated email sent from a Python script.\n\nCheers,\nYour Name"

# Create SMTP session
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

# Send email to each recipient
for person in recipients:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = person["email"]
    msg["Subject"] = subject

    body = body_template.format(name=person["name"])
    msg.attach(MIMEText(body, "plain"))

    server.send_message(msg)
    print(f"Email sent to {person['name']} at {person['email']}")

server.quit()
