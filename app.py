#import dependencies
from flask import Flask
from blueprints.user import user_blueprint


#declare an app instance
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"


#blueprints
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
  app.run()