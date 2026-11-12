from playwright.sync_api import expect, Page

def test_sorted_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # dropdown_option = page.locator("#animals>option")  # sorted
    dropdown_option = page.locator("#colors>option") # unsorted

    options_text = [text.strip() for text in dropdown_option.all_text_contents()]

    original_list = options_text.copy()

    sorted_list = sorted(options_text)

    print("OriginalList:", original_list)
    print("SortedList:", sorted_list)

    if original_list==sorted_list:
        print("Drop down options are in sorted order")
    else:
        print("Drop down options are in unsorted order")
