# Email Sender
## Practice with Async Tasks, SMTP Servers 


### Description

The objective of this project is to demonstrate in a practical way how the flow of a project with Clean Architecture works, as well as a way to use the SMTP (Simple Mail Transfer Protocol) protocol for sending emails.

It is important to point out that with this project I do not intend to theoretically delve into any of the concepts presented, just to demonstrate their application. Subsequently, new projects will bring greater theoretical rigor. It is also worth mentioning that the project is not yet fully adapted to the principles of the concepts used for its development.

## Features

- Creating a service to send emails via SMTP asynchronously

## Tech

- [Docker](https://docs.docker.com/) - Container Management
- [Python 3.10](https://www.python.org/) - Programming language
- [Poetry](https://python-poetry.org/) - Python Packaging and Dependency Management
- [Pydantic](https://docs.pydantic.dev/) - Data validation and settings management 
- [aiosmtplib](https://pypi.org/project/aiosmtplib/) -  asynchronous SMTP client 
- [Visual Studio Code](https://code.visualstudio.com/) - Integrated Development Env
- [MailHog](https://github.com/mailhog/MailHog) - Web and API based SMTP testing

## Instructions to test

Use the file .env.example as model to create your .env file. Set values in the variables as follow format:
```
SMTP_EMAIL_SENDER="developer@gmail.com"
SMTP_HOST=localhost
SMTP_PORT=1025
SMTP_USERNAME=
SMTP_PASSWORD=
```

If you want, you can use the [Google SMTP Server](https://support.google.com/a/answer/176600?hl=en). In this case, you should
set values to variables ``` SMTP_USERNAME ``` and ``` SMTP_PASSWORD ```.

Once you have installed Python, Poetry and Docker, run the follow commands in the project root:

- To create Mailhog Container.

``` 
docker compose up 
```

- To add python dependencies and create virtual environment.

```
poetry install
```

Once the commands have generated the expected result, run:

- To activate Python Virtual Environment.
```
poetry shell
```

- To run project.
```
python app/main.py
```

## Next Steps

The next steps of this project still being considering. But i have some ideas like:

- Add Login System
- Add CRUD of Entities and send emails to set a password to login in system
- Add OutBox Pattern to control multiple email sending

