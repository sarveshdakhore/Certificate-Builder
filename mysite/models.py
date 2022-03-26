from enum import unique
from operator import truediv
import pandas as pd
from setup import *
from timest import current_time, startTIime

class certificateInfo(dab.Model):
    id = dab.Column(dab.Integer, primary_key=True, autoincrement=True)
    name=dab.Column(dab.String(50), nullable=False,default="")
    certificate_code=dab.Column(dab.String, nullable=False,unique=True)
    event = dab.Column(dab.String(50), nullable=False,default="")
    catagory=dab.Column(dab.String(50), nullable=False,default="")
    issue_date=dab.Column(dab.String(50), nullable=False,default=str(current_time()))
    certificate_design_id=dab.Column(dab.String, nullable=False,default="")
    special=dab.Column(dab.Boolean,nullable=False,default=False)
    school_reg=dab.Column(dab.Boolean,nullable=False,default=False)
    school_name=dab.Column(dab.String, nullable=False,default="")
    position_bool=dab.Column(dab.Boolean,nullable=False,default=False)
    position=dab.Column(dab.String, nullable=True)
    description=dab.Column(dab.String, nullable=False,default="")
    extra1=dab.Column(dab.String, nullable=True)
    extra2=dab.Column(dab.String, nullable=True)
    extra3=dab.Column(dab.String, nullable=True)
    extra4=dab.Column(dab.String, nullable=True)
    # 1) if is "T" true then extra content will be showed,elif only "F" the field will be ignored....
    # 2) if is "T" then then the content will be showed, if "F" then the extra content from flask_alchemy data will be showed

    def __repr__(self):
        return f"certificateInfo('{self.name}','{self.certificate_code}', '{self.certificate_design_id}','{self.issue_date}')"

class designInfo(dab.Model):
    certDesignID=dab.Column(dab.String, nullable=False,primary_key=True)
    certificateCodeXYL=dab.Column(dab.String, nullable=False)
    nameXYL=dab.Column(dab.String, nullable=True)
    catagoryXYL=dab.Column(dab.String, nullable=True)
    positionXYL=dab.Column(dab.String, nullable=True)
    schoolNameXYL=dab.Column(dab.String, nullable=True)
    date=dab.Column(dab.String, nullable=False,default=str(current_time()))
    extra1XYL=dab.Column(dab.String, nullable=True)
    extra2XYL=dab.Column(dab.String, nullable=True)
    extra3XYL=dab.Column(dab.String, nullable=True)
    extra4XYL=dab.Column(dab.String, nullable=True)
    maxFontSize=dab.Column(dab.Integer, nullable=False)
    font=dab.Column(dab.String, nullable=False,default="alice_regular.ttf")
    fontColorRGB=dab.Column(dab.String, nullable=False,default="0;0;0")
    description=dab.Column(dab.String, nullable=False,default="F")

    def __repr__(self):
        return f"designInfo('{self.certDesignID}','{self.font}','{self.date}')"



class deleteInfo(dab.Model):
    certificateCode=dab.Column(dab.String, nullable=False,primary_key=True)
    design_time=dab.Column(dab.Integer, default=startTIime())

    def __repr__(self):
        return f"deleteInfo('{self.certificateCode}','{self.design_time}')"


"""dab.create_all()
toAdd=designInfo(certDesignID="P12",certificateCodeXYL="0;0;150",	nameXYL="1085;774;630",	catagoryXYL="150;922;435",	positionXYL="1310;850;245",	schoolNameXYL="394;845;677",	extra1XYL="T/F;T/F;Content;X;Y;L",	extra2XYL="T/F;T/F;Content;X;Y;L",	extra3XYL="T/F;T/F;Content;X;Y;L",	extra4XYL="T/F;T/F;Content;X;Y;L",	maxFontSize=60,		description="T;content")
dab.session.add(toAdd)
dab.session.commit()"""
