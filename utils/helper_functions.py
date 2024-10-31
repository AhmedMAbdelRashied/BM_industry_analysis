import yaml
from app.EnumIndustryName import IndustryName
def read_ymal(path)->dict:
     with open(path, 'r',encoding='utf-8') as file:
            data = yaml.safe_load(file)
     return data if data else None

def save_yaml_file(data:dict , path:str ) :
    with open(path, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

    

def create_yaml_files_from_prompts(industries:dict) -> list[dict] :
    """
    Create a YAML files from industries dict which contains all industries prompts

    """
    prompts={} # dict to save the industries prompt 
    queries={} # dict to save the queries for each section inside industries
    for industry_name in industries.keys():
        # get industry_id
        industry=IndustryName.get_key(industry_name)
        
        prompts[industry]={}
        queries[industry]={}

    for industry_name in industries.keys():
        # get industry_id
        industry_id=IndustryName.get_key(industry_name)

        for section in industries[industry_name]['prompts'].keys():
            # check eif the section contains bing queries
            if industries[industry_name]['prompts'][section]['bing_query']!=None:
                # Save the prompts for each industry
                prompts[industry_id][section]=industries[industry_name]['prompts'][section]
                # Save section's queries for each industry 
                queries[industry_id][section]=industries[industry_name]['prompts'][section]['bing_query']
                # Set the bing query to True to link the queries by its prompts in back-end server
                prompts[industry_id][section]['bing_query']=True

            else: 
                # the section does not contain any queries
                prompts[industry_id][section]=industries[industry_name]['prompts'][section]
                prompts[industry_id][section]['bing_query']=False
        # Save the pdf_paths
        prompts[industry_id]['pdf']=industries[industry_name]['pdf_paths']
    return prompts, queries


