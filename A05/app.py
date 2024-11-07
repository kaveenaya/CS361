from flask import Flask, render_template, request, redirect, url_for, jsonify
from uuid import uuid4
import time

app = Flask(__name__)

# In-memory storage for bookmarks
bookmarks = []

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to render add bookmark page
@app.route('/add')
def add_page():
    return render_template('add.html')

# Route to add a bookmark
@app.route('/bookmark', methods=['POST'])
def add_bookmark():
    start_time = time.time()
    url = request.form.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    bookmark = {
        "id": str(uuid4()),
        "url": url
    }
    bookmarks.append(bookmark)
    if time.time() - start_time > 2:
        return jsonify({"error": "Request took too long"}), 500
    return redirect(url_for('list_page'))

# Route to render list bookmarks page
@app.route('/list')
def list_page():
    return render_template('list.html', bookmarks=bookmarks)

# Route to delete bookmark page
@app.route('/delete')
def delete_page():
    return render_template('delete.html', bookmarks=bookmarks)

# Route to delete a bookmark by ID
@app.route('/bookmark/<id>', methods=['POST'])
def delete_bookmark(id):
    start_time = time.time()
    global bookmarks
    bookmarks = [b for b in bookmarks if b['id'] != id]
    if time.time() - start_time > 2:
        return jsonify({"error": "Request took too long"}), 500
    return redirect(url_for('list_page'))

if __name__ == '__main__':
    app.run(debug=True)
