from flask import Flask, render_template, request, redirect, url_for  
from models import init_db, get_db  

app = Flask(__name__)  
init_db()  

@app.route('/')  
def index():  
    db = get_db()  
    tasks = db.execute('SELECT * FROM tasks').fetchall()  
    return render_template('index.html', tasks=tasks)  

@app.route('/add', methods=['POST'])  
def add_task():  
    task = request.form.get('task')  
    if task:  
        db = get_db()  
        db.execute('INSERT INTO tasks (content) VALUES (?)', (task,))  
        db.commit()  
    return redirect(url_for('index'))  

@app.route('/delete/<int:id>')  
def delete_task(id):  
    db = get_db()  
    db.execute('DELETE FROM tasks WHERE id = ?', (id,))  
    db.commit()  
    return redirect(url_for('index'))  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)  



