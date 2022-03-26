from datetime import datetime
import pytz
def current_time():
	return datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d/%m/%Y')

def timeStamp():
  return datetime.now(pytz.timezone('Asia/Kolkata'))

import time


def startTIime():
  return int(time.time())

def timeTaken(c_User):
  return (int(time.time())-int(c_User.design_time))
