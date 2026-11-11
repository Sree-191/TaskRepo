from playwright.sync_api import expect, Page


def test_single_dropdown(page: Page):
    page.goto("https://practice-automation.com/form-fields/")
    page.locator("#automation").select_option(value="No")
    page.wait_for_timeout(5000)
    page.locator("#automation").select_option("")
    page.wait_for_timeout(5000)
    page.locator("#automation").select_option(index=3)

    # check number of options in dropdown

    dropdown_options = page.locator("#automation>option")
    expect(dropdown_options).to_have_count(4)

    option_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(option_text)

    for option in option_text:
        print(option)