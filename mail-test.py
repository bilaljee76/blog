from app import app
from email_utils import send_email

with app.app_context():
    send_email(
        to="bilal.networking@gmail.com",
        subject="Welcome",
        template="email/welcome",
        name="Bilal"
    )