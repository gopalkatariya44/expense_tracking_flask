# My Flask Project

A brief description of what your project does and its purpose. For example:

This project is a simple web application built with Flask that allows users to manage books and expenses. Users can add new books, view a list of books, add expenses, view expense details, and manage their user account.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Add new books
- View a list of books
- Add new expenses
- View expense details
- User registration and login
- Responsive UI

## Demo

Here are some screenshots of the application:

### Login

![Login](demo/login.png)

### Register

![Register](demo/register.png)

### Add Book

![Add Book](demo/add_book.png)

### Book List

![Book List](demo/book_list.png)

### Expense List

![Expense List](demo/expense_list.png)

### Expense Details

![Expense Details](demo/expense_details.png)

### Add Expense

![Add Expense](demo/add_expense.png)

## Installation

To install and run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gopalkatariya44/expense_tracking_flask.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd your-repository
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Set up environment variables:**

   - Create a `.env` file in the root directory of your project and add the necessary configuration variables. Example:

     ```env
     PROJECT_NAME=Expense
     JWT_SECRET_KEY=
     SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@localhost/
     DATABASE_NAME=expense_tracking
     ```

7. **Run the application:**

   ```bash
   flask run
   ```

## Usage

Once the application is running, you can access it by navigating to [http://127.0.0.1:5001](http://127.0.0.1:5001) in your web browser.

### Main Features:

- **Add Book:** Navigate to the "Add Book" page to enter new book details.
- **View Books:** Go to the "Book List" page to see a list of all books.
- **Add Expense:** Navigate to the "Add Expense" page to enter new expense details.
- **View Expenses:** Go to the "Expense List" page to see a list of all expenses.
- **User Management:** Use the "Register" and "Login" pages to manage user accounts.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions about this project, please feel free to contact me.

- GitHub: [gopalkatariya44](https://github.com/gopalkatariya44)
