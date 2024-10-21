# Self-Checkout System

A comprehensive self-checkout system built with Python, utilizing the `Tkinter` library for the graphical user interface (GUI) and `psycopg2` to interact with a PostgreSQL database. This application provides a user-friendly interface for customers to search products, manage their shopping basket, set their balance, and complete transactions.

## Table of Contents
1. [Features](#features)
2. [System Architecture](#system-architecture)
3. [Database Design](#database-design)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)

6. [Future Enhancements](#future-enhancements)

## Features

- **Product Search**: Users can search for products stored in the PostgreSQL database.
- **Basket Management**: Add products to the basket, remove items, and view the current basket contents.
- **Balance Management**: Set and track user balance for transactions.
- **Transaction Processing**: Complete purchases and generate receipts.
- **Database Integration**: All product and transaction data is stored and retrieved from a PostgreSQL database.
- **Category Management**: Products are organized into categories for easier navigation.
- **User Authentication**: (Planned feature) Support for user accounts and authentication.

## System Architecture

The Self-Checkout System consists of two main components:

1. **Frontend**: A Python application using Tkinter for the graphical user interface.
2. **Backend**: A PostgreSQL database for storing product, transaction, and user data.

The system uses `psycopg2` to establish a connection between the frontend and the database.

## Database Design

### Schema

The database includes the following tables:

- `products`: Stores product information (id, name, description, price, quantity, category_id).
- `categories`: Stores product categories (id, name, description).
- `transactions`: Records completed transactions (id, total_amount, payment_method, transaction_date).
- `transaction_items`: Links transactions to specific products (id, transaction_id, product_id, quantity, price_at_purchase).
- `users`: Stores user information for future authentication features (id, username, password_hash, email).

### Relationships

- Products belong to Categories (Many-to-One)
- Transaction Items belong to Transactions (Many-to-One)
- Transaction Items reference Products (Many-to-One)

### Optimizations

- Indexes on frequently queried columns (e.g., product name, transaction date)
- Connection pooling for efficient database connections

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kelvinnseth//Self_checkout_project.git
   cd Self_checkout_project
   ```

2. **Install Dependencies**
   ```bash
   pip install psycopg2 tkinter
   ```

3. **Set up PostgreSQL Database**
   - Install PostgreSQL if not already installed
   - Create a new database named `self_checkout_db`
   - Run the SQL scripts provided in `database/schema.sql` to create the necessary tables and indexes

4. **Configure Database Connection**
   Update the `config.py` file with your PostgreSQL credentials:
   ```python
   DB_CONFIG = {
       "dbname": "self_checkout_db",
       "user": "your_username",
       "password": "your_password",
       "host": "localhost",
       "port": "5432"
   }
   ```

5. **Run the Application**
   ```
   python self_checkout.py
   ```

## Usage

1. **Search for Products**: Enter a product name or category in the search bar and click "Search".
2. **Add to Basket**: Select a product from the search results and click "Add to Basket".
3. **Manage Basket**: View your current basket on the right side of the application. Use "Remove Item" to remove products.
4. **Set Balance**: Enter your available balance in the "Set Balance" field and click the button to update.
5. **Complete Transaction**: Click "Pay" to process the transaction. If successful, a receipt will be generated and displayed.


## Future Enhancements

1. Implement user authentication and personalized shopping experiences.
2. Add a graphical representation of products, including images.
3. Implement inventory management to update product quantities after purchases.
4. Create an admin interface for managing products, categories, and viewing transaction histories.
5. Implement a loyalty program and special offers system.
6. Add support for multiple payment methods (credit cards, mobile payments).
7. Develop a reporting system for sales analytics and inventory tracking.

## Contributing

Contributions to the Self-Checkout System are welcome! Please feel free to submit a Pull Request.

