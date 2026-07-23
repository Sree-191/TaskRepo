from playwright.sync_api import Page, expect
import re

def test_flipkart_page(page: Page):
    page.goto("https://www.flipkart.com/")

    login_popup = page.get_by_role("button", name = "✕")
    login_popup.click()
    expect(page).to_have_title("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!")

    search_box = page.get_by_role("textbox",name= "Search for Products, Brands and More")
    search_box.fill("Summer Essentials")
    search_box.press("Enter")

    expect(page).to_have_url(re.compile(".*Summer.*"))
    expect(page.get_by_text("Summer Essentials")).to_be_visible()