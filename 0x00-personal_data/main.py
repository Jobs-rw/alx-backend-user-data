#!/usr/bin/env python3
"""
"""
Main file
"""
'''
import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter
filter_datum = __import__('filtered_logger').filter_datum
get_db = __import__('filtered_logger').get_db
hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
"""
password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(hash_password(password))
print(hash_password(password))
print(encrypted_password)
print(is_valid(encrypted_password, password))
