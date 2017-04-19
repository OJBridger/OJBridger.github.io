from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('Opened Database Successfully')

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT, likes INTEGER, id INTEGER)')
print('Table Created Successfully')
connection.close()

#HOME PAGE#
@app.route('/')
def index():
  return render_template('home.html')
#NEW POST# 
@app.route('/new')
def new_post():
  return render_template('new.html')
#RECORD OF POST PAGE#
@app.route('/addrecord', methods = ['POST'])
def addrecord():
  
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()

  try:
     title = request.form['title']  	
     post = request.form['post']
     likes = 0
     id = request.form['id']
     cursor.execute('INSERT INTO posts(title, post, likes, id) VALUES (?, ?, ?, ?)', (title, post, likes, id))
     connection.commit()
     message = 'Record successfully added'
  except:
     connection.rollback()
     message = 'Error in insert operation'
  finally:
     return render_template('result.html', message = message)
     connection.close()

@app.route('/posts')
def getPosts():
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()
  cursor.execute('SELECT * FROM posts')
  postList = cursor.fetchall()
  connection.close()
  return jsonify(postList)

@app.route('/like/<post_id>')
def likePost(post_id):
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()

  cursor.execute('UPDATE posts SET likes=likes + 1 WHERE ID=?', (post_id))
  connection.commit()
  connection.close()
  return post_id + ' successfully updated'


#DEBUGGER#
app.run(debug = True)






