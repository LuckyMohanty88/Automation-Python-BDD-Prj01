import json
import os

from mss import mss  # Takes a screenshot of monitor

from utils.browsers import browsers
from utils.paths import project_path



def before_scenario(context, scenario):
    context.browser = browsers(context, context.config.userdata.get("browser", 'chrome'))


def after_scenario(context, scenario):
    if scenario.status.name != 'passed':
        if not os.path.isdir(project_path.join("screenshots").strpath):
            os.mkdir(project_path.join("screenshots").strpath)
        context.browser.save_screenshot(project_path.join("screenshots",
                                                          f"{context.scenario.name}_screenshot.png").strpath)
    context.browser.quit()