import yaml
from enum import Enum

def read_ymal(path)->dict:
     with open(path, 'r',encoding='utf-8') as file:
            data = yaml.safe_load(file)
     return data if data else None

def save_txt(data:Enum,path:str):
     
    with open(path, 'w') as f:
        for industry in  data:
            f.write(f'{industry.name}={industry.value}\n')

def read_txt(path):
    loaded_data = {}
    with open(path, 'r') as f:
        for line in f:
            value, name = line.strip().split('=')
            loaded_data[name] = value
    return loaded_data
def save_yaml_file(data:dict , path:str ) :
    with open(path, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

    

def create_yaml_files_from_prompts(industries:dict) -> list[dict] :
    """
    Create a YAML files from industries dict which contains all industries prompts

    """
    prompts={}
    queries={}
    for industry in industries.keys():
        prompts[industry]={}
        queries[industry]={}

    for industry in industries.keys():
        for section in industries[industry]['prompts'].keys():
            if industries[industry]['prompts'][section]['bing_query']!=None:
                prompts[industry][section]=industries[industry]['prompts'][section]
                queries[industry][section]=industries[industry]['prompts'][section]['bing_query']
                prompts[industry][section]['bing_query']=True

            else:
                prompts[industry][section]=industries[industry]['prompts'][section]
                prompts[industry][section]['bing_query']=False
    
        prompts[industry]['pdf']=industries[industry]['pdf_paths']
        
        
    return prompts, queries
    # save_yaml_file(prompts,'config\prompts.yml')
    # save_yaml_file(queries,'config\queries.yml')


