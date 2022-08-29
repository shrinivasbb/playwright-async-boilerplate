def pytest_addoption(parser):
   parser.addoption('--browser', action = 'store', help = 'Enter Browser Name e.g. firefox, chrome, chromium etc.')