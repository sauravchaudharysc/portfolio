from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__);

#this is a decorator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\nName :- {name}, \nEmail :- {email},\nSubject :- {subject}, \nMessage :-{message}')

def write_to_csv(data):
	with open('database.csv',mode='a') as database2:
	 name = data["name"] 
	 email = data["email"]
	 subject = data["subject"]
	 message = data["message"]
	 spamwriter = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	 spamwriter.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
      try:	
       data = request.form.to_dict()
       write_to_csv(data)
       return redirect('/thankyou.html')
      except:
      	return 'Something wrong happened'   
    else:
       return 'Something went wrong..!'