import pytest
from selenium import webdriver
from page_objects.user.login_page import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class BaseTest:
    @pytest.fixture
    def base(self, browser):
        pass
