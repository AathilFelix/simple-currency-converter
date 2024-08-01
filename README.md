# Simple Currency Converter

## Description
A currency converter project that uses Fawaz Ahmed's open-source API to access up-to-date currency conversions.

## Project Structure

### app.py
The core of the application, built with Flask. It handles the backend server logic and includes the `index` function.

- **index() function**: 
  - Handles GET requests by rendering `index.html` for user input.
  - Handles POST requests by processing form data to generate and return the exchange value.

### helpers.py
Contains core functions essential for the project:

- **get_currency_exchange(currencya, currencyb, amount)**: Returns the exchange rate between two currencies.
- **get_currencies()**: Returns a list of currencies for rendering in `index.html`.
- **apology(message, code)**: Returns an error message with a provided HTTP code using the Memegen API.

## HTML Files

- **index.html**: Displays information for the user in a user-friendly format, including forms and buttons. JavaScript is used to enhance the UI experience and parse data to the Flask backend.
- **layout.html**: The foundation for `index.html`, containing elements from Bootstrap and the webpage favicon.
- **apology.html**: Uses the Memegen API to generate a custom error message for client-side errors.

---