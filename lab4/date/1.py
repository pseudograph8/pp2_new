'''
Write a Python program to subtract five days from current date.
'''

from datetime import date, timedelta

five_days_ago = date.today() - timedelta(5)
print('Today:',date.today())
print('5 days ago:',five_days_ago)