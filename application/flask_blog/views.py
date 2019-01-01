# flask_blog/views.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def show_entries():
  if not session.get('logged_in'):
    return redirect('/login')
  return render_template('entries/index.html')  # パスにtemplatesは不要

# methodsはURLに対して許可するHTTPメソッド、デフォルトではGETのみが許可される
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME']:
      flash('ユーザ名が異なります')
    elif request.form['password'] != app.config['PASSWORD']:
      flash('パスワードが異なります')
    else:
      session['logged_in'] = True
      flash('ログインしました')
      return redirect('/')
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('logged_in', None)  # Flaskではsessionという変数を扱うことでセッション情報を扱うことができる
  flash('ログアウトしました')
  return redirect('/')
