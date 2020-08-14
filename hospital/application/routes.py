from application import app,db
from flask import render_template,flash,json,request,redirect,url_for,session
from application.form import LoginForm, DeleteForm, CreateForm, DelForm, SeaForm, SearchForm, UpdateForm, UpForm, IssueForm, FindmedsForm
import config
from application.models import User, Patient, Medicines, Purdetails
from werkzeug.security import generate_password_hash, check_password_hash
import secrets, string, random
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms.validators import ValidationError
import datetime

N=9

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

		
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password==form.password.data:
				login_user(user)
				return redirect(url_for('properhome'))
			else:
				flash('Incorrect password, try again','danger')
				return redirect(url_for('login'))
		else:
			flash('Invalid username','danger')
			return redirect(url_for('login'))
	return render_template('login.html', form=form)
	
	
@app.route('/properhome',methods=['GET','POST'])
@login_required
def properhome():
	return render_template("properhome.html")

	
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
	form = CreateForm()
	if request.method=='POST' and form.validate_on_submit():
		result = Patient.query.filter_by(pid=form.pid.data).first()
		if result:
				flash('Patient already exists!','danger')
				return redirect(url_for('create'))
		else:
			autopid = ''.join(secrets.choice(string.digits) 
														  for i in range(N))
			x= datetime.datetime.strptime(request.form.get('doa'), '%Y-%m-%d')
			newp = Patient(autopid=autopid, pid=request.form.get('pid'), name=request.form.get('name'),
			age=request.form.get('age'), doa=x.date(),
			tob=request.form.get('tob'), address=request.form.get('address'),
			state=request.form.get('state'), city=request.form.get('city'), status='Active')         
			db.session.add(newp)
			db.session.commit()
			flash('Patient creation initiated successfully','success')
			return redirect(url_for('properhome'))
	return render_template('create.html',title='CREATE PATIENT',form=form)


@app.route("/delete", methods=['GET','POST'])
@login_required
def delete():
    form=DelForm()
    if request.method=='POST' and form.validate_on_submit():
        result = Patient.query.filter_by(pid=form.pid.data).first()
        if result:
            if request.form['action'] == 'get':
                #pid=form.pid.data
                session['pid'] =form.pid.data
                return redirect(url_for('get'))
            else:
                return redirect(url_for('properhome'))
        else:
            flash('Patient not found','danger')
            return redirect(url_for('delete'))
    return render_template("delete.html",form=form,delete=True)
	

@app.route("/get",methods=['GET','POST'])
def get():
    pid= session.get('pid', None)
    u=Patient.query.filter_by(pid=pid).first()
    form= DeleteForm(formdata=request.form, obj=u)
    if u:
        if request.method=='POST':
            db.session.delete(u)
            db.session.commit()
            flash('Record was deleted successfully ')
            return redirect(url_for('properhome'))
        return render_template("get.html",form=form)
    else:
        return redirect(url_for('properhome'))
    return render_template("get.html",form=form,delete=True)
	
	
@app.route("/search",methods=['GET','POST'])
@login_required
def search():
    form=SeaForm()
    #form1=SearchForm()
    if request.method=='POST' and form.validate_on_submit():
        result = Patient.query.filter_by(pid=form.pid.data).first()
        if result:
            session['pid'] =form.pid.data
            return redirect(url_for("search1"))
        else:
            flash('Patient not found','danger')
            return redirect(url_for('search'))
    return render_template("search.html",form=form,title=search)
	

@app.route('/search1')
@login_required
def search1():
    pid= session.get('pid', None)
    u=Patient.query.filter_by(pid=pid).first()
    form= SearchForm(formdata=request.form, obj=u)
    if u:
        return render_template("search1.html",form1=form)
    else:
        return "bye"
    return render_template("search1.html",form1=form)
   
@app.route('/update',methods=['GET','POST'])
@login_required
def update():
    form=UpForm()
    if request.method=='POST' and form.validate_on_submit():
        result = Patient.query.filter_by(pid=form.pid.data).first()
        if result:
            if request.form['action'] == 'get':
                #pid=form.pid.data
                session['pid'] =form.pid.data
                return redirect(url_for('getup'))
            else:
                return redirect("properhome.html")
        else:
            flash('Patient not found','danger')
            return redirect(url_for('update'))
    return render_template("update.html",title="Update Customer",form=form,Update=True)


