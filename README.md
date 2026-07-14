# Todo Task Manager API

A simple task management backend built with Django and Django REST Framework.

## Services

- **users** — user profiles, authentication (token-based login)
- **tasks** — CRUD for tasks (title, status, priority, due date, assignment)
- **notifications** — logs of notifications sent for task events

## Tech Stack

See `requirements.txt` for exact pinned versions.

- Django
- Django REST Framework
- SQLite (default dev database)

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpoints

- `POST /api/users/login/` — obtain auth token
- `GET /api/users/profile/` — current user's profile
- `GET/POST /api/tasks/` — list/create tasks
- `GET/PUT/DELETE /api/tasks/<id>/` — retrieve/update/delete a task
- `GET /api/notifications/` — list notification logs
