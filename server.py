from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

# @app.route('/index.html')
# def homee():
# 	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as text_file:
	 email = data['email']
	 subject = data['subject']
	 message = data['message']
	 text_file.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database2.csv',mode='a',newline='') as csv_file:
	 email = data['email']
	 subject = data['subject']
	 message = data['message']
	 csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	 csv_writer.writerow([email,subject,message])
	
	  	
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
		  data = request.form.to_dict()
		  #write_to_file(data)
		  write_to_csv(data)
		  #print(data)
		  return redirect('/thanks.html')
		except:
		  return 'Did not save to Database'
	else:
	  return 'Something went wrong'
    

# @app.route('/works.html')
# def works():
# 	return render_template('works.html')

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/components.html')
# def components():
# 	return render_template('components.html')