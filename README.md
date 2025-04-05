# Selenium WebDriver Test Automation Framework

This project is a Selenium WebDriver-based test automation framework for testing the functionality of a web application. It includes tests for logging in, navigating, and interacting with elements on the `https://www.guvi.in/` website. The framework is built with Python, `pytest`, and `Selenium`.

## Prerequisites

Before running the tests, make sure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Selenium**: WebDriver for automating browsers.
- **ChromeDriver**: If you're using Google Chrome, download the appropriate version of ChromeDriver [here](https://sites.google.com/a/chromium.org/chromedriver/).
- **pytest**: A testing framework for Python to run the tests.
- **pip**: Python's package installer.

### Install Dependencies

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install all required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` should contain:

   ```txt
   selenium
   pytest
   ```

3. **Download ChromeDriver**: Make sure to download the ChromeDriver and either add it to your system’s PATH or specify the path directly in the `Base.py` file (within the `setup()` method).

---

## Project Structure

```
your_project/
├── pages/
│   ├── home_page.py         # HomePage class for interacting with home page elements
│   ├── login_page.py        # LoginPage class for interacting with login page elements
├── utilities/
│   └── base.py              # Base class for setup and teardown
├── tests/
│   └── test_login.py        # Test suite with various login and home page tests
├── requirements.txt         # Python dependencies file
├── README.md                # Project documentation
└── chromedriver             # ChromeDriver for Selenium (or specify path in code)
```

---

## Configuration

1. **WebDriver Configuration**:
   - The default browser for the framework is **Chrome**. Ensure the correct version of **ChromeDriver** is installed.
   - If you want to use a different browser, modify the `Base.py` class to configure WebDriver for that browser.

---

## Running Tests

To run the tests in this framework, follow these steps:

1. **Make sure ChromeDriver is installed**:
   - Ensure that `chromedriver` is available in your system’s PATH or specify its path in the code.
   
2. **Run Tests with `pytest`**:
   - You can run all the tests at once by executing the following command:

     ```bash
     pytest tests/test_login.py --maxfail=1 --disable-warnings -q
     ```

   - **Explanation**:
     - `--maxfail=1`: Stops after the first failure (optional).
     - `--disable-warnings`: Disables warnings to make the output cleaner.
     - `-q`: Quiet mode to reduce verbosity.

3. **Run Tests Programmatically**:
   - You can also trigger the tests programmatically by running the following Python script:

     ```bash
     python run_tests.py
     ```

---

## Tests

### Available Tests:

1. **Test URL Validity**: 
   - Verifies that the home page URL is correct.
   
2. **Test Page Title**: 
   - Verifies that the title of the home page matches the expected value.

3. **Test Login Button Visibility & Clickability**: 
   - Ensures that the login button is visible and clickable.

4. **Test Signup Button Visibility & Clickability**: 
   - Ensures that the signup button is visible and clickable.

5. **Test Signup Redirect**: 
   - Ensures that clicking the "Sign up" button redirects the user to the correct page.

6. **Test Login Success**: 
   - Logs in with valid credentials and verifies the successful login.

7. **Test Login with Invalid Credentials**: 
   - Tries logging in with invalid credentials and checks if the correct error message is displayed.

---

## Customizing Tests

- You can customize the tests by modifying the test functions in the `test_login.py` file.
- You can add more tests for other pages or user interactions.
- The `HomePage` and `LoginPage` classes can be extended to add more page elements and interactions.

---

## Example Output

When the tests are executed, the following output will appear in the terminal:

```bash
============================= test session starts =============================
collecting ... collected 7 items

test_guvi.py::Test::test_url_valid <- ..\..\guvi_automation\test_cases\test_guvi.py 
test_guvi.py::Test::test_title <- ..\..\guvi_automation\test_cases\test_guvi.py 
test_guvi.py::Test::test_login_button_visible_and_clickable <- ..\..\guvi_automation\test_cases\test_guvi.py 
test_guvi.py::Test::test_signup_button_visible_and_clickable <- ..\..\guvi_automation\test_cases\test_guvi.py 
test_guvi.py::Test::test_sign_up_redirect <- ..\..\guvi_automation\test_cases\test_guvi.py 
test_guvi.py::Test::test_login_success <- ..\..\guvi_automation\test_cases\test_guvi.py 
test_guvi.py::Test::test_login_invalid <- ..\..\guvi_automation\test_cases\test_guvi.py 

======================== 7 passed in 64.68s (0:01:04) =========================
```

---

## Troubleshooting

- **WebDriver errors**:
  - Ensure that the correct version of **ChromeDriver** is installed and matches your installed version of Google Chrome.
  - You can download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/).

- **Element Not Found**:
  - If any test fails due to element not being found, inspect the web page using browser developer tools to verify the locators in `HomePage.py` and `LoginPage.py`.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
