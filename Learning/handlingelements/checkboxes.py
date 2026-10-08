from playwright.sync_api import Page, expect

def test_checkbox(page: Page):
    page.goto("https://practice-automation.com/form-fields/")

    # select specific checkbox
    water = page.get_by_label("Water")
    water.check()
    expect(water).to_be_checked()
    # page.wait_for_timeout(5000)
    water.uncheck()
    expect(water).not_to_be_checked()

    # count number of checkboxes
    favorite_drink = ['Water', 'Milk', 'Coffee', 'Wine', 'Ctrl-Alt-Delight']
    list_drinks = []

    # for drinks in favorite_drink:
    #    list_of_drinks = page.get_by_label(drinks)
    #    list_drinks.append(list_of_drinks)
    #    print(len(list_drinks))
    # One line code
    list_drinks = [page.get_by_label(x) for x in favorite_drink]
    print('No.of favorite drinks: ', len(list_drinks))

    #3 select all the checkboxes and assert each check box is selected
    # for drink in list_drinks:
    #     drink.check()
    #     expect(drink).to_be_checked()


    #4 check last 3 checkboxes
    # for drink in list_drinks[-3:]:
    #     drink.uncheck()
    #     expect(drink).not_to_be_checked()

    #5 Uncheck the selected checkboxes and check the unselected checkboxes [Toggle checkboxes]

    # for drink in list_drinks:
    #     if drink.is_checked():
    #         drink.uncheck()
    #         expect(drink).not_to_be_checked()
    #     else:
    #         drink.check()
    #         expect(drink).to_be_checked()


    #6 Randomly check checkboxes - check 1,3,6 checkboxes
    # indexes = [0, 2, 4]
    # for index in indexes:
    #     list_drinks[index].check()
    #     expect(list_drinks[index]).to_be_checked()

    #7 Select checkbox based on label/input value by choice

    drink = 'wine'

    for label in favorite_drink:
        if label==drink:
            checkbox = page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_checked()