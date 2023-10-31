from commons.base_page import BasePage


class TransactionsPage(BasePage):
    def __init__(self, *args):
        super().__init__(args[0])
        self.logged_username_css = 'div.logged-user-name'
        self.completed_green_icon = 'span.status-pill.smaller.green'

    def is_logged_username_displayed(self):
        return len(self.elements_by_css(self.logged_username_css)) > 0

    def get_logged_username(self):
        return self.element_by_css(self.logged_username_css).text

    def get_number_of_completed_transactions(self):
        return len(self.elements_by_css(self.completed_green_icon))
