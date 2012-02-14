class WrongNumberException(Exception):
    msg = 'Wrong number.'

class OperatorNotFoundException(Exception):
    msg = 'Operator not found.'

class NotPostRequestException(Exception):
    msg = 'Only post methods allowed.'
