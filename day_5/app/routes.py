from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Todo
from app.forms import TodoForm
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@bp.route('/add', methods=['GET', 'POST'])
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(title=form.title.data, description=form.description.data)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_todo.html', form=form)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_todo(id):
    todo = Todo.query.get_or_404(id)
    form = TodoForm(obj=todo)
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_todo.html', form=form)