@app.route("/getup",methods=['GET','POST'])
@login_required
def getup():
    pid= session.get('pid', None)
    u=Patient.query.filter_by(pid=pid).first()
    form= UpdateForm(formdata=request.form, obj=u)
    if u:
        if request.method=='POST' and form.validate_on_submit():           
			#y, m, d = form.doa.data.split('-')
			#date = datetime.datetime(int(y), int(m), int(d))
            x= datetime.datetime.strptime(request.form.get('doa'), '%Y-%m-%d')
            u.name=request.form.get('name')
            u.age=request.form.get('age')
            u.doa=x.date()
            u.tob=request.form.get('tob')
            u.address=request.form.get('address')
            u.state=request.form.get('state')
            u.city=request.form.get('city')
            db.session.add(u)
            db.session.commit()
            flash('Record was updated successfully ')
            return redirect(url_for('properhome'))
        return render_template("getup.html",form=form)
    else:
        return "bye"
    return render_template("getup.html",form=form,update=True)
	
	
@app.route("/pharmsearch", methods=['GET','POST'])
@login_required
def pharmsearch():
    form=DelForm()
    if request.method=='POST' and form.validate_on_submit():
        result = Patient.query.filter_by(pid=form.pid.data).first()
        if result:
            session['pid'] =form.pid.data
            return redirect(url_for('pharmget'))
        else:
            flash('Patient not found','danger')
            return redirect(url_for('pharmsearch'))
    return render_template("pharmsearch.html",form=form)
	
	
@app.route("/pharmget",methods=['GET','POST'])
@login_required
def pharmget():
	pid= session.get('pid', None)
	tempmeds=[]
	u=Patient.query.filter_by(pid=pid).first()
	form=IssueForm()
	if u:
		records = Purdetails.query.filter_by(pid=pid).all()
		session['tempmeds']=tempmeds
		return render_template("issuemeds.html",form=form,res=u,records=records)
		#if request.method=='POST':
		#	return redirect(url_for('selectmeds'))
		#return render_template("issuemeds.html",form=form)
	else:
		flash('Patient not found','danger')
		return redirect(url_for('properhome'))
	return render_template("issuemeds.html",form=form,res=u)

	
@app.route('/selectmeds',methods=['GET','POST'])
@login_required
def selectmeds():
	form=FindmedsForm()
	tempmeds=session.get('tempmeds',None)
	if form.validate_on_submit():
		med = Medicines.query.filter_by(medname=form.name.data).first()
		if med:				
			if med.qtyav>=form.qty.data:
				if len(tempmeds)==0:
					#return 'dhdmu'
					flash('Medicine available','success')
					n=med.medname
					q=request.form.get('qty')
					r=med.rate
					amt=med.rate*float(q)
					newlist=[n,q,r,amt]
					med.qtyav=med.qtyav-int(q)
					tempmeds.append(newlist)
					#tempmeds=[newlist]
					return render_template("selectmeds.html",form=form,res=tempmeds)
				else:
					for list in tempmeds:
						if list[0]==form.name.data:
							#return 'dgjuktuta'
							list[1]=int(list[1])+form.qty.data
							q=request.form.get('qty')
							med.qtyav=med.qtyav-int(q)
							r=med.rate
							list[3]=float(list[3])+med.rate*float(q)
							flash('Medicine available','success')
							return render_template("selectmeds.html",form=form,res=tempmeds)
							#return 'dgjuktutb'
					flash('Medicine available','success')
					n=med.medname
					q=request.form.get('qty')
					med.qtyav=med.qtyav-int(q)
					r=med.rate
					amt=med.rate*float(q)
					newlist=[n,q,r,amt]
					tempmeds.append(newlist)
					return render_template("selectmeds.html",form=form,res=tempmeds)
			else:
				#return 'dgjuktutc'
				flash('Oops!Required quantity not available','danger')
				return redirect(url_for('selectmeds'))
		else:
			#return 'dgjuktut'
			flash('Sorry!Medicine not available','danger')
			return redirect(url_for('selectmeds'))
	return render_template("selectmeds.html",form=form)
	
	
@app.route('/storemeds',methods=['GET','POST'])
@login_required
def storemeds():
	pid= session.get('pid', None)
	tempmeds=session.get('tempmeds',None)
	for list in tempmeds:
		m = Medicines.query.filter_by(medname=list[0]).first()
		x = Purdetails(pid=pid, medid=m.medid, medname=list[0], qtypur=list[1], rate=list[2], amt=list[3])
		db.session.add(x)
		db.session.commit()
	flash('Medicine issued successfully','success')
	#session.pop('tempmeds',None)
	u=Patient.query.filter_by(pid=pid).first()
	#ans = Purdetails.query.filter_by(pid=pid).first()
	records = Purdetails.query.filter_by(pid=pid).all()
	if u and records:
		return render_template("finalmeds.html",res=u,records=records)
	return render_template("finalmeds.html")
	
	

@app.route("/view")
@login_required
def view():
	return render_template("view.html",patients = Patient.query.all())
	
	
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
	

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
	
	

    