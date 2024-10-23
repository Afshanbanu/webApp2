from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

'''@app.route('/')
def home():
    return "Welcome to the Home Page!"
@app.route('/about')
def about():
    return "This is the About Page!"

@app.route('/welcome')
def welcome():
    return render_template('/home.html', name="John")'''

# List to store tasks
tasks = []
@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('home'))
'''@app.route('/blog/<int:postID>')
def show_blog(postID):gyu89-\'-nbvdsasdfgh123-'24ytrewq1`   qwergh12+*-/
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo'''
if __name__ == '__main__':
   app.run(port=5002)