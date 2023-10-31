import pandas as pd

from commons.base_page import BasePage


class TransactionsPage(BasePage):
    def __init__(self, *args):
        super().__init__(args[0])
        self.transactions_table_css = 'table.table'
        self.transactions_table_row_css = 'table.table tbody tr'
        self.transactions_table_headers_css = 'table thead th'
        self.transactions_table_row_cells_css = self.transactions_table_row_css + ':nth-child({}) td'
        self.logged_username_css = 'div.logged-user-name'
        self.completed_green_icon = 'span.status-pill.smaller.green'

    def is_logged_username_displayed(self):
        return len(self.elements_by_css(self.logged_username_css)) > 0

    def get_logged_username(self):
        return self.element_by_css(self.logged_username_css).text

    def is_transactions_table_displayed(self):
        return len(self.elements_by_css(self.transactions_table_css)) > 0

    def get_number_of_completed_transactions(self):
        return len(self.elements_by_css(self.completed_green_icon))

    def get_transactions_table(self):
        table_rows = self.elements_by_css(self.transactions_table_row_css)
        table = {}
        columns = [cell.text for cell in self.elements_by_css(self.transactions_table_headers_css)]

        for row_index in range(1, len(table_rows) + 1):
            cells = [cell.text for cell in
                     self.elements_by_css(self.transactions_table_row_cells_css.format(row_index))]
            row = {}

            for i in range(len(columns)):
                row[columns[i]] = cells[i]
            table[row_index] = row

        s = pd.DataFrame(table)
        res_table = s.transpose()
        return res_table
