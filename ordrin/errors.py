class OrdrinError(Exception):
  def __init__(self, msg=None):
    self.msg = msg

class ApiError(OrdrinError):
  def __init__(self, msg=None, text=None):
    OrdrinError.__init__(self, msg)
    self.text = text

class BadValueError(OrdrinError, ValueError):
  def __init__(self, msg):
    OrdrinError.__init__(self, msg)
    ValueError.__init__(self, msg)

def state(value):
  return BadValueError("State must be a two letter postal code abbreviation: {}".format(value))

def money(value):
  return BadValueError("Money values must be dollars.cents: {}".format(value))

def zip_code(value):
  return BadValueError("Zip code must be exactly 5 digits: {}".format(value))

def phone(value):
  return BadValueError("Phone numbers must have exactly 10 digits: {}".format(value))

def number(value):
  return BadValueError("This value must be only digits: {}".format(value))

def month(value):
  return BadValueError("Months must be two digits: {}".format(value))

def year(value):
  return BadValueError("Years must be four digits: {}".format(value))

def cvc(value):
  return BadValueError("Credit card CVC must be 3 or 4 digits: {}".format(value))

def email(value):
  return BadvalueError("Bad email format: {}".format(value))

def normalizer(value):
  return BadValueError("Unknown validator name: {}".format(value))

def nick(value):
  return BadValueError("Nick names can only have letters, nubmers, dashes, and underscores: {}".format(value))

def date_time(value):
  return BadValueError("date_time must be a datetime.datetime object or the string 'ASAP': {}".format(value))

def date(value):
  return BadValueError("date must be a datetime.datetime or datetime.date object or the string 'ASAP': {}".format(value))

def time(value):
  return BadValueError("time must be a datetime.datetime or datetime.time object: {}".format(value))
