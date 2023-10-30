from behave import *

from pages.signin_page import sign_in
from pages.HomePage import HomePage


@when('user clicks on the button: {button}')
def step_impl(context, button):
    HomePage(context).clicks_on_button(button)


@when("user fills in valid {email} and {password}")
def step_impl(context, email, password):
    sign_in(context).fill_in_email(email)
    sign_in(context).fill_in_password(password)


@then("user should be logged in to application")
def step_impl(context):
    HomePage(context).verify_user_is_logged_in()


@when("user fills in invalid {email}")
def step_impl(context, email):
    sign_in(context).fill_in_email(email)


@then("user should not be logged in to application")
def step_impl(context):
    sign_in(context).verify_error_if_email_or_password_is_wrong()
