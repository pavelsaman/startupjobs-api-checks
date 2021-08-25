from Configuration.Config import Config


def pytest_configure(config):
    config._metadata['Env'] = Config.env()
    config._metadata['Base Url'] = Config.base_url()


def pytest_html_report_title(report):
    report.title = Config.REPORT_TITLE
