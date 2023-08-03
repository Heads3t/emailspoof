import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    try:
        # Create a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure SSL/TLS connection
        server.login(smtp_username, smtp_password)  # Login to the SMTP server

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add the email body
        message.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close the connection to the SMTP server
        server.quit()

        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    smtp_server = ""
    smtp_port = 587
    smtp_username = ""
    smtp_password = ""

    # Prompt the user for sender email, recipient email, subject, and message
    sender_email = input("Enter sender email: ")
    recipient_email = input("Enter recipient email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    # Call the send_email function to send the email
    send_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password)
