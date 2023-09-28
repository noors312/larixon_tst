# Use Alpine Linux as the base image
FROM python:3.9-alpine

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev libffi-dev

# Install Poetry using pip
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the 'pyproject.toml' and 'poetry.lock' files to leverage Poetry's
# dependency resolution
COPY pyproject.toml poetry.lock /app/

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --without dev --no-root --all-extras

# Copy the Django project files into the container
COPY . /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Specify the entrypoint script to run when the container starts
ENTRYPOINT ["/app/entrypoint.sh"]