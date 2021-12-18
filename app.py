from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
# from models.Todo import Todo
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Todo(db.Model):
    
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(600), nullable=False)
    created_Date = db.Column(db.DateTime ,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.srno} - {self.title}"

@app.route("/", methods=['POST','GET'])
def hello_world():
   if request.method == 'POST':     
      todo = Todo(title=request.form['title'], desc=request.form['desc'])
      db.session.add(todo)
      db.session.commit()

   alltodo = Todo.query.all()
   return render_template('index.html', alltodos = alltodo)


@app.route("/show")
def show():
   alltodo = Todo.query.all()
   
   return render_template('index.html')

   
@app.route("/update/<int:sno>")
def update(sno):
   sr_up= Todo.query.get(sno)   
   print(sr_up)

   alltodo = Todo.query.all()
   
   return render_template('index.html', alltodos = alltodo)

   
@app.route("/delete/<int:sno>")
def delete(sno):
   del_todo = Todo.query.filter_by(srno = sno) .first()
   db.session.delete(del_todo)
   db.session.commit()  
   return redirect('/')
  


if __name__ == '__main__':
    app.run(debug=True)
    