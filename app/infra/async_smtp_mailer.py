from email.message import EmailMessage
from pydantic import EmailStr
from typing import Optional, Any
import aiosmtplib
from app.domain.services import MailerService
from app.domain.email import Email


class AsyncSMTPMailerService(MailerService):
    def __init__(
        self,
        smtp_host: str,
        smtp_port: int,
        smtp_username: Optional[str],
        smtp_password: Optional[str],
    ) -> None:
        self._smtp_host = smtp_host
        self._smtp_port = smtp_port
        self._smtp_username = smtp_username
        self._smtp_password = smtp_password

    async def send(self, email: Email) -> None:
        message: EmailMessage = self.__build_message(email)
        await self.__send(message)

    def __build_message(self, email: Email) -> EmailMessage:
        message = EmailMessage()
        message["From"] = email.sender
        message["Subject"] = email.subject
        message["To"] = ", ".join(email.recipients)
        message.add_header("Content-Type", "text/html")
        message.set_payload(email.content, charset="utf-8")
        return message

    async def __send(self, message: EmailMessage) -> Any:
        await aiosmtplib.send(
            message,
            hostname=self._smtp_host,
            port=self._smtp_port,
            username=self._smtp_username,
            password=self._smtp_password,
        )
