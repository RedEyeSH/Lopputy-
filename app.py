# Run this app.py code while trying my code 
# and do not run any of html file because it is working only in this file!
from flask import Flask
from views import views  

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=1000)    



