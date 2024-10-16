import allure
from playwright.sync_api import Page


class PasswordField:
    def __init__(self, page: Page):
        self.page = page
        self.input_selector = "input#password"
        self.error_selector = "#password-err-msg app-error div, .alert-general-error, #pass-err-msg div"

    def enter(self, text: str):
        if text is not None:
            self.page.fill(self.input_selector, text)

    def is_displayed(self) -> bool:
        return self.page.is_visible(self.input_selector)

    def get_error_message(self, timeout: int = 3000) -> str:
        error_selector = ".alert-general-error, #pass-err-msg div"
        self.page.wait_for_selector(error_selector, timeout=timeout)

        if self.page.is_visible(error_selector):
            return self.page.inner_text(error_selector)

        return ""

    def is_valid(self) -> bool:
        return not self.page.is_visible(self.error_selector)

    def clear(self):
        self.page.click(self.input_selector)
        self.page.fill(self.input_selector, "")

    @allure.step("Check, if Password field is empty")
    def is_password_field_empty(self) -> bool:
        return "ng-pristine" in self.page.get_attribute("input#password", "class")
