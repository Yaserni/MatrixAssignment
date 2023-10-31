from commons.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, *args):
        super().__init__(args[0])
        self.remember_me_css = 'input.form-check-input'
        self.base_url = 'https://demo.applitools.com/'

    def set_username(self, username):
        self.element_by_id('username').send_keys(username)

    def set_password(self, password):
        self.element_by_id('password').send_keys(password)

    def click_login_btn(self):
        login_btn = self.element_by_id('log-in')
        self.click_element(login_btn)

    def click_remember_me_btn(self):
        remember_me_btn = self.element_by_css(self.remember_me_css)
        self.click_element(remember_me_btn)

    def navigate(self):
        self.navigate_to_url(self.base_url)
