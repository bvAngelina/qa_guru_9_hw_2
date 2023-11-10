import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_configs():
    browser.config.window_width = 1920
    browser.config.window_height = 1200
    yield
    browser.quit()


def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.quit()

def test_no_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('gkelvlvkwekvglw').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу gkelvlvkwekvglw ничего не найдено'))
