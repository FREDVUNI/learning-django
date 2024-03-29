# Django Learning Repository

## Overview

This repository serves as a learning project, containing various Django apps. Each app focuses on different aspects, providing examples and exercises for understanding Django concepts.

## Apps

### 1. admin/

- Basic Django admin app showcasing administrative functionalities.

### 2. guest/

- A guest app demonstrating a simple guest management system.

### 3. todo_list/

- An app featuring a to-do list with basic CRUD operations.

### 4. tasks/

- An app centered around managing tasks and assignments.

### 5. projects/

- A project management app for handling different projects.

### 6. blog/

- A blog app allowing users to create, edit, and delete blog posts.

### 7. project/

- An app focusing on individual project details and tasks.

## Static and Media Files

- Static and media files are served through Django. The patterns `^static/(?P<path>.*)$` and `^media/(?P<path>.*)$` are configured to handle static and media file routing.

## How to Use:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/FREDVUNI/django-learning.git
    ```

2. **Setup Virtual Environment:**

    ```bash
    cd django-learning
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create Superuser (Optional):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Apps:**
   - Visit `http://127.0.0.1:8000/admin/` for the Django admin.
   - Explore other apps using their respective URLs (e.g., `http://127.0.0.1:8000/guest/`, `http://127.0.0.1:8000/todo_list/`, etc.).

8. **Screenshots:**

![image](https://github.com/FREDVUNI/learning-django/assets/41730664/59c75206-c6d6-4673-8062-dea6957391c1)
![image](https://github.com/FREDVUNI/learning-django/assets/41730664/efef7301-00e8-4daa-85f1-0259887aae92)
![image](https://github.com/FREDVUNI/learning-django/assets/41730664/da374978-d8bb-43d7-a183-606ea569334a)
![image](https://github.com/FREDVUNI/learning-django/assets/41730664/99d510aa-297f-47db-bb2d-74c69bc22263)
![image](https://github.com/FREDVUNI/learning-django/assets/41730664/c50a7294-a1d0-4ed1-8749-c6287a7eb2ba)
![image](https://github.com/FREDVUNI/learning-django/assets/41730664/d4d0452e-33e4-4230-88fe-5085dc1717ec)
