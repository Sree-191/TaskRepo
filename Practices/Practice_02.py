from playwright.sync_api import Page, expect


def test_expand_testing(page: Page):
    page.goto("https://practice.expandtesting.com/login")
    page.get_by_role("textbox", name="username").fill("practice")
    page.get_by_role("textbox", name="password").fill("SuperSecret&Password!")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your password is invalid!")).to_be_visible()