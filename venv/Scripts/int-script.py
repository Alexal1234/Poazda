#!C:\Users\Сергей\PycharmProjects\poezda\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'int==3.2.0','console_scripts','int'
__requires__ = 'int==3.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('int==3.2.0', 'console_scripts', 'int')()
    )
