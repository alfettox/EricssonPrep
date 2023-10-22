# Automated Login Testing Script (Python)

## Project Overview

This project demonstrates how to create an automated login testing script using Python and Selenium. The script is designed to test login functionality on a web page, and it provides detailed reports on the results of login attempts.

## Project Components

### 1. Prerequisites

Before running the script, make sure you have the following components and prerequisites in place:

- Python 3.x installed.
- The Selenium library for Python. You can install it using `pip`:

  ```shell
  pip install selenium
A WebDriver for your preferred browser (e.g., Chrome WebDriver or Firefox WebDriver). Ensure that the WebDriver is in your system's PATH.
2. Project Structure
The project directory should have the following structure:

bash
Copy code
project_directory/
│
├── .env                   # Configuration file for storing environment variables
├── login_test.py          # The Python script for login testing
├── README.md              # Project documentation
3. Environment Variables
Sensitive data such as login credentials should be stored in an .env file. Create a .env file in your project directory with the following format:

makefile
Copy code
VALID_USERNAME=your_valid_username
VALID_PASSWORD=your_valid_password
INVALID_USERNAME=your_invalid_username
INVALID_PASSWORD=your_invalid_password
Replace the placeholders with your actual test data. Ensure that you do not upload the .env file to a public repository.

4. Python Script
The login_test.py script is the main component of the project. It performs the following tasks:

Initializes a WebDriver for web testing.
Defines the URL of the login page.
Automates the login process using the Selenium library.
Captures and reports the results of login attempts.
Handles exceptions and provides detailed error messages.
5. Running the Script
To run the script, open your terminal, navigate to the project directory, and execute the following command:

shell
Copy code
python login_test.py
The script will run login tests using the provided credentials and report the results in the terminal.

Conclusion
This project showcases how to create an automated login testing script in Python using the Selenium library. It emphasizes the use of environment variables to store sensitive data securely and provides a clear structure for your testing script.
