# Test Tickets System

This is a ticket system. Customers place support tickets and support agents can process, respond and solve those tickets.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Those steps are done in ubuntu 14.04, you have to adapt it to your OS.

### Prerequisites

python3.x
python-pip
virtualenv

### Installing

Creating new enviroment

```
sudo virtualenv -p /opt/env_test_tickets
```

Installing packages

```
source /opt/env_test_tickets/bin/activate
sudo pip install -r requirements.txt
```

## Using the application

To start the server run this command from project root folder /TicketSystem

```
python manage.py runserver
```

First access to a custormer portal, and create tickets

http://localhost:8000/
user: customer1 or customer2
pass: pass1234

Then access to a support agent portal, and answer some tickets

http://localhost:8000/agent/
user: agent1 or agent2
pass: pass1234

You can continue replying as a customer or answering as agent, until one of then decides to close the ticket

Finally you can access to the administration backend to manage user and some information

http://localhost:8000/admin/
user: admin
pass: pass1234

## Built With

* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
* [DRF](http://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.

## Authors

* **Jesus Steer** - *Initial work* - [jsteerv](https://github.com/jsteerv)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
