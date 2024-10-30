import yaml
from banque_misr_industry_analysis.industry_data import industry_data
from banque_misr_industry_analysis.EnumIndustryName import IndustryName
from helper_functions.helper_functions import *


prompts, queries=create_yaml_files_from_prompts(industry_data)
save_yaml_file(prompts,'config/prompts.yml')
save_yaml_file(queries,'config/queries.yml')
save_txt(IndustryName,'config/industryName.txt')

