from playwright.sync_api import Page, expect


def test_radiobuttons(page: Page):
    page.goto("https://practice-automation.com/form-fields/")
    x = page.locator("[type='radio']")
    # print(x.count()) #5

    favourite_colors = ["Red", "Blue", "Yellow", "Green", "#FFC0CB"]

    expect(x).not_to_be_checked()