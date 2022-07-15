from flask import Flask, request, render_template,url_for,redirect,flash,session,jsonify
print("debug benchmark")
import json 
# Flask constructor
app = Flask(__name__) 

dic={"name":[]}

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def home():
   return f"hello user"


@app.route('/login', methods =["POST", "GET"])
def login():
   if request.method=="POST":
      user=request.form['nm']
      dic['name'].append (user)
      with open('data.json', 'w') as f:
        json.dump(dic, f)
      return redirect(url_for('user',username=user))
   else:
      return render_template('login.html')

@app.route('/<username>')
def user(username):
   return f"hello {username}"
 
if __name__=='__main__':
   app.run(debug=True)