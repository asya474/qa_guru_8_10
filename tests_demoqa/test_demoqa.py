import os
from selene import browser, have, be
from selene.support.shared import browser


def test_registration_form(browser_management):
    browser.open("/automation-practice-form")
    browser.element("#firstName").should(be.visible).type('Test')
    browser.element("#lastName").should(be.visible).type('Test')
    browser.element("#userEmail").should(be.visible).type('test@test.com')
    browser.element("input#gender-radio-2+.custom-control-label").should(be.visible).click()
    browser.element("#userNumber").should(be.visible).type("1234567890")
    browser.element("#dateOfBirthInput").should(be.visible).click()
    browser.element(".react-datepicker__month-select").should(be.visible).click()
    browser.element(".react-datepicker__month-select > option:nth-child(5)").should(be.visible).click()
    browser.element(".react-datepicker__year-select").should(be.visible).click()
    browser.element(".react-datepicker__year-select > option:nth-child(20)").should(be.visible).click()
    browser.element(".react-datepicker__day.react-datepicker__day--012").should(be.visible).click()
    browser.element("input#subjectsInput").should(be.visible).type('Hello world').press_enter()
    browser.element("input#hobbies-checkbox-1+.custom-control-label").should(be.visible).click()
    browser.element("#uploadPicture").should(be.visible).type(os.path.abspath("pictures/character.png"))
    browser.element("currentAddress").should(be.visible).type("Hollywood")
    browser.element("#state > *:first-child > *:first-child").should(be.visible).type("NCR").press_enter()
    browser.element("#city > *:first-child > *:first-child").should(be.visible).type("Delhi").press_enter()
    browser.element("#submit").should(be.visible).click()
    browser.all("#example-modal-sizes-title-lg").should(have.texts(
    "Test Test",
    "test@test.com",
    "Female",
    "1234567890",
    "12 May 1919",
    "Hello world",
    "Sports",
    "character.png",
    "Hollywood",
    "NCR Delhi"))
    browser.element("#closeLargeModal").should(be.visible).click()
