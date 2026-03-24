import re
import time
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://tailwindcss.com/plus/ui-blocks/application-ui/overlays/modal-dialogs")
    page.locator("iframe[name=\"frame-b6812b6c13fff16861f2645c4100ae5b\"]").content_frame.get_by_role("button", name="Cancel").click()
    time.sleep(6)
    page.locator("iframe[name=\"frame-b6812b6c13fff16861f2645c4100ae5b\"]").content_frame.get_by_role("button", name="Open dialog").click()
    time.sleep(6)
    page.locator("iframe[name=\"frame-b6812b6c13fff16861f2645c4100ae5b\"]").content_frame.get_by_role("button", name="Deactivate").click()
