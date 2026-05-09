import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import testutils
from solution import move

testutils.Test.assert_equals(move("hello"), "ifmmp")
testutils.Test.assert_equals(move("lol"), "mpm")
testutils.Test.assert_equals(move("bye"), "czf")

print("\nFinished all tests.")
