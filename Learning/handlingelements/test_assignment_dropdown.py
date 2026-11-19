from playwright.sync_api import expect, Page

def test_assignment_dropdown(page: Page):
    # Open the website
    page.goto("https://bstackdemo.com/")

    # Locate and verify dropdown
    dropdown = page.locator("select")

    expect(dropdown).to_be_visible()
    expect(dropdown).to_be_enabled()

    # sort the products from lowest to highest
    page.locator("select").select_option(value="lowestprice")

    products_count = page.locator("//div[@class='shelf-item']")
    print(products_count.count())
    expect(products_count).to_have_count(25)

    product_names = page.locator("//div[@class='shelf-item']/p").all_text_contents()
    product_prices = page.locator("//div[@class='shelf-item__price']//div[@class='val']").all_text_contents()

    product_name = [text.strip() for text in product_names]
    product_price = [price.strip() for price in product_prices]
    print(product_name)
    print(product_price)

    # for names in product_names:
    #     print(names)

    # for price in product_prices:
    #     print(price)

    # get lowest_price first product

