# Import necessary libraries and modules
import pytest  # For running the tests
from pages.home_page import HomePage  # Importing the HomePage class
from pages.login_page import LoginPage  # Importing the LoginPage class
from utilities.base import Base  # Importing the Base class for setup and teardown

class Test(Base):
    """
    Test class for handling various tests related to the HomePage and LoginPage.
    Inherits from Base class to use setup and teardown methods.
    """

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """
        Setup and teardown for each test.
        Ensures that the browser is initialized before each test and closed after.
        """
        self.setup()  # Call the setup method from Base class to initialize WebDriver
        yield  # Yield to run the test
        self.teardown()  # Call the teardown method from Base class to close the browser

    def test_url_valid(self):
        """
        Test to check if the current URL matches the expected URL of the home page.
        """
        self.open_url(HomePage.URL)  # Open the home page URL
        assert self.driver.current_url == HomePage.URL, "URL does not match"

    def test_title(self):
        """
        Test to verify if the page title is as expected.
        """
        self.open_url(HomePage.URL)  # Open the home page URL
        assert self.get_title() == "GUVI | Learn to code in your native language", "Title mismatch"

    def test_login_button_visible_and_clickable(self):
        """
        Test to check if the login button is visible and clickable.
        """
        self.open_url(HomePage.URL)  # Open the home page URL
        home_page = HomePage(self.driver)  # Instantiate the HomePage class
        login_button = home_page.find_element('xpath', "//*[@id='login-btn']")  # Find the login button by XPath
        assert login_button.is_displayed(), "Login button is not visible"  # Check if login button is visible
        login_button.click()  # Click the login button

    def test_signup_button_visible_and_clickable(self):
        """
        Test to check if the signup button is visible and clickable.
        """
        self.open_url(HomePage.URL)  # Open the home page URL
        home_page = HomePage(self.driver)  # Instantiate the HomePage class
        signup_button = home_page.find_element('xpath', "//a[text()='Sign up']")  # Find the signup button by XPath
        assert signup_button.is_displayed(), "Sign-up button is not visible"  # Check if signup button is visible
        signup_button.click()  # Click the signup button

    def test_sign_up_redirect(self):
        """
        Test to check if clicking the signup button redirects to the correct URL.
        """
        self.open_url(HomePage.URL)  # Open the home page URL
        home_page = HomePage(self.driver)  # Instantiate the HomePage class
        home_page.click_signup()  # Click the signup button
        # Assert that the current URL is not the login URL
        assert self.driver.current_url != "https://www.guvi.in/sign-in/"
        print(f"Expected URL: https://www.guvi.in/register/")
        print(f"Actual URL: {self.driver.current_url}")
        print(f"Expected URL: https://www.guvi.in/register/ Should not equal to URL: https://www.guvi.in/sign-in/")

    def test_login_success(self):
        """
        Test to perform a successful login with valid credentials.
        """
        self.open_url("https://www.guvi.in/sign-in/")  # Open the login page
        login_page = LoginPage(self.driver)  # Instantiate the LoginPage class
        login_page.login("manupavankumar@gmail.com", "Pavan#223")  # Perform login with valid credentials

    def test_login_invalid(self):
        """
        Test to check if the login fails with invalid credentials and if the correct error message is shown.
        """
        self.open_url("https://www.guvi.in/sign-in/")  # Open the login page
        login_page = LoginPage(self.driver)  # Instantiate the LoginPage class
        login_page.login("invalidemail@example.com", "invalidpassword")  # Attempt login with invalid credentials
        error_message = login_page.get_error_message()  # Get the error message displayed after login failure
        assert error_message == "Incorrect Email or Password", f"Expected error message 'Incorrect Email or Password', but got '{error_message}'"
        print(f"The Error Message for invalid email and password is {error_message}")
