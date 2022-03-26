from models import *
import os
from timest import timeTaken
data= deleteInfo.query.all()
for i in data:
  if timeTaken(i) > 1800:
    try:
      os.remove("/home/dpscertificate/mysite/static/"+str(i.certificateCode))
      dab.session.delete(i)
      dab.session.commit()
    except:
      pass
  else:
    pass

