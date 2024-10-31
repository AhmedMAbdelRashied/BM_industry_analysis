
import base64
from app.industry_analysis_module import IndustryAnalysisModule
from app.EnumIndustryName import IndustryName
from flask import Flask, jsonify, request
 
app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False

# # Just for testing the server using the URL
# # Just open the home url it will generate an industry analysis 
# @app.route("/")
# def home():

#     industry_analysis_module.create_industry_analysis("arabic",'Oil and Gas')
#     return " Done"


## API routes
@app.route('/api/industry_analysis/<lang>/<industry_id>', methods=['GET'])
def industry_analysis(lang,industry_id):
    
    file_path=industry_analysis_module.create_industry_analysis(language=lang,industry_name=industry_id)
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
    industry_names=IndustryName.get_all_values()
    industries_ids=IndustryName.get_all_keys()
    
    return jsonify({
        "industry_names":industry_names,
        "industries_ids":industries_ids
        })

if __name__ == "__main__":
    industry_analysis_module=IndustryAnalysisModule()
    app.run(host="0.0.0.0", port=5000, debug=True)