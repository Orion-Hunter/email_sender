from pydantic import EmailStr
from typing import List


class Email:
    sender: EmailStr
    recipients: List[EmailStr]
    subject: str
    content: str

    def __init__(self, sender: EmailStr, recipients: List[EmailStr], subject: str, content: str) -> None:
        self.sender = sender
        self.recipients = recipients
        self.subject = subject
        self.content = content