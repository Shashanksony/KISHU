import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(to_address, subject, body, attachment_path):
    from_address = "your_email@example.com"
    password = "your_password"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    attachment = open(attachment_path, "rb")

    # Instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())

    # Encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")

    # Attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # Create server
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()

    # Login Credentials for sending the mail
    server.login(from_address, password)

    # Convert the Multipart msg into a string
    text = msg.as_string()

    # Send the mail
    server.sendmail(from_address, to_address, text)
    server.quit()

if __name__ == "__main__":
    send_email("recipient@example.com", "Subject", "Email body", "/path/to/attachment")
