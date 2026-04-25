import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def get_user():
    # VULNERABILITY: Raw user input is concatenated directly into the query
    username = request.args.get('username')
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # This executes the malicious payload if 'username' contains SQL commands
    cursor.execute(query)
    user = cursor.fetchone()
    return str(user)

if __name__ == "__main__":
    app.run(debug=True)

api_key ='1223342sdsrtretdg'

# BAD PATTERN (conceptual example)
user_input = input("Enter a number: ")
result = eval(user_input)  # Dangerous: executes arbitrary code
print(result)

