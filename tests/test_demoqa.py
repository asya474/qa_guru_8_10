from pages.registration_page import RegistrationPage


def test_student_registration_form(browser_setup):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Test')
    registration_page.fill_last_name('Test')
    registration_page.fill_email('test@test.com')
    registration_page.choose_gender('Male')
    registration_page.fill_mobile_number('1234567890')
    registration_page.fill_date_of_birth('2001', 'May', '15')
    registration_page.choose_subject('Computer Science')
    registration_page.choose_hobbie('Reading')
    registration_page.select_picture('character.png')
    registration_page.fill_address('Sugar Palace, a candy store in Ponyville')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')

    registration_page.submit_form()

    registration_page.should_have_registered(
        'Test Test',
        'test@test.com',
        'Male',
        '1234567890',
        '15 May,2001',
        'Computer Science',
        'Reading',
        'character.png',
        'Sugar Palace, a candy store in Ponyville',
        'NCR Delhi')
