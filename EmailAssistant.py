import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailAssistant:
    def __init__(self):
        # Predefined mailing list
        self.Mailing = {
            '"cat"': "sakleonel51@gmail.com",
            '"shadab"': "sakn501@gmail.com",
            '"baller"': "salahuddinakhtar1@gmail.com",
            "vinay": "vinaybagra2002@gmail.com"
        }

    def send_email(self, to_address, subject, body, from_address="youremail@example.com", password="yourpassword"):
        """
        Sends an email to the specified address with the given subject and body.
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Set up the server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, password)

            # Send the email
            server.send_message(msg)
            server.quit()

            print(f"Email sent to {to_address}")

        except Exception as e:
            print(f"Failed to send email to {to_address}: {e}")

    def get_contact_email(self, contact_name):
        """
        Returns the email address for a given contact name.
        """
        return self.Mailing.get(contact_name, None)

# Example usage:
if __name__ == "__main__":
    email_assistant = EmailAssistant()

    # Example: Get a contact's email
    contact_email = email_assistant.get_contact_email('"shadab"')
    if contact_email:
        print(f"Contact email for 'shadab': {contact_email}")

    # Example: Send an email
    email_assistant.send_email(
        to_address="recipient@example.com",
        subject="Test Email",
        body="This is a test email from your AI assistant.",
        from_address="youremail@example.com",
        password="yourpassword"
    )
