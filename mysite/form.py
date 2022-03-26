from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from certificate_maker import *



class takeCode(FlaskForm):
    takeCertificateCode = StringField('Certification Code', validators=[DataRequired(),Length(max=11,min=11,message="Field must be exactly 9 characters long.")],render_kw={"placeholder": "XXX-XXX-XXX"})
    submit = SubmitField('  Check Certification  ')
    def validate_takeCertificateCode(self, takeCertificateCode):
        if certificateInfo.query.filter_by(certificate_code=takeCertificateCode.data.upper()).first():
            pass
        else:
            raise ValidationError("Invalid Certificate Code !!!")