from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    text_to_be_present_in_element,
    invisibility_of_element_located,
)


def wait_and_assert_displayed(self, element):
    self.wait.until(visibility_of_element_located(element))
    self.assertTrue(self.driver.find_element(*element).is_displayed())
    return True


def wait_and_assert_not_displayed(self, element):
    self.wait.until(invisibility_of_element_located(element))
    self.assertTrue(len(self.driver.find_elements(*element)) == 0)


def wait_and_assert_text_equal(self, element, text):
    self.wait.until(text_to_be_present_in_element(element, text))
    self.assertEqual(self.driver.find_element(*element).text, text)


def wait_and_assert_element_is_enabled(self, element):
    self.wait.until(visibility_of_element_located(element))
    self.driver.find_element(*element).is_enabled()
