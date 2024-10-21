# Self Checkout Machine - Python GUI Application

This is a simple self-checkout system built with Python, using the `Tkinter` library for the graphical user interface (GUI) and `psycopg2` to interact with a PostgreSQL database. The application allows users to search for products, add them to a shopping basket, manage the basket, set their balance, and pay for items. A receipt is generated after payment.

## Features

- **Search Products**: Search for products stored in a PostgreSQL database.
- **Add to Basket**: Add selected products to the basket.
- **Remove from Basket**: Remove selected products from the basket.
- **Display Basket**: Shows current items in the basket and total price.
- **User Balance**: Allows the user to input a balance and deducts the total cost of items purchased.
- **Pay for Items**: Check if the user has sufficient funds to pay and generate a receipt after the transaction.
- **Receipt Generation**: A receipt containing details of the transaction is generated and printed.
- **PostgreSQL Integration**: Data is stored and fetched from a PostgreSQL database.

## Installation and Setup

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/self-checkout-machine.git
   cd self-checkout-machine
   ```

2. **Install Dependencies**

   Ensure you have the required Python packages installed:

   ```bash
   pip install psycopg2
   ```

3. **Set up PostgreSQL Database**

   Create a PostgreSQL database named `products` and set up the following schema by running the provided Python script.

   Use the following SQL schema for your database:

   ```sql
   CREATE TABLE IF NOT EXISTS products (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100),
       description VARCHAR(255),
       price DECIMAL(10, 2),
       quantity INTEGER
   );

   CREATE TABLE IF NOT EXISTS transactions (
       transaction_id SERIAL PRIMARY KEY,
       transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       total_amount DECIMAL(10, 2)
   );
   ```

4. **Configure Database Connection**

   Update the PostgreSQL connection details in the Python script (`host`, `user`, `password`, `dbname`, `port`) according to your setup:

   ```python
   conn = psycopg2.connect(
       dbname="products",
       user="postgres",
       password="YourDatabasePassword",
       host="localhost",
       port="5432"
   )
   ```

5. **Run the Application**

   After setting up the database, run the application:

   ```bash
   python self_checkout.py
   ```

## Usage

1. **Search Products**: Use the search bar to find products stored in the database.
2. **Add to Basket**: After searching, click on "Add to Basket" to add the first search result to your shopping basket.
3. **View and Manage Basket**: Your basket and total price will be displayed in the right-hand section. Use the "Remove Item" button to delete items from the basket.
4. **Set Balance**: Enter your available balance and click "Set Balance".
5. **Pay**: After adding items to the basket, click on "Pay" to complete the transaction. If your balance is sufficient, a receipt will be displayed.

## Project Structure

- `self_checkout.py`: Main Python script containing the GUI logic and database interactions.
- `README.md`: Instructions for setting up and running the project.

## Future Enhancements

- Implementing product categories and filtering.
- Enhancing the receipt generation to include more details.
- Adding a login system to support multiple users.



Feel free to raise any issues or contribute to the project on GitHub!

