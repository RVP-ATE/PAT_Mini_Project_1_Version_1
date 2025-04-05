
class HomePage:
    """
    HomePage class to represent and interact with elements on the home page of the website.
    """
    URL = "https://www.guvi.in/"  # The URL of the home page.

    def __init__(self, driver):
        """
        Initialize the HomePage object with the provided WebDriver instance.
        :param driver: WebDriver instance used to interact with the browser.
        """
        self.driver = driver  # Store the WebDriver instance for use in methods.

    def find_element(self, method, value):
        """
        Find a web element on the page using a specified locator method and value.
        :param method: The method to locate the element (e.g., 'xpath', 'id', etc.).
        :param value: The locator value (e.g., XPath, ID).
        :return: The located web element.
        """
        return self.driver.find_element(method, value)  # Locate and return the element.

    def click_signup(self):
        """
        Click on the sign-up button on the home page.
        Locates the sign-up button by its XPath and performs a click action.
        """
        # Find the sign-up button using XPath locator strategy
        signup_button = self.find_element('xpath', "//a[text()='Sign up']")
        signup_button.click()  # Click on the found sign-up button.
