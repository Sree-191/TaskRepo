from playwright.sync_api import expect, Page


def test_single_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#colors").select_option(value=['blue','yellow','red'])
    page.wait_for_timeout(5000)

    page.locator("#colors").select_option(['Green','White','Red'])
    page.wait_for_timeout(5000)

    page.locator("#colors").select_option(index=[1,0,4,3])
    page.wait_for_timeout(5000)


    # check number of options in dropdown

    dropdown_options = page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)

    option_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(option_text)

    for option in option_text:
        print(option)