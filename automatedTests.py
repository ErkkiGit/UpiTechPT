from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

IMPLICITLY_WAIT = 5

GOOGLE_URL = 'https://www.google.com'
OPUS_URL = "https://www.opusonline.co/"

CHECK_COMPANY_NAME = 'Opus Online'
CHECK_ADRESS = 'Pärnu maantee 139c, 11317 Tallinn'
CHECK_PHONE_NR = '682 9670'


class FindOpusFF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_URL)

    def test_01_find_company_name(cls):
        enter_google_search(cls.driver, CHECK_COMPANY_NAME)
        find_company_name(cls.driver)

    def test_02_find_address(cls):
        find_address(cls.driver)

    def test_03_find_phone_nr(cls):
        find_phone_nr(cls.driver)

    def test_04_find_company_link(cls):
        find_company_link(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class FindOpusChrome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_URL)

    def test_01_find_company_name(cls):
        enter_google_search(cls.driver, CHECK_COMPANY_NAME)
        find_company_name(cls.driver)

    def test_02_find_address(cls):
        find_address(cls.driver)

    def test_03_find_phone_nr(cls):
        find_phone_nr(cls.driver)

    def test_04_find_company_link(cls):
        find_company_link(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class FindOpusIe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_URL)

    def test_01_find_company_name(cls):
        enter_google_search(cls.driver, CHECK_COMPANY_NAME)
        find_company_name(cls.driver)

    def test_02_find_address(cls):
        find_address(cls.driver)

    def test_03_find_phone_nr(cls):
        find_phone_nr(cls.driver)

    def test_04_find_company_link(cls):
        find_company_link(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class FindOpusEdge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_URL)

    def test_01_find_company_name(cls):
        enter_google_search(cls.driver, CHECK_COMPANY_NAME)
        find_company_name(cls.driver)

    def test_02_find_address(cls):
        find_address(cls.driver)

    def test_03_find_phone_nr(cls):
        find_phone_nr(cls.driver)

    def test_04_find_company_link(cls):
        find_company_link(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


def enter_google_search(driver, user_input):
    search_field = driver.find_element_by_name('q')
    search_field.clear()
    search_field.send_keys(user_input)
    search_field.send_keys(Keys.ENTER)


def find_company_name(driver):
    company_name = driver.find_element_by_class_name('gsmt')
    company_name = company_name.text
    assert company_name == CHECK_COMPANY_NAME


def find_address(driver):
    address = driver.find_element_by_class_name('LrzXr')
    address = address.text
    assert address == CHECK_ADRESS


def find_phone_nr(driver):
    phone_nr = driver.find_element_by_class_name('zdqRlf')
    phone_nr = phone_nr.text
    assert phone_nr == CHECK_PHONE_NR


def find_company_link(driver):
    try:
        driver.find_element_by_xpath('//a[@href="' + OPUS_URL + '"]')
        link_found = True
    except Exception as error:
        print(error)
        link_found = False

    assert link_found is True


html_report_dir = './html_report'


def run_all_test_generate_html_report():
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))


if __name__ == '__main__':
    run_all_test_generate_html_report()
