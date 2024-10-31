
import base64
from flask import Flask, jsonify, request
from utils.industry_analysis import * 

 
app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False

# Just for testing the seerver
@app.route("/")
def home():

    create_industry_analysis("arabic",'Oil and Gas')
    return " Done"



## API routes
@app.route('/api/industry_analysis/<lang>/<industry>', methods=['GET'])
def industry_analysis(lang,industry):
    
    file_path=create_industry_analysis(language=lang,industry_name=industry)
    print(file_path)
    file_path=''.join(['output/',file_path]) 
    print(file_path)
    with open(file_path, "rb") as file:
        file_data = file.read()
        encoded_file = base64.b64encode(file_data).decode('utf-8')

    # Return the base64-encoded file as JSON

    return jsonify({
        "file_name": file_path.split('/')[-1],
        "file_data": encoded_file
        })

@app.route('/api/language', methods=['GET'])
def get_language():
    return jsonify({"Language": ["Arabic","English"]})


@app.route('/api/industries', methods=['GET'])
def industries_names():
    industry_names=get_industries_names()
    
    return jsonify({"industry_names":industry_names})

# @app.route('/api/industry_analysis_download/<path>', methods=['GET'])
# def download(path):
#     pass



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)