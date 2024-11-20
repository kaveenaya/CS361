# CS361

# Bookmark Manager Microservice

This microservice allows users to manage bookmarks by providing endpoints to add, list, and delete bookmarks.

---

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

### **Receive Data**
Responses are in JSON format. Example responses:
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
