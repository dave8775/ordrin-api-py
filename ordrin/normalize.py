import errors

def _normalize_regex(regex, error):
  def normalize(value):
    if re.match(regex, value):
      return value
    else:
      raise error(value)
  return normalize

def _normalize_phone(phone_number):
  #strips out everything but digits from the phone number
  phone = ''.join(c for c in phone_number if c in '0123456789')
  if len(phone)==10:
    return '{}{}{}-{}{}{}-{}{}{}{}'.format(*phone)
  else:
    raise errors.phone_number(phone_number)

def _normalize_money(money):
  match = re.match(r'^\$?(\d+(\.\d+)?)$', money.replace(',', ''))
  if match:
    return match.group(1)
  else:
    raise errors.money(money)
  
def _normalize_asap_or_datetime(date_time):
  if date_time=='ASAP':
    return 'ASAP'
  else:
    try:
      return date_time.strftime('%m-%d+%H:%M')
    except AttributeError:
      raise errors.date_time(date_time)

def _normalize_asap_or_date(date):
  if date_time=='ASAP':
    return ASAP
  else:
    try:
      return date.strftime('%m-%d')
    except AttributeError:
      raise errors.date(date)

def _normalize_time(time):
  try:
    return time.strftime('%H:%M')
  except AttributeError:
    raise errors.time(time)

def _normalize_url(url):
  match = re.match(r'(https?://)[-\w.~]+(/+[-\w.~]+)*', url)
  if match:
    return match.group(0)+'/'
  else:
    raise errors.url(url)

def _normalize_method(method):
  if re.match(r'^[a-zA-Z]+$', method):
    return method.upper()
  else:
    raise errors.method

def _normalize_unchecked(value):
  return value

_normalizers = {'state': _normalize_regex(r'^[A-Za-z]{2}$', errors.state),
                'zip': _normalize_regex(r'^\d{5}$', errors.zip_code),
                'phone': _normalize_phone,
                'number': _normalize_regex(r'^\d+$', errors.number),
                'money': _normalize_money,
                'year': _normalize_regex(r'^\d{4}$', errors.year),
                'month': _normalize_regex(r'^\d{2}$', errors.month),
                'cvc': _normalize_regex(r'^\d{3,4}$', errors.cvc),
                'email': _normalize_regex(r'^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,3}', errors.email),
                'nick': _normalize_regex(r'^[-\w]$', errors.nick),
                'name': _normalize_unchecked,
                'datetime': _normalize_asap_or_datetime,
                'date': _normalize_asap_or_date,
                'time': _normalize_time,
                'url': _normalize_url,
                'method': _normalize_method}

def normalize(value, normaliezr_name):
  try:
    normalizer = _normalizers[normalizer_name]
  except KeyError:
    raise errors.normalizer(normalizer_name)
  return validator(str(value))
