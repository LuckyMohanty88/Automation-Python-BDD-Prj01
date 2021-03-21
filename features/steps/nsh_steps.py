from behave import *
import configparser
import os
from time import sleep

use_step_matcher("re")


def get_config():
    config_parser = configparser.RawConfigParser()
    config_file_path = os.getcwd() + '/config.ini'
    config_parser.read(config_file_path)
    return config_parser.get('URL', 'url')


@given("I am on NHS Help page\.")
def step_impl(context):
    context.browser.get(get_config())
    context.browser.find_element_by_xpath("//button[@id='nhsuk-cookie-banner__link_accept_analytics']").click()


@step("I click Next")
def step_impl(context):
    context.browser.find_element_by_xpath('//input[@value="Next"]').click()
    sleep(3)


@step("I click start")
def step_impl(context):
    context.page = context.browser.find_element_by_xpath("//input[@value='Start']").click()
    sleep(3)


@step('I select "(?P<country>.+)" as my living Country')
def step_impl(context, country):
    context.browser.find_element_by_xpath(f'//input[@value="{country}"]/parent::label').click()
    sleep(3)


@step('I Select "(?P<gp_status>.+)" for GP practice')
def step_impl(context, gp_status):
    context.browser.find_element_by_xpath(f'//input[@value="{gp_status}"]/parent::label').click()


@step("I input my birth date")
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@name='dateOfBirth.day']").send_keys("12")
    context.browser.find_element_by_xpath("//input[@name='dateOfBirth.month']").send_keys("02")
    context.browser.find_element_by_xpath("//input[@name='dateOfBirth.year']").send_keys("1999")


@step('I select "(?P<live_partner>.+)" for live with partner')
def step_impl(context, live_partner):
    context.browser.find_element_by_xpath(f'//input[@value="{live_partner}"]/parent::label').click()


@step('I select "(?P<partner_credit>.+)" for my partner credit')
def step_impl(context, partner_credit):
    context.browser.find_element_by_xpath(f'//input[@value="{partner_credit}"]/parent::label').click()


@step('I select "(?P<pregnant_status>.+)" for pragnant status')
def step_impl(context, pregnant_status):
    context.browser.find_element_by_xpath(f'//input[@value="{pregnant_status}"]/parent::label').click()


@step('I select "(?P<injury_status>.+)" for my injury status')
def step_impl(context, injury_status):
    context.browser.find_element_by_xpath(f'//input[@value="{injury_status}"]/parent::label').click()


@step('I select "(?P<diabetes_status>.+)" for my diabetes status')
def step_impl(context, diabetes_status):
    context.browser.find_element_by_xpath(f'//input[@value="{diabetes_status}"]/parent::label').click()


@step('I select "(?P<affect_status>.+)" for my affected status')
def step_impl(context, affect_status):
    context.browser.find_element_by_xpath(f'//input[@value="{affect_status}"]/parent::label').click()


@step('I select "(?P<glaucoma_status>.+)" for my glaucoma stutus')
def step_impl(context, glaucoma_status):
    context.browser.find_element_by_xpath(f'//input[@value="{glaucoma_status}"]/parent::label').click()


@step('I select "(?P<partner_live>.+)" for my partner live\.')
def step_impl(context, partner_live):
    context.browser.find_element_by_xpath(f'//input[@value="{partner_live}"]/parent::label').click()


@step('I select "(?P<local_council>.+)" for home care from local council')
def step_impl(context, local_council):
    context.browser.find_element_by_xpath(f'//input[@value="{local_council}"]/parent::label').click()


@step('I select "(?P<savings>.+)" for saving investment\.')
def step_impl(context, savings):
    context.browser.find_element_by_xpath(f'//input[@value="{savings}"]/parent::label').click()


@step("I save the screenshot for the result option page\.")
def step_impl(context):
    if context.config.userdata.get("headless", "false") == 'false':
        context.browser.execute_script("document.body.style.zoom='50%'")
        context.browser.find_element_by_tag_name('body').screenshot("screenshots/result.png")  # avoids scrollbar
    else:
        s = lambda x: context.browser.execute_script('return document.body.parentNode.scroll' + x)
        context.browser.set_window_size(s('Width'), s('Height'))
        context.browser.find_element_by_tag_name('body').screenshot("screenshots/result.png")
