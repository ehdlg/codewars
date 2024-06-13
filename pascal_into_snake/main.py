"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
Examples

"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"

"""


def to_underscore(camel):
    camel = str(camel)
    if len(camel) == 1:
        return str(camel)

    snake = camel[0].lower()

    for letter in camel[1:]:
        if letter.isupper():
            snake += f"_{letter.lower()}"
        else:
            snake += letter

    return snake


print(to_underscore("HolaMundo"))
