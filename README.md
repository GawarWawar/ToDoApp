
# RenovateHub_project

  

# 1. Task manager
### Functional requirements
- [x] Being able to create/update/delete projects - Fully functional, but with 1 bug that I couldn't fix. When task in the middle deleted, it doesn't update its task automatically
- [x] Being able to create/update/delete tasks to projects - 100%
- [ ] Being able to prioritize tasks into a project - Add button to drag tasks, but it does not have functionality
- [ ] Being able to choose deadline for my task - Tasks and Projects has deadline, but they do not have any effect on behavior
- [x] being able to mark a task as 'done'
### Technical requirements
- [x] It works as WEB application on Python 3.12 & Django v5.1 - 100%
- [x] Docker-compose for running application - This step is ready, however can not add superuser through docker.
- [x] For the client side  HTML, CSS (Bootstrap v5), JavaScript (Alpine.js)
- [x] It should be responsible for desktop and mobile (use Bootstrap Grid system) - Grid is a little bit different, but it is still comfortable to use it on mobile
- [x] It should have a client side and server side validation - Client side is a little bit on weak side, but server side is doing its work good :D
- [x] It should look like on screens (see attached screenshot below) - Made as close, as possible
### Additional notes
- [x] It works like one-page WEB application and uses AJAX technology with, load and submit data without reloading a page 

- [x] It should have user authentication solution and a user should only have access to their own projects and tasks. (use `django-allauth` here) - Pages use standard set up, but users can sing up and sign in

- [ ] It does not have automated tests for the all functionality

- [x] Usage of linters (at least `ruff`)

### To start the project, 2 ways could be used:
- 1st: Docker:
  - `> docker-compose up --build`
  - After that site will be ready to use
- 2nd: Using python:
  - Clone git from https://github.com/GawarWawar/RenovateHub_project
  - `python -m venv env` - to create virtual environment;
  - `source/evn/bin/activate` - to activate virtual environment;
  - `cd django_instance` - get into working directory;
  - `python -m pip install -r requirements.txt` - install dependencies;
  - `python manage.py migrate`- populate database;
  - `python manage.py collectstatic`- collect needed static files;
  - ` python manage.py createsuperuser`- create superuser to manage admin;
  - `python manage.py runserver 0:0:0:0:8000`- use site on 127.0.0.1:8000 or your local IP.

# 2. SQL task:
sql_exercice contains database with mock files and .sql file with all the scripts