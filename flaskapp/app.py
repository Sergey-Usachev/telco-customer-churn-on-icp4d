
from flask import Flask, request, session, render_template, flash

application = Flask(__name__)
@application.route("/")

def hello():
        
        return render_template('input.html')


#load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
#port = os.environ.get('PORT', '5000')
#host = os.environ.get('HOST', '0.0.0.0')
if __name__ == "__main__":
#    app.run(host=host, port=int(port))

   application.run()

