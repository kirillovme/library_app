# Library App

Library App is a Django-based application for managing books, authors, and genres in a library. It provides RESTful APIs to create, read, update, and delete (CRUD) operations for each entity.

## Main Technologies Used

- Python 3.10
- Django 4.1 
- Django REST framework
- PostgreSQL 15
- Docker

## Deploying the Project

### Requirements
- Docker and Docker Compose installed
- GNU Make

### Instructions:
1. Clone the repository
   ```bash
   git clone <repository_url>
   ``` 
2. Start the containers
   ```bash
   make up-d
   ```
3. Run tests
   ```bash
   make test
   ```

## Key External Projects or Frameworks Used

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)

## Use Cases

1. CRUD operations for Author
   - Adding a new author
   - Viewing author details
   - Updating author information
   - Deleting an author

2. CRUD operations for Book
   - Adding a new book with authors and genres
   - Viewing book details
   - Updating book information
   - Deleting a book

3. CRUD operations for Genre
   - Adding a new genre
   - Viewing genre details
   - Updating genre information
   - Deleting a genre

## Project Branch Structure

- `main` - Current production branch of the project
- `develop` - Main development branch
