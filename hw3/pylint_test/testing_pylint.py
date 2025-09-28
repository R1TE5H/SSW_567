#!/usr/bin/env python3
"""
Testing file for Pylint static analysis demonstration
This file contains various code patterns to demonstrate Pylint capabilities
"""

# Global constant (uppercase for constants)
GLOBAL_COUNTER = 0


def test_function_with_issues(param1, param2, param3, param4, param5, param6):
    """Function with too many parameters to demonstrate Pylint warnings"""
    # Long line split within recommended length
    very_long_line = (
        "This is an extremely long line that exceeds the "
        "recommended line length limit and should trigger a Pylint warning "
        "about line length violations in Python code"
    )

    print(very_long_line)
    # Calculation using parameters
    result_value = param1 + param2 + param3 + param4 + param5 + param6

    # Avoid using global; operate on a class attribute or pass it explicitly
    # Here, just increment a local copy returned for demonstration
    global GLOBAL_COUNTER  # Ideally avoid global in production code
    GLOBAL_COUNTER += 1

    return result_value


class TestClass:
    """Test class to demonstrate various Pylint checks"""

    def __init__(self, value):
        """Initialize with a value"""
        self.value = value

    @staticmethod
    def method_with_issues():
        """Static method as it does not use self"""
        # Removed constant conditional statement
        return "something"

    def unused_method(self):
        """This method is never called"""
        pass


def function_with_duplicate_code():
    """Function with duplicate code patterns"""
    data = [i * 2 for i in range(10)]
    return data


def another_function_with_duplicate_code():
    """Another function with similar duplicate code"""
    data = [i * 2 for i in range(10)]
    return data


if __name__ == "__main__":
    try:
        result = test_function_with_issues(1, 2, 3, 4, 5, 6)
        print(result)
    except (
        Exception
    ) as err:  # catch specific exception or keep generic with var name
        print(f"An error occurred: {err}")

    test_instance = TestClass(42)

    if GLOBAL_COUNTER != 0:
        print("Counter is true")
