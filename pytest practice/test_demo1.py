# any pytest file should start with test
# pytest method names should start with test
# any code should be wrapped in method
# to run, get the file path by right-clicking the folder, open cmd and type cd then paste the path
# type py.test
# to run a specific file, type py.test space filename
# to run a specific test case, type py.test -k (method name) -v -s
# to run with mark, type py.test -m (smoke) -v -s
# to skip a test case, add @pytest.mark.skip on top of the test case
# @pytest.mark.xfail is used to exclude the test case in the report
# to create a report, type in cmd py.test html=(report).html
import pytest

@pytest.mark.smoke
def test_firstprogram():
    print("hello")
