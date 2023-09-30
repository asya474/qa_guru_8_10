from selene import browser, have, be
from selene.support.shared import browser


def test_submit_form(browser_open):
    browser.should(have.title_containing('DEMOQA'))
# first name
    browser.element('[id="firstName"]').type('Test').press_enter()
# last name
    browser.element('[id="lastName"]').type('Test').press_enter()
# email
#    browser.element('[id="userEmail"]').type('test@test.com').press_enter()
# gender chexbox
    browser.element('input#gender-radio-2+.custom-control-label').click()
# mobile number
    browser.element('[id="userNumber"]').type('1234567890').press_enter()
# date of birth
#    browser.element('[id="dateOfBirthInput"]').type('b.').press_enter()
# subjects
#   browser.element('input#subjectsInput').type('Hello world').press_enter()
# hobbies chexbox
#    browser.element('input#hobbies-checkbox-1+.custom-control-label').click()
# current address
#    browser.element('[id="currentAddress"]').type('Hollywood').press_enter()
# select state
#    browser.element('#state > *:first-child > *:first-child').type('b.').press_enter()
# select city
#    browser.element('#city > *:first-child > *:first-child').type('b.').press_enter()
# submit
#    browser.element('[id="submit"]').click()
# submit form
    browser.element('#example-modal-sizes-title-lg').should(be.visible)
