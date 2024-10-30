

from flask import Flask
from utils.industry_analysis import * 


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
@app.route("/")
def home():
    create_industry_analysis("arabic",'Construction')
    return " Done"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)