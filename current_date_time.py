"""
Ashleigh Berry
Module 08 Lab Assignment
Part B

This program gives the current date and time
"""
from datetime import datetime, timedelta
now = datetime.now()
print(now)
tomorrow = datetime.now() + timedelta(1)
print(tomorrow)