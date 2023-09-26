from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page
from tests_ui_layout.constants import *

"""
This file contains the main table page, where you can navigate over existing users and add users
"""

class Home_page:
    def __init__(self, page):
        self.__page = Page
        self.__add_person_icon = page.locator("[data-testid='PersonAddIcon']")
        self.__first_name_field = page.locator("xpath=//label[contains(text(),'Name')]")
        self.__last_name_field = page.locator("xpath=//label[contains(text(),'Family')]")
        self.__add_button = page.locator("button.MuiButton-contained")
        self.__filter_field = page.locator("[id=':r0:']")
        self.__table = page.locator("tbody.MuiTableBody-root>tr")
        self.__previous_page_button = page.get_by_role("button").first
        self.__next_page_button = page.get_by_role("button").nth(1)
        self.__rows = page.locator("tr.MuiTableRow-root")
        self.__id_col = page.locator("td:nth-child(1)")
        self.__name_col = page.locator("td:nth-child(2)")
        self.__family_col = page.locator("td:nth-child(3)")
        self.__id_header = page.locator("tr th:nth-child(1)")
        self.__name_header = page.locator("tr th:nth-child(2)")
        self.__family_header = page.locator("tr th:nth-child(3)")

    def add_user(self, first_name: str, last_name: str):
        expect(self.__add_person_icon).to_be_enabled()
        self.__add_person_icon.click()
        self.__first_name_field.type(first_name)
        self.__last_name_field.type(last_name)
        self.__add_button.click()
        self.__filter_field.fill(PAGE_TO_FILL)
        self.__filter_field.press('Enter')

    def verify_user_added(self, exp_first_name: str, exp_last_name: str) -> bool:
        for row in self.__table.all():
            first_name_cell = row.locator(self.__name_col)
            first_name = first_name_cell.text_content().strip().lower()
            last_name_cell = row.locator(self.__family_col)
            family_name = last_name_cell.text_content().strip().lower()
            if (first_name == exp_first_name.lower()) and (family_name == exp_last_name.lower()):
                return True
        return False

    def verify_data_in_table(self) -> bool:
        for index in range(FIRST_PAGE, LAST_PAGE):
            self.go_to_page_in_table(str(index))
            for row in self.__table.all():
                if len(self.__table.all()) != EXPECTED_ROWS_IN_TABLE:
                    return False
                else:
                    id = row.locator(self.__id_col).inner_text()
                    name = row.locator(self.__name_col).inner_text()
                    family = row.locator(self.__family_col).inner_text()
                    if not name or not family or not id:
                        return False
        return True

    def validate_id_on_page(self, value: str) -> bool:
        self.__filter_field.fill(value)
        self.__filter_field.press('Enter')
        id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
        if int(id_in_table) == int(value) * 10:
            return True
        return False

    def go_to_page_in_table(self, value: str):
        self.__filter_field.fill(value)
        self.__filter_field.press('Enter')

    def validate_user_in_page_tenth(self) -> bool:
        id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
        if id_in_table == LAST_ID:
            return True
        return False

    def validate_user_in_page_one_after_invalid_page(self) -> bool:
        id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
        if id_in_table == LAST_ID_ON_PAGE_ONE:
            return True
        return False

    def validate_user_in_page_eleven(self) -> bool:
        id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
        if id_in_table == '110':
            return True
        return False

    def validate_page_in_table(self, value: str) -> bool:
        return self.validate_id_on_page(value)

    def validate_page_in_table_with_invalid_values(self, value: str) -> bool:
        if self.validate_id_on_page(PAGE_TO_GO):
            id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
            self.__filter_field.fill(value)
            self.__filter_field.press('Enter')
            if id_in_table == '50':
                return True
        return False

    def validate_previous_and_forward_arrows(self, value: str) -> bool:
        self.__filter_field.fill(value)
        self.__filter_field.press('Enter')
        id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
        if id_in_table != '50':
            return False
        self.__next_page_button.click()
        id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
        if id_in_table != '60':
            return False
        self.__previous_page_button.click()
        id_in_table = self.__table.all().pop().locator(self.__id_col).text_content()
        if id_in_table != '50':
            return False
        return True

    def verify_ten_rows_in_table(self, exp_rows: str) -> bool:
        return len(self.__table.all()) == exp_rows

    def verify_title_headers(self,page: str, exp_id: str, exp_name: str, exp_family: str) -> bool:
        self.go_to_page_in_table(page)
        if (self.__id_header.text_content() == exp_id and
            self.__name_header.text_content() == exp_name and
            self.__family_header.text_content() == exp_family):
            return True
        return False

