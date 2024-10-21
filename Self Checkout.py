# Import necessary modules
import psycopg2  # Library to connect and interact with PostgreSQL
from tkinter import *  # Import all from tkinter for GUI elements
from tkinter import ttk  # Import ttk for themed widgets

# Function to create the database table if it doesn't exist
def create_database_table():
    conn = psycopg2.connect(
        dbname="products",
        user="postgres",
        password="Target@database",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    # SQL query to create a table if it does not exist already
    cur.execute(""" 
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    description VARCHAR(255),
                    price DECIMAL(10, 2),
                    quantity INTEGER
                );
            """)
    conn.commit()
    conn.close()

# Class for the Self Checkout application (inherits from Tk)
class Self_checkout(Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Tk)
        self.title("Self Checkout Machine")  # Set the window title

        # Instance variables
        self.basket = []
        self.total_price = 0.0
        self.results = []
        self.user_balance = 0.0
        self.selected_item = StringVar()  # Track selected item for deletion

        # Create a style object to customize ttk widgets
        style = ttk.Style()
        style.theme_use('clam')  # Use a modern theme
        style.configure("TFrame", background="#ffffff", relief="flat")
        style.configure("TLabel", font=("Helvetica", 10), background="#ffffff", foreground="#333333")
        style.configure("TButton", font=("Helvetica", 10), padding=10, relief="flat", background="#333", foreground="#ffffff")
        style.configure("Custom.TButton", background="red", foreground="white")
        style.configure("Custom.TLabel", font=("Arial", 12, "bold"))
        style.map("TButton", background=[('active', '#222')])
        style.configure("TEntry", padding=5)

        # Grid configuration for layout management
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # GUI Elements
        self.frame = ttk.Frame()
        self.frame.grid(row=0, column=0, sticky="ns", columnspan=2)

        self.frame_display = ttk.Frame()
        self.frame_display.grid(row=0, column=3, sticky="ns")



        # Label to show current basket items
        self.basket_label = ttk.Label(self.frame_display, style="Custom.TLabel", text="Basket: []", width=40)
        self.basket_label.grid(row=5, column=1, pady=30, padx=30, sticky="")

        # Dropdown to select an item to remove
        self.item_dropdown = ttk.Combobox(self.frame_display, textvariable=self.selected_item, width=40)
        self.item_dropdown.grid(row=6, column=1, pady=10, padx=30, sticky="ew")

        # Button to remove an item from the basket
        self.remove_button = ttk.Button(self.frame_display, text="Remove Item", command=self.remove_from_basket)
        self.remove_button.grid(row=6, column=5, padx=30, pady=10, sticky="ew")


        # Search Entry
        self.search_entry = ttk.Entry(self.frame, style="Custom.TEntry", font=('Arial', 12))
        self.search_entry.grid(row=0, column=1, columnspan=2, padx=30, pady=30, sticky="ew")

        # Button to search for items
        self.search_button = ttk.Button(self.frame, text="Search", command=self.search_product)
        self.search_button.grid(row=1, column=1, padx=30, pady=10, sticky="ew")

        # Label to display search results
        self.label = ttk.Label(self.frame_display, style="Custom.TLabel", text="Your basket will appear here", width=40)
        self.label.grid(row=3, column=1, pady=30, padx=30, sticky="")

        # Button to add to basket
        self.add_to_basket_button = ttk.Button(self.frame_display, text="Add to Basket", command=self.add_to_basket)
        self.add_to_basket_button.grid(row=4, column=1, padx=30, pady=10, sticky="ew")

        # Label to show current basket items
        self.basket_label = ttk.Label(self.frame_display, style="Custom.TLabel", text="Basket: []", width=40)
        self.basket_label.grid(row=5, column=1, pady=30, padx=30, sticky="")

        # Label to show total price
        self.total_price_label = ttk.Label(self.frame_display, style="Custom.TLabel", text="Total Price: £0.00", width=40)
        self.total_price_label.grid(row=6, column=1, pady=30, padx=30, sticky="")
        # Dropdown to select an item to remove
        self.item_dropdown = ttk.Combobox(self.frame_display, textvariable=self.selected_item, width=40)
        self.item_dropdown.grid(row=6, column=1, pady=10, padx=30, sticky="ew")

        # Button to remove an item from the basket
        self.remove_button = ttk.Button(self.frame_display, text="Remove Item", command=self.remove_from_basket)
        self.remove_button.grid(row=7, column=1, padx=30, pady=10, sticky="ew")

        # Balance Entry
        self.balance_entry = ttk.Entry(self.frame, style="Custom.TEntry", font=('Arial', 12))
        self.balance_entry.grid(row=2, column=1, padx=30, pady=10, sticky="ew")
        self.balance_entry.insert(0, "Enter your balance")  # Placeholder text

        # Button to set balance
        self.set_balance_button = ttk.Button(self.frame, text="Set Balance", command=self.set_balance)
        self.set_balance_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        # Label to show user balance
        self.balance_label = ttk.Label(self.frame_display, style="Custom.TLabel", text="Balance: £0.00", width=40)
        self.balance_label.grid(row=7, column=1, pady=10, padx=30, sticky="")

        # Button to pay for items
        self.pay_button = ttk.Button(self.frame_display, text="Pay", command=self.pay)
        self.pay_button.grid(row=8, column=1, padx=30, pady=10, sticky="ew")

    def search_product(self):
        search_term = self.search_entry.get().strip()

        conn = psycopg2.connect(
            dbname="products",
            user="postgres",
            password="Target@database",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # SQL query to search for items along with their prices
        cur.execute("SELECT name, price FROM products WHERE name ILIKE %s;", ('%' + search_term + '%',))
        self.results = cur.fetchall()  # Store the results for later use

        if self.results:
            # Format results into a string
            result_text = "Found items:\n" + "\n".join([f"{item[0]} - £{item[1]:.2f}" for item in self.results])
        else:
            result_text = "No items found."

        # Update the label to display results
        self.label.config(text=result_text)

        # Close the database connection
        conn.close()

    def update_basket_display(self):
            # Update the basket label to show current items
            basket_items = ', '.join([f"{item[0]}\n - £{item[1]:.2f}" for item in self.basket])
            self.basket_label.config(text=f"Basket: [{basket_items}]")
            self.total_price_label.config(text=f"Total Price: £{self.total_price:.2f}")

            # Update the item dropdown with items in the basket
            self.item_dropdown['values'] = [item[0] for item in self.basket]  # Populate dropdown with item names
            self.selected_item.set('')  # Clear the selection

    def remove_from_basket(self):
        item_to_remove = self.selected_item.get()  # Get the selected item name

        if item_to_remove:
            conn = psycopg2.connect(
                dbname="products",
                user="postgres",
                password="Target@database",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()

            try:
                # Remove the selected item from the basket in the local list
                for item in self.basket:
                    if item[0] == item_to_remove:
                        self.basket.remove(item)
                        self.total_price -= float(item[1])  # Adjust the total price
                        break

                # SQL query to delete the selected item from the `todo` table
                cur.execute("DELETE FROM todo WHERE list_item = %s;", (item_to_remove,))
                conn.commit()  # Commit the changes to the database

                # Update the basket display after the item is removed
                self.update_basket_display()

                # Provide feedback in the label widget
                self.label.config(text=f"Removed {item_to_remove} from the basket!")
            except Exception as e:
                self.label.config(text="Error removing item from basket.")
                print(f"Error: {e}")
            finally:
                cur.close()  # Close the cursor
                conn.close()  # Close the connection
        else:
            self.label.config(text="No item selected to remove!")

    def add_to_basket(self):
        # Add the first search result to the basket (modify as needed)
        if self.results:
            item_to_add = self.results[0][0]  # Get the first item
            price_to_add = self.results[0][1]  # Get the price of the first item
            self.basket.append((item_to_add, price_to_add))  # Add item and price to the basket
            self.total_price += float(price_to_add)  # Update total price
            self.update_basket_display()

            # Clear the search entry after adding the item
            self.search_entry.delete(0, END)  # Clear the search bar

    def set_balance(self):
        # Set the user's balance from the entry field
        try:
            self.user_balance = float(self.balance_entry.get())
            self.balance_label.config(text=f"Balance: £{self.user_balance:.2f}")
        except ValueError:
            self.balance_label.config(text="Invalid balance!")

    def pay(self):
        # Check if user balance is sufficient
        if self.user_balance >= self.total_price:
            paid_amount = self.total_price  # Store total price before resetting it

            # Log the transaction and get the transaction ID and date
            transaction_id, transaction_date = self.log_transaction(paid_amount)

            # Deduct total price from balance
            self.user_balance -= paid_amount
            self.balance_label.config(text=f"Balance: £{self.user_balance:.2f}")
            self.basket.clear()
            self.total_price = 0.0  # Reset total price after logging and deducting

            self.update_basket_display()

            # Create the receipt string using `paid_amount` instead of `self.total_price`
            receipt = f"Receipt\nTransaction ID: {transaction_id}\n"
            receipt += f"Transaction Date: {transaction_date}\n"
            receipt += "Items Purchased:\n"
            for item, price in self.basket:
                receipt += f"- {item}: £{price:.2f}\n"
            receipt += f"Total Amount: £{paid_amount:.2f}\n"  # Use `paid_amount` here
            receipt += "Thank you for your purchase!"

            # Print the receipt to the console (or display it in the GUI)
            print(receipt)  # Print receipt in the console
            self.label.config(text=receipt)  # Display the receipt in the label widget

        else:
            self.label.config(text="Insufficient funds!")

    def log_transaction(self,total_amount):
        conn = psycopg2.connect(
            dbname="products",
            user="postgres",
            password="Target@database",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # SQL query to insert the transaction and return the transaction details
        cur.execute("""
            INSERT INTO transactions (total_amount) 
            VALUES (%s)
            RETURNING transaction_id, transaction_date;
        """, (total_amount,))

        # Fetch the transaction ID and date after inserting
        transaction_record = cur.fetchone()

        conn.commit()  # Commit the transaction
        cur.close()  # Close the cursor
        conn.close()  # Close the database connection

        return transaction_record  # Return transaction ID and date


# Create an instance of the Self_checkout class and run the app
run = Self_checkout()

# Create the database table if it doesn't exist
create_database_table()

# Start the Tkinter event loop
run.mainloop()