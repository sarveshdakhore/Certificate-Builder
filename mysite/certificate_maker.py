import os
path = ""
from os import name
from models import *
import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def strintToList(string):
  finalList=[]
  for i in list(string.split(';')):
    if i.isnumeric():
      finalList.append(int(i))
    else:
      finalList.append(i)
  return (finalList)



def dataAdder(file):
  df=pd.read_csv(file)
  dataToAdd= df.values.tolist()
  for i in dataToAdd:
    if certificateInfo.query.filter_by(certificate_code=i[1].upper()).first():
      pass
    else:
      if i[5].upper()=="T":
        spectialBool = True
      else:
        spectialBool = False

      if i[-7]!="" or str(i[-7])!="nan":
        schoolReg=True
        schoolp=i[-7]
      else:
        schoolReg=True
        schoolp=""

      if i[-6].upper()!="" and str(i[-6])!="nan":
        psn = True
        psn1=i[-6]
      else:
        psn = False
        psn1=""

      if i[-5]!="" or str(i[-5])!="nan":
        desc=i[-5]
      else:
        desc=""

      if i[-1]!="" or str(i[-1])!="nan":
        ex4=i[-1]
      else:
        ex4=""

      if i[-2]!="" or str(i[-2])!="nan":
        ex3=i[-5]
      else:
        ex3=""

      if i[-3]!="" or str(i[-3])!="nan":
        ex2=i[-3]
      else:
        ex2=""

      if i[-4]!="" or str(i[-4])!="nan":
        ex1=i[-4]
      else:
        ex1=""
      toAdd=certificateInfo(description=desc,position_bool=psn,position=psn1,school_name=schoolp,school_reg=schoolReg,name=i[0],certificate_code=i[1].upper(),event=i[2],catagory=i[3],certificate_design_id=i[4],extra1=ex1,extra2=ex2,extra3=ex3,extra4=ex4)
      dab.session.add(toAdd)
      dab.session.commit()



