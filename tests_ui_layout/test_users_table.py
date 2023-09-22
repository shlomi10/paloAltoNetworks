import pytest
from playwright.sync_api import sync_playwright
from pages.Home_page import Home_page
from tests_ui_layout.constants import *


@pytest.fixture()
def setup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)
        main_page = Home_page(page)
        yield main_page, page
        page.close()
        browser.close()

@pytest.mark.flaky(reruns=2)
def test_add_user(setup):
    main_page, page = setup
    main_page.add_user(FIRST_NAME, LAST_NAME)
    is_user_added = main_page.verify_user_added(FIRST_NAME, LAST_NAME)
    assert is_user_added, "User was not added"

@pytest.mark.flaky(reruns=2)
def test_id_in_table(setup):
    main_page, page = setup
    is_id_according_the_page = main_page.validate_id_on_page(PAGE_TO_GO)
    assert is_id_according_the_page, "ID is not according to the page"

@pytest.mark.flaky(reruns=2)
def test_table_navigation_via_input(setup):
    main_page, page = setup
    is_page_in_table = main_page.validate_page_in_table(PAGE_TO_GO)
    assert is_page_in_table, "ID is not according to the page"

@pytest.mark.flaky(reruns=2)
def test_table_navigation_via_character_input_fields(setup):
    main_page, page = setup
    is_user_stays_on_page_in_table = main_page.validate_page_in_table_with_invalid_values(CHARACTER_PAGE_TO_GO)
    assert is_user_stays_on_page_in_table, "Input field working with character"

@pytest.mark.flaky(reruns=2)
def test_table_navigation_via_zero_input_fields(setup):
    main_page, page = setup
    is_user_stays_on_page_in_table = main_page.validate_page_in_table_with_invalid_values(ZERO_PAGE_TO_GO)
    assert is_user_stays_on_page_in_table, "Input field is working with zero value"

@pytest.mark.flaky(reruns=2)
def test_table_navigation_via_name_input_fields(setup):
    main_page, page = setup
    is_user_stays_on_page_in_table = main_page.validate_page_in_table_with_invalid_values(NAME_PAGE_TO_GO)
    assert is_user_stays_on_page_in_table, "Input field is working with name value"

@pytest.mark.flaky(reruns=2)
def test_add_more_than_hundred_users(setup):
    main_page, page = setup
    main_page.go_to_page_in_table(TENTH_PAGE_TO_GO)
    main_page.add_user(FIRST_NAME, LAST_NAME)
    is_user_added = main_page.verify_user_added(FIRST_NAME, LAST_NAME)
    assert is_user_added, "User was not added"

    main_page.go_to_page_in_table(TENTH_PAGE_TO_GO)
    is_user_in_page_tenth = main_page.validate_user_in_page_tenth()
    assert is_user_in_page_tenth, "User not in page 10"

    main_page.go_to_page_in_table(PAGE_TO_FILL)
    is_user_in_page_eleven = main_page.validate_user_in_page_eleven()
    assert is_user_in_page_eleven, "User is not in page 11"

@pytest.mark.flaky(reruns=2)
def test_user_go_to_invalid_page(setup):
    main_page, page = setup
    main_page.go_to_page_in_table(TENTH_PAGE_TO_GO)
    is_user_in_page_tenth = main_page.validate_user_in_page_tenth()
    assert is_user_in_page_tenth, "User is not in page 10"

    main_page.go_to_page_in_table(SIXTY_PAGE_TO_GO)
    is_user_in_page_more_then_ten = main_page.validate_user_in_page_one_after_invalid_page()
    assert is_user_in_page_more_then_ten, "User not in page 1"

@pytest.mark.flaky(reruns=2)
def test_user_go_to_hugh_page_number(setup):
    main_page, page = setup
    main_page.go_to_page_in_table(TENTH_PAGE_TO_GO)
    is_user_in_page_tenth = main_page.validate_user_in_page_tenth()
    assert is_user_in_page_tenth, "User is not in page 10"

    main_page.go_to_page_in_table(HUGE_PAGE_NUMBER)
    is_user_in_page_more_then_ten = main_page.validate_user_in_page_one_after_invalid_page()
    assert is_user_in_page_more_then_ten, "User not in page 1"

@pytest.mark.flaky(reruns=2)
def test_arrows_in_table(setup):
    main_page, page = setup
    is_arrows_worked = main_page.validate_previous_and_forward_arrows(PAGE_TO_GO)
    assert is_arrows_worked, "Navigation arrows are not working"

@pytest.mark.flaky(reruns=2)
def test_that_table_has_ten_rows(setup):
    main_page, page = setup
    main_page.go_to_page_in_table(PAGE_TO_GO)
    is_expected_rows_in_table = main_page.verify_ten_rows_in_table(EXPECTED_ROWS_IN_TABLE)
    assert is_expected_rows_in_table, "There is not 10 rows in table"

@pytest.mark.flaky(reruns=2)
def test_that_table_has_correct_headers(setup):
    main_page, page = setup
    is_headers_correct = (main_page.verify_title_headers(PAGE_TO_GO, EXPECTED_ID_IN_TABLE, EXPECTED_NAME_IN_TABLE, EXPECTED_FAMILY_IN_TABLE))
    assert is_headers_correct, "Titles at the table not as described"

@pytest.mark.flaky(reruns=2)
def test_data_populated_correctly_in_table(setup):
    main_page, page = setup
    is_table_populated = main_page.verify_data_in_table()
    assert is_table_populated, "Table is not populated"