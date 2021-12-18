from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
# from models.Todo import Todo
from datetime import datetime

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
      # req_data = request.form['title']
      # print("req_data-",req_data)
      todo = Todo(title=request.form['title'], desc=request.form['desc'])
      db.session.add(todo)
      db.session.commit()

   alltodo = Todo.query.all()
   return render_template('index.html', alltodos = alltodo)


@app.route("/show")
def show():
   alltodo = Todo.query.all()
   
   return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    