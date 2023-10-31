from pages.login_page import LoginPage
from pages.transactions_page import TransactionsPage


class TestLogin:

    def test_login(self):
        login_page = LoginPage(self.selenium_driver)
        login_page.navigate()
        login_page.set_username("usern123")
        login_page.set_password("Passw212")
        login_page.click_login_btn()
        transactions_page = TransactionsPage(self.selenium_driver)
        assert transactions_page.is_transactions_table_displayed(), "Error, transactions table is not displayed"
        assert transactions_page.is_logged_username_displayed(), "Error, Logged User is not displayed"
        assert transactions_page.get_logged_username() == 'Jack Gomez', "Error, Logged User is as expected"

        transactions_page = transactions_page.get_transactions_table()
        succeed_transactions = transactions_page[transactions_page['STATUS'] == 'Complete']
        assert len(succeed_transactions) == 2, "Error, Number of completed transactions is incorrect"
        # assert transactions_page.get_number_of_completed_transactions() == 2, "Error, Number of completed transactions is incorrect"
