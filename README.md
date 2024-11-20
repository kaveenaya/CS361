# CS361

# Bookmark Manager Microservice

This is a Flask-based microservice for managing bookmarks. It allows users to add, list, and delete bookmarks.

---

## Prerequisites

Before running the microservice, ensure you have the following installed:

Python 3.10+
pip (Python package manager) - pip install flask

---

## To Run The Program:

python3 app.py


## Communication Contract

### **Request Data**
You can interact with the microservice via its endpoints using HTTP requests. Below are the details for each supported operation:

1. **Add a Bookmark**
   - `POST /bookmark`
   - **Parameters**: 
     - `url` (string): The URL to save.
   - **Example Call**:
     ```python
     import requests
     response = requests.post("http://127.0.0.1:5000/bookmark", data={"url": "http://example.com"})
     print(response.status_code, response.text)
     ```
Expected Behavior:

The server processes the request, saves the bookmark, and redirects to /list.
If successful, it responds with a 302 status code indicating a redirection.

2. **List Bookmarks**
   - `GET /list`
   - **Parameters**: None.
   - **Example Call**:
     ```python
     import requests
     response = requests.get("http://127.0.0.1:5000/list")
     print(response.status_code, response.text)
     ```
Expected Behavior:

The server responds with an HTML page containing all saved bookmarks.
If successful, the response status code will be 200.

3. **Delete a Bookmark**
   - `POST /bookmark/<id>`
   - **Parameters**: 
     - `id` (string): The bookmark ID to delete.
   - **Example Call**:
     ```python
     import requests
     response = requests.post("http://127.0.0.1:5000/bookmark/<id>")
     print(response.status_code, response.text)
     ```

Expected Behavior:

The server processes the delete request and redirects to /list.
If successful, it responds with a 302 status code.

---

### **Programmatically Receive Data**
Responses are in JSON format. Example responses:

Add a Bookmark: No data is directly returned. The response redirects to the /list endpoint if successful.
List Bookmarks: Returns an HTML response with all the bookmarks. You can parse the HTML to extract the list if needed.
Delete a Bookmark: No data is directly returned. The response redirects to the /list endpoint after deletion.

The microservice provides responses to all requests, either as HTML (for /list) or as redirects (for /bookmark and /bookmark/<id>). 

1. **Adding a Bookmark**:
   - **Response**: Redirects to `/list`.
2. **Listing Bookmarks**:
   - **Response**:
     ```json
     [
       {"id": "12345", "url": "http://example.com", "timestamp": "2024-11-18 10:00:00"}
     ]
     ```
3. **Deleting a Bookmark**:
   - **Response**: Redirects to `/list`.

---

### **UML Sequence Diagram**
![BookmarkManager_Chart](https://github.com/user-attachments/assets/6f3a0f3d-8b07-496a-8366-a5941c305c14)

