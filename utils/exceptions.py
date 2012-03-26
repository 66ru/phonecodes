class InvalidNumberException(Exception):
    code = 1
    msg = 'Invalid number.'

class OperatorNotFoundException(Exception):
    code = 2
    msg = 'Operator not found.'

