from tkinter import *
from tkinter import ttk, scrolledtext
import asyncio
import sys
from pathlib import Path
from typing import List
from pydantic import EmailStr

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from app.config import Settings
from app.infra.async_smtp_mailer import AsyncSMTPMailerService
from app.domain.services import MailerService
from app.domain.email import Email

settings = Settings()

async def send_email(service: MailerService, email: Email) -> None:
    await service.send(email)

def callback(sender: EmailStr, to: List[EmailStr], subject: str, content: str):
    service = AsyncSMTPMailerService(settings.SMTP_HOST, settings.SMTP_PORT, settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
    asyncio.run(send_email(service=service, email=Email(
            sender=sender,
            recipients=to,
            subject=subject,
            content=content
        )))
    



root = Tk()
frm = ttk.Frame(root, height=500, width=500)
frm.grid()

author_value = StringVar()
recipients_value = StringVar()
subject_value = StringVar()
content_value = StringVar()

ttk.Label(frm, text='From: ').grid(column=0, row=0, padx=10, pady=10)
author = ttk.Entry(frm, textvariable=author_value)
author.grid(column=1, row=0, padx=10, pady=10)
author.insert(END, settings.SMTP_EMAIL_SENDER)

ttk.Label(frm, text='To: ').grid(column=0, row=1,padx=10, pady=10)
recipients = ttk.Entry(frm,textvariable=recipients_value)
recipients.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(frm, text='Subject: ').grid(column=0, row=2,padx=10, pady=10)
subject = ttk.Entry(frm, textvariable=subject_value)
subject.grid(column=1, row=2, padx=10, pady=10)

ttk.Label(frm, text='Content: ').grid(column=0, row=3,padx=10, pady=10)
content = ttk.Entry(frm, textvariable=content_value)
content.grid(column=1, row=3, padx=10, pady=10, ipady=20)

button = ttk.Button(frm, text="Enviar", command=lambda: callback(author_value.get(), recipients_value.get().split(','), subject_value.get(), content_value.get()))
button.grid(column=1, row=4, padx=10, pady=10)

root.mainloop()

