
import time
from pages.homepage import HomePage
from pages.product import Product


def test_open_S6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_s6()
    product = Product(driver)
    product.check_title('Samsung galaxy s6')

def test_open_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3) #ЗАПРЕЩЕНО, НУЖНО НЕ СПАТЬ А ЖДАТЬ ЗАГРУЗКИ ЧЕГО-ЛИБО
    homepage.check_count(2)
