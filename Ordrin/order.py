class Order(object):

  def __init__(url):
    """Initializes this API class with the url that it accesses"""
    ordrin.OrdrinAPI.__init__(self, url)

  def order(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, email, credit_card, login=None):
    data = {'restaurant_id':restaurant_id, 'tray':str(tray), 'tip':tip}
    data['delivery_date'] = _get_asap_or_date(delivery_date_time)
    if data['delivery_date'] != 'ASAP':
      data['delivery_time'] = delivery_date_time.strftime('%H:%M')
    data['first_name'] = first_name
    data['last_name'] = last_name
