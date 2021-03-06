from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
import time


class AdminTestCase(LiveServerTestCase):
    # функция setUp создает экземпляр пользователя и веб драйвера
    def setUp(self):
        # создание экземпляра пользователя
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )

        # подключение веб драйвера
        self.selenium = webdriver.Chrome('Kinopedia/chromedriver.exe')
        self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        # функция закрывает браузер по завершению тестирования

        self.selenium.quit()
        super(AdminTestCase, self).tearDown()

    def test_create_user(self):
        # Открытие формы авторищации
        # Получение url к live server
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/admin/")
        )

        # заполнение данных пользователя
        username = self.selenium.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("admin")

        # Поиск кнопки входа и нажатие на неё
        self.selenium.find_element_by_xpath('//input[@value="Войти"]').click()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/admin/")
        )