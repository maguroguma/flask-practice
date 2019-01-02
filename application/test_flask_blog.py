# test_flask_blog.py

import os
import flask_blog
import unittest
import tempfile
from flask_blog.scripts.db import InitDB

class TestFlaskBlog(unittest.TestCase):

  def setUp(self):
    """ テストを実行するときに最初に実行されるメソッド """
    # 本番用のデータベースを使用するとテストした内容が含まれてしまうので、最初にテスト専用に一時的なデータベースを作成し、アプリケーションを起動する
    self.db_fd, flask_blog.DATABASE = tempfile.mkstemp()
    self.app = flask_blog.app.test_client()
    InitDB().run()

  def tearDown(self):
    """ テストの最後、終了直前に実行されるメソッド """
    os.close(self.db_fd)
    os.unlink(flask_blog.DATABASE)

  def login(self, username, password):
    return self.app.post('/login', data=dict(
      username=username,
      password=password
    ), follow_redirects=True)

  def logout(self):
    return self.app.get('/logout', follow_redirects=True)

  def test_login_logout(self):
    rv = self.login('john', 'due123')
    assert 'ログインしました'.encode() in rv.data
    rv = self.logout()
    assert 'ログアウトしました'.encode() in rv.data
    rv = self.login('admin', 'default')
    assert 'ユーザ名が異なります'.encode() in rv.data
    rv = self.login('john', 'defaultx')
    assert 'パスワードが異なります'.encode() in rv.data

if __name__ == '__main__':
  unittest.main()
