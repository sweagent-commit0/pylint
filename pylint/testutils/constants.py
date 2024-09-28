import operator
import re
import sys
from pathlib import Path
SYS_VERS_STR = '%d%d%d' % sys.version_info[:3]
TITLE_UNDERLINES = ['', '=', '-', '.']
UPDATE_OPTION = '--update-functional-output'
UPDATE_FILE = Path('pylint-functional-test-update')
_MESSAGE = {'msg': '[a-z][a-z\\-]+'}
_EXPECTED_RE = re.compile('\\s*#\\s*(?:(?P<line>[+-]?[0-9]+):)?(?:(?P<op>[><=]+) *(?P<version>[0-9.]+):)?\\s*\\[(?P<msgs>{msg}(?:,\\s*{msg})*)]'.format(**_MESSAGE))
_OPERATORS = {'>': operator.gt, '<': operator.lt, '>=': operator.ge, '<=': operator.le}