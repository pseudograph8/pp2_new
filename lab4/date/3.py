'''
Write a Python program to drop microseconds from datetime.
'''

import datetime

datat = datetime.datetime.today().replace(microsecond=0)
print(datat)

