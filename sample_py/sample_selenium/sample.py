import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    target_url = 'http://www.python.org/'
    with webdriver.Chrome() as driver:
        driver.get(target_url)
        assert "Python" in driver.title

        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No results found.' not in driver.page_source

    return 0


if __name__ == '__main__':
    sys.exit(main())
