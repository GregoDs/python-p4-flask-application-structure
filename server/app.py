from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Use app instance to register a route to handle requests to the root URL
@app.route('/')
def index():  # Function to handle requests to the root URL
    return '<h1>Welcome to My Page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'




# Run the server
if __name__ == '__main__':
    app.run(port=5555,debug=True)
