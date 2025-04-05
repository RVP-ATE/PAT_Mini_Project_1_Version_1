# Importing necessary libraries
from selenium.webdriver.support import expected_conditions as EC  # For waiting on conditions.
from selenium.webdriver.support.wait import WebDriverWait  # To create explicit waits.
from selenium.webdriver.common.by import By  # To identify elements on the web page using different strategies.



class LoginPage:
    """
    LoginPage class to represent and interact with elements on the login page of the website.
    """

    def __init__(self, driver):
        """
        Initialize the LoginPage object with the provided WebDriver instance.
        :param driver: WebDriver instance used to interact with the browser.
        """
        self.driver = driver  # Store the WebDriver instance for use in methods.

    def login(self, email, password):
        """
        Login to the application using the provided email and password.
        This method interacts with the email and password fields, enters the credentials, and clicks the login button.
        :param email: The email address used for login.
        :param password: The password associated with the email.
        """
        # Find the email, password, and login button elements by their ID and input the credentials.
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        email_field.send_keys(email)  # Enter email.
        password_field.send_keys(password)  # Enter password.

        # Find the login button and click it to attempt login.
        login_button = self.driver.find_element(By.ID, "login-btn")
        login_button.click()  # Click the login button to submit the form.

    def get_error_message(self):
        """
        Get the error message displayed on the page after a failed login attempt.
        Waits for the error message to be visible and returns it.
        :return: The error message text if displayed; an empty string if no error message is found.
        """
        try:
            # Wait for the error message to become visible on the page (up to 10 seconds).
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='invalid-feedback']"))
            )
            # Once visible, get the error message text.
            error_message = self.driver.find_element(By.XPATH, "//div[@class='invalid-feedback']").text
            return error_message
        except Exception as e:
            # If the error message is not found or an exception occurs, print the error and return an empty string.
            print(f"Error while fetching error message: {e}")
            return ""


