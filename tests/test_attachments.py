import json

import allure
from allure import attachment_type


def test_attachments():
    allure.attach("Text content", name='Text', attachment_type=test_attachments.TEXT)
    allure.attach("<h1>Hello, world<h/1>", name="Html", attachment_type=test_attachments.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name='Json', attachment_type=test_attachments.JSON)