def make_certificate(certificateID):
  holder=certificateInfo.query.filter_by(certificate_code=certificateID).first()
  certificateDesignID=holder.certificate_design_id
  design=designInfo.query.filter_by(certDesignID=certificateDesignID).first()

  nameXYL=strintToList(design.nameXYL)
  catagoryXYL=strintToList(design.catagoryXYL)
  positionXYL=strintToList(design.positionXYL)
  schoolXYL=strintToList(design.schoolNameXYL)
  certificateCodeXYL=strintToList(design.certificateCodeXYL)

  extra1BBCXYL= strintToList(design.extra1XYL)
  extra2BBCXYL= strintToList(design.extra2XYL)
  extra3BBCXYL= strintToList(design.extra3XYL)
  extra4BBCXYL= strintToList(design.extra4XYL)

  font = path+"certificate_fonts/"+str(design.font)
  fontColorRGB=design.fontColorRGB
  maxFontSize=design.maxFontSize

  img = Image.open(path + "certificate_design/"+str(certificateDesignID)+".png")

  # Font size Adjusment
  def fontSizeIs(font,maxFontSize,length,inputValue):
    for i in range(maxFontSize,5,-1):
      if ImageFont.truetype(font, i).getsize(inputValue)[0]>length:   #(x,y) x- width in px and y- height in px
        pass
      else:
        return (int(i))

  def YAxisCalculater(font,maxFontSize,length,YAxisDefault,inputValue):
    currentHeight=ImageFont.truetype(font, fontSizeIs(font,maxFontSize,length,inputValue)).getsize(inputValue)[1]
    orignalHeight=ImageFont.truetype(font, maxFontSize).getsize(inputValue)[1]
    newYAxis=((int(orignalHeight)-int(currentHeight)))+YAxisDefault
    return int(newYAxis)

  I1 = ImageDraw.Draw(img)
  rgb=strintToList(fontColorRGB)

  #Draw Name
  myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,nameXYL[2],holder.name))
  I1.text((nameXYL[0], YAxisCalculater(font,maxFontSize,nameXYL[2],nameXYL[1],holder.name)), holder.name, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))

  #Draw Code
  myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,nameXYL[2],holder.certificate_code))
  I1.text((certificateCodeXYL[0], YAxisCalculater(font,maxFontSize,certificateCodeXYL[2],certificateCodeXYL[1],holder.certificate_code)), holder.certificate_code, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))

  #Draw School Name
  if holder.school_reg==True:
    myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,schoolXYL[2],holder.school_name))
    I1.text((schoolXYL[0], YAxisCalculater(font,maxFontSize,schoolXYL[2],schoolXYL[1],holder.school_name)), holder.school_name, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
  else:
    pass

  #Draw Position
  if holder.position_bool==True:
    myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,positionXYL[2],holder.position))
    I1.text((positionXYL[0], YAxisCalculater(font,maxFontSize,positionXYL[2],positionXYL[1],holder.position)), holder.position, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
  else:
    pass

  #Draw Event
  myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,catagoryXYL[2],holder.catagory))
  I1.text((catagoryXYL[0], YAxisCalculater(font,maxFontSize,catagoryXYL[2],catagoryXYL[1],holder.catagory)), holder.catagory, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))



  #Draw extra1
  if extra1BBCXYL[0].upper()=="T":
    if extra1BBCXYL[1].upper()=="T":
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra1BBCXYL[-1],extra1BBCXYL[2]))
      I1.text((extra1BBCXYL[-3], YAxisCalculater(font,maxFontSize,extra1BBCXYL[-1],extra1BBCXYL[-2],extra1BBCXYL[2])), extra1BBCXYL[2], font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
    else:
      if len(extra1BBCXYL)==6:
        content=str(extra1BBCXYL[2])+str(holder.extra1)
      else:
        content=str(holder.extra1)
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra1BBCXYL[-1],content))
      I1.text((extra1BBCXYL[-3], YAxisCalculater(font,maxFontSize,extra1BBCXYL[-1],extra1BBCXYL[-2],content)), content, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
  else:
    pass


  #Draw extra2
  if extra2BBCXYL[0].upper()=="T":
    if extra2BBCXYL[1].upper()=="T":
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra2BBCXYL[-1],extra2BBCXYL[2]))
      I1.text((extra2BBCXYL[-3], YAxisCalculater(font,maxFontSize,extra2BBCXYL[-1],extra2BBCXYL[-2],extra2BBCXYL[2])), extra2BBCXYL[2], font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
    else:
      if len(extra2BBCXYL)==6:
        content=str(extra2BBCXYL[2])+str(holder.extra2)
      else:
        content=str(holder.extra2)
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra2BBCXYL[-1],content))
      I1.text((extra2BBCXYL[-3], YAxisCalculater(font,maxFontSize,extra2BBCXYL[-1],extra2BBCXYL[-2],content)), content, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
  else:
    pass


  #Draw extra3
  if extra3BBCXYL[0].upper()=="T":
    if extra3BBCXYL[1].upper()=="T":
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra3BBCXYL[-1],extra3BBCXYL[2]))
      I1.text((extra3BBCXYL[-3], YAxisCalculater(font,maxFontSize,extra3BBCXYL[-1],extra3BBCXYL[-2],extra3BBCXYL[2])), extra3BBCXYL[2], font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
    else:
      if len(extra3BBCXYL)==6:
        content=str(extra3BBCXYL[2])+str(holder.extra3)
      else:
        content=str(holder.extra3)
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra3BBCXYL[-1],content))
      I1.text((extra3BBCXYL[-3], YAxisCalculater(font,maxFontSize,extra3BBCXYL[-1],extra3BBCXYL[-2],content)), content, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
  else:
    pass



  #Draw extra4
  if extra4BBCXYL[0].upper()=="T":
    if extra4BBCXYL[1].upper()=="T":
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra4BBCXYL[-1],extra4BBCXYL[2]))
      I1.text((extra4BBCXYL[-3], extra4BBCXYL[-2]), YAxisCalculater(font,maxFontSize,extra4BBCXYL[-1],extra4BBCXYL[-2],extra4BBCXYL[2]), font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
    else:
      if len(extra4BBCXYL)==6:
        content=str(extra4BBCXYL[2])+str(holder.extra4)
      else:
        content=str(holder.extra4)
      myFont = ImageFont.truetype(font, fontSizeIs(font,maxFontSize,extra4BBCXYL[-1],content))
      I1.text((extra4BBCXYL[-3], YAxisCalculater(font,maxFontSize,extra4BBCXYL[-1],extra4BBCXYL[-2],content)), content, font=myFont, fill = (rgb[0],rgb[1],rgb[2]))
  else:
    pass

  img.save(path + "static/"+str(holder.certificate_code)+".png")
  if deleteInfo.query.filter_by(certificateCode=str(holder.certificate_code)+".png").first():
    pass
  else:
    toAdd=deleteInfo(certificateCode=str(holder.certificate_code)+".png")
    dab.session.add(toAdd)
    dab.session.commit()
