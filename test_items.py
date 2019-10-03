

def test_something(browser):
    link = ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    browser.get(link)
    cart_button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(cart_button) > 0