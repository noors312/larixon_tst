# LARIXON HOME TEST

## Getting Started

### 1. Clone the Repository

Clone the project repository from GitHub:

```bash
git clone https://github.com/noors312/larixon_tst.git
cd larixon_tst
```

### 2. Create a .env File

```bash
cp .env.example .env
```

### 3. Build and Start the Docker Containers

Build and start the Docker containers using Docker Compose:

```bash
docker-compose up --build
```

### 4. Apply migrations

Apply the database migrations to set up the initial database schema:

```bash
docker-compose exec app python manage.py migrate
```

### 5. Create a Superuser (Optional)

If you want to create an admin superuser for the Django admin panel, you can do
so using the following command:

```bash
docker-compose exec app python manage.py createsuperuser
```

### 6. Apply fixtures

```bash
docker-compose exec app sh -c "poetry install --only dev && python manage.py generate_initial_data_for_test"
```