from form import *

@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    form = takeCode()
    if form.validate_on_submit():
        currentHolder=certificateInfo.query.filter_by(certificate_code=form.takeCertificateCode.data.upper()).first()
        if currentHolder:
            if currentHolder.special==True:
                return render_template('certificate.html',currentHolder=currentHolder,special=True,descrpt=desp(currentHolder.certificate_design_id))
            else:
                import delete
                make_certificate(str(currentHolder.certificate_code))
            return render_template('certificate.html',currentHolder=currentHolder,descrpt=desp(currentHolder.certificate_design_id))

    return render_template('home.html',takeCodeForm=form)




