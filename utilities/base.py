from selenium import webdriver
from selenium.webdriver.common.by import By

class Base:
    def setup(self):
        """
        Initialize the WebDriver, set up the browser,
        and maximize the browser window for testing.
        """
        self.driver = webdriver.Chrome()  # Launch Chrome browser using Selenium WebDriver.
        self.driver.maximize_window()  # Maximize the browser window for a better view.

    def teardown(self):
        """
        Close the browser after the completion of the test.
        Ensures that the WebDriver instance is properly closed.
        """
        if self.driver:
            self.driver.quit()  # Quit the browser and close all associated windows.

    def open_url(self, url):
        """
        Open the provided URL in the browser.
        :param url: The URL to navigate to.
        """
        self.driver.get(url)  # Navigate to the given URL.

    def get_title(self):
        """
        Retrieve the title of the current page.
        :return: The title of the web page.
        """
        return self.driver.title  # Return the title of the current page.

    def find_element(self, method, value):
        """
        Find an element on the page using a specific locator strategy.
        :param method: The locator strategy (e.g., 'xpath', 'id', 'name').
        :param value: The value of the locator (e.g., XPath expression or ID).
        :return: The web element found using the locator.
        """
        # Locate elements using different strategies.
        if method == 'xpath':
            return self.driver.find_element(By.XPATH, value)
        elif method == 'id':
            return self.driver.find_element(By.ID, value)
        elif method == 'name':
            return self.driver.find_element(By.NAME, value)
        # Add additional locator strategies as needed.

    def is_element_visible(self, element):
        """
        Check if an element is visible on the page.
        :param element: The web element to check.
        :return: True if the element is visible, False otherwise.
        """
        return element.is_displayed()  # Return whether the element is visible.

    def is_element_clickable(self, element):
        """
        Check if an element is clickable (enabled and visible).
        :param element: The web element to check.
        :return: True if the element is clickable, False otherwise.
        """
        return element.is_enabled() and element.is_displayed()  # Element must be enabled and visible.

    def click_element(self, element):
        """
        Click on a specified web element.
        :param element: The web element to click on.
        """
        element.click()  # Click the element using Selenium WebDriver.