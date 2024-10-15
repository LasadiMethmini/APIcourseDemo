# Book List API Project

This project involves developing a simple API for a bookstore to manage books and streamline the process of adding, editing, and browsing book collections via a website or mobile application. The API will implement standard CRUD (Create, Read, Update, Delete) operations for book management.

## Key Features:

### Django Model:
- **Book Model** with fields:
  - **title**: A string field (max length: 255).
  - **author**: A string field (max length: 255).
  - **price**: A decimal field (max 5 digits, 2 decimal places).

### API Endpoints:
- **GET /api/books**: 
  - Returns a list of all books in the database. This allows browsing the full collection, including books in or out of stock.
  
- **GET /api/books/{book_id}**: 
  - Returns a specific book by its ID. If the book doesn't exist, it returns a 404 error; otherwise, it returns the book details with a status code 200.
  
- **POST /api/books**: 
  - Adds a new book to the database. If successful, it returns the newly created book with a 201 status code. Missing or invalid data will trigger a 400 error.

### Editing and Deleting:
- **PUT /api/books/{book_id}**: 
  - Updates an existing book's information.
  
- **DELETE /api/books/{book_id}**: 
  - Deletes a book from the database. If the request is successful, it returns a confirmation message.

### Response Format:
- API responses will be returned in JSON format. For single book responses, data is delivered as a JSON object, not an array, following REST API conventions.
