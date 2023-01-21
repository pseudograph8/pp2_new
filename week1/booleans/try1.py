print(bool("Hello"))
print(bool(15))

bool("abc")
bool(123)
print(bool(["apple", "cherry", "banana"]))

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""