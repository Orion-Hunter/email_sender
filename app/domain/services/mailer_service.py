from abc import ABC, abstractmethod
from ..email import Email


class MailerService(ABC):
    @abstractmethod
    async def send(self, email: Email) -> None:
        ...
