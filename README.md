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

2. **List Bookmarks**
   - `GET /list`
   - **Parameters**: None.
   - **Example Call**:
     ```python
     import requests
     response = requests.get("http://127.0.0.1:5000/list")
     print(response.status_code, response.text)
     ```

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

---

### **Programmatically Receive Data**
Responses are in JSON format. Example responses:

Add a Bookmark: No data is directly returned. The response redirects to the /list endpoint if successful.
List Bookmarks: Returns an HTML response with all the bookmarks. You can parse the HTML to extract the list if needed.
Delete a Bookmark: No data is directly returned. The response redirects to the /list endpoint after deletion.

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
