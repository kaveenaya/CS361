from flask import Flask, render_template, request, redirect, url_for, jsonify
from uuid import uuid4
import time

app = Flask(__name__)

# In-memory storage for bookmarks
bookmarks = []
deleted_bookmarks = []
categories = ["Uncategorized", "Work", "Personal", "Education", "Entertainment"]

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to render add bookmark page
@app.route('/add')
def add_page():
    return render_template('add.html', categories=categories)

# Route to add a bookmark
@app.route('/bookmark', methods=['POST'])
def add_bookmark():
    start_time = time.time()
    url = request.form.get("url")
    category = request.form.get("category", "Uncategorized")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    bookmark = {
        "id": str(uuid4()),
        "url": url,
        "category": category,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    bookmarks.append(bookmark)
    if time.time() - start_time > 2:
        return jsonify({"error": "Request took too long"}), 500
    return redirect(url_for('list_page'))

# Route to render list bookmarks page
@app.route('/list')
def list_page():
    categorized_bookmarks = {}
    for category in categories:
        categorized_bookmarks[category] = [b for b in bookmarks if b['category'] == category]
    return render_template('list.html', categorized_bookmarks=categorized_bookmarks)

# Route to delete bookmark page
@app.route('/delete')
def delete_page():
    return render_template('delete.html', bookmarks=bookmarks)

# Route to delete a bookmark by ID
@app.route('/bookmark/<id>', methods=['POST'])
def delete_bookmark(id):
    global bookmarks, deleted_bookmarks
    for bookmark in bookmarks:
        if bookmark['id'] == id:
            deleted_bookmarks.append(bookmark)
            break
    bookmarks = [b for b in bookmarks if b['id'] != id]
    return redirect(url_for('list_page'))

# Undo last deletion
@app.route('/undo', methods=['POST'])
def undo_delete():
    global bookmarks, deleted_bookmarks
    if deleted_bookmarks:
        bookmarks.append(deleted_bookmarks.pop())
    return redirect(url_for('list_page'))

# Reset all bookmarks
@app.route('/reset', methods=['POST'])
def reset_bookmarks():
    global bookmarks
    bookmarks.clear()
    return redirect(url_for('list_page'))

if __name__ == '__main__':
    app.run(debug=True)
