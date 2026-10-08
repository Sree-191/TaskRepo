from playwright.sync_api import Page, expect

def test_input_box(page: Page):
    page.goto("https://practice-automation.com/form-fields/")
    # text_box = page.locator("#name-input")  # CSS
    text_box = page.locator("//input[@name='name-input']")  # XPath

    # visibility of the element and enable or not

    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    # Check the attribute of the elements

    expect(text_box).to_have_attribute('type', 'text')

    # get an attribute of the element

    get_attribute = text_box.get_attribute("data-testid")
    print(get_attribute)

    # Fill the textbox
    text_box.fill("Demo")

    # get the input value from input box
    get_value = text_box.input_value()
    print(get_value)

    password_field = page.locator("input[type='password']")
    expect(password_field).to_be_visible()
    expect(password_field).to_be_enabled()
    get_password_attribute = password_field.get_attribute("type")
    print(get_password_attribute)
    password_field.fill("Demo2")

    password_input_value = password_field.input_value()
    print(password_input_value)