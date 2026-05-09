class Test:
    @staticmethod
    def assert_equals(actual, expected, msg=None):
        if actual != expected:
            details = f"Expected {expected}, got {actual}"
            raise AssertionError(f"{msg}: {details}" if msg else details)
        prefix = f"{msg} - " if msg else ""
        print(f"{prefix}[PASS] {actual} == {expected}")

