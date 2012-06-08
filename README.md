Ordr.in Python API
==================

A Python wrapper for the Restaurant, User, and Order APIs provided by Ordr.in. Everything mentioned here is described in more detail in the documentation in the python modules. The main API documentation can be found at http://ordr.in/developers.

Data Structures
---------------

```python
ordrin.data.Address(addr, city, state, zip, phone, addr2='')

ordrin.data.CreditCard(name, expiry_month, expiry_year, bill_address, number, cvc)

ordrin.data.UserLogin(email, password)

ordrin.data.TrayItem(item_id, quantity, *options)

ordrin.data.Tray(*items)
```

Exceptions
----------

```python
ordrin.errors.ApiError(msg, text)

ordrin.errors.ApiInvalidResponseError(msg)

ordrin.errors.BadValueError(msg)
```

API Initialization
------------------

```python
api = ordrin.APIs(developer_key, restaurant_url, user_url, order_url)
```

Restaurant API Functions
------------------------

```python
api.restaurant.get_delivery_list(date_time, address)

api.restaurant.get_delivery_check(retaurant_id, date_time, address)

api.restaurant.get_fee(restaurant_id, subtotal, tip, date_time, address)

api.restaurant.get_details(restaurant_id)
```

User API Functions
------------------

```python
api.user.get(login)

api.user.create(login, first_name, last_name)

api.user.update(login, first_name, last_name)

api.user.get_all_addresses(login)

api.user.get_address(login, addr_nick)

api.user.set_address(login, addr_nick, address)

api.user.remove_address(login, addr_nick)

api.user.get_all_credit_cards(login)

api.user.get_credit_card(login, card_nick)

api.user.set_credit_card(login, card_nick, credit_card)

api.user.remove_credit_card(login, card_nick)

api.user.get_order_history(login)

api.user.get_order_detail(login, order_id)

api.user.set_password(login, new_password)
```

Order API Functions
-------------------

```python
api.order.order(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, credit_card, email=None, login=None)

order_create_user(restaurant_id, tray, tip, delivery_date_time, first_name, last_name, address, credit_card, email, password)
```