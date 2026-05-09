from solution import encrypt
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import testutils

print("Testing", "karaca")
testutils.Test.assert_equals(encrypt("karaca"), "0c0r0kaca")
print("Testing", "burak")
testutils.Test.assert_equals(encrypt("burak"), "k0r3baca")
print("Testing", "banana")
testutils.Test.assert_equals(encrypt("banana"), "0n0n0baca")
print("Testing", "alpaca")
testutils.Test.assert_equals(encrypt("alpaca"), "0c0pl0aca")
print("Testing", "hello")
testutils.Test.assert_equals(encrypt("hello"), "2ll1haca")