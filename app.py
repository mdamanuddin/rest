from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///hello.db' #database file (sqlite) this will create file in the project folder
dbase=SQLAlchemy(application)

class User(dbase.Model):
    id=dbase.Column(dbase.Integer,primary_key=True)
    name=dbase.Column(dbase.String(255)) # It will help in creating database in the sqlite database
    def __repr__(self):
        return '<Name %r>' % self.name #if you print this object it will output the name and not the id
@application.route('/')
def index():
    #if(request.method =='POST'):
        #userinput= request.get_json()
        #return jsonify({'You typed':userinput}),202 #I set response code to 202
    #else:
    return "<h4> Usage: http://0.0.0.0:5000/hello/&ltstring&gt </h4>"

@application.route('/hello')
def hello():
    #if(request.method =='POST'):
        #userinput= request.get_json()
        #return jsonify({'You typed':userinput}),202 #I set response code to 202
    #else:
    return jsonify('Hello Stranger!')
@application.route('/hello/<string:var>')
def retr(var):
    vr=User(name=var)
    dbase.session.add(vr)   #write the name to the database
    dbase.session.commit()  #commit the string name to database
    var1='hello'+' '+var
    return jsonify(var1) #return the string entered at the RESTFULL endpoint as JSON data
@application.route('/db')
def db():
    dba=User.query.all() #gets all the objects from the database that we created
    repr(dba)
    return jsonify(repr(dba)) #returns all the contents of the database
    

if  __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')