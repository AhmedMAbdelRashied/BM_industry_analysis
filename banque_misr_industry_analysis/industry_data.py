from prompt.prompts import *  # Import prompts for each industry
# Mapping industry names to their corresponding PDF paths and prompts
industry_data = {
"Oil and Gas":
{
       "pdf_paths": "Raw_data/oil_gas/",
       "prompts": oil_gas_prompts
   },
"Information Technology":
{
       "pdf_paths": "Raw_data/It/",
       "prompts": IT_prompts
   },
"Automotives":
{
    "pdf_paths" : "Raw_data/automotives/",
     "prompts":AUTOMOTIVE_prompts
},

"Realestate":
{
"pdf_paths": "Raw_data/real_estate/",
"prompts":real_estate_prompts
},
"Construction":
{

"pdf_paths":"Raw_data/construction/",
"prompts":construction_prompts
},

"Tourism":
{

"pdf_paths":"Raw_data/tourism/",
"prompts":tourism_prompts

},
"Electricity":
{
"pdf_paths":"Raw_data/electricity/",
"prompts":Electricity_prompts

},
"Steel":
{
    "pdf_paths":None,

    "prompts":steel_prompts
},

"Food and beverage (retail)":
{

"pdf_paths":"Raw_data/food_beverage/",
"prompts":food_Retail_prompts

},
"Sugar":
{
    "pdf_paths":"Raw_data/sugar/",

    "prompts":sugar_prompts
},
"Grains":
{

"pdf_paths":"Raw_data/grain/",

"prompts":grain_prompts

},

"Cotton":
{
    "pdf_paths":"Raw_data/cotton/",

    "prompts":cotton_prompts
},
"Fruits and vegetables":
{
    "pdf_paths":"Raw_data/food_and_vegetables/",
    "prompts" : fruits_and_vegetables_prompts
},
"Fertilizers":
{
    "pdf_paths":"Raw_data/fertilizers/",
    "prompts" : fertilizers_prompts
},
"Food & Beverage (Oil Refining & Extraction)":
{
    "pdf_paths":"Raw_data/Oil_Refining_And_Extraction/",
    "prompts" : Oil_Refining_Extraction_prompts
},
"Food & Beverage (Meat)":
{
    "pdf_paths":"Raw_data/meat",
    "prompts" : meat_prompts
},
"Food & Beverage (Dairy & Cheese)":
{
    "pdf_paths":"Raw_data/dairy_cheese/",
    "prompts" : dairy_cheese_prompts
},
"Textiles":
{
    "pdf_paths":None,
    "prompts" : textiles_prompts
}
   # Add more industries here as needed
}