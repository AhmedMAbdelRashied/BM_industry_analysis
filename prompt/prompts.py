from datetime import datetime 

# Get the current date
today = datetime.today()
# Format the date as 'day month year'
date_string = today.strftime("%d-%B-%Y")

# Current year
current_year = today.strftime("%Y")
# - note that today's date is {date_string} anything beyond add it as forcasting

IT_prompts = {
        "Introduction": {
            "prompt": f"""
            Generate the following sections in [language]:
            # A comprehensive analysis of the Information Technology industry
            ### Industry Overview:
            -Historical overview about the indusrty of the Information technology in Egypt including its definitions.
            -Industry stages and types of nformation technology.
            -Software and Hardware types.
            -Characteristic of the Industry
            -Include numbers,facts and dates if present , dont include any ungiven data.
            -Mention their types as well.
            -Make it in one paragraph not more than 5 lines.
            -Don't include any conclusions.
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": None,
        },
    
        "Introduction 2": {
            "prompt": f"""
            Generate the following sections in [language]:
    
            ### information technology Industry Importance:
            -Industry importance in Egypt and Worldwide.
            -Digital transformation in Egypt and worldwide.
            -Evolution of new technologies such as GenAI,Cyber Security,BlockChain and it's impact on the GDP.
            -Industries that are linked to the information technology industry.
            -Include Numbers , dates, geographical distributions if possible and present in the data.
            -Make it 3 to 4 lines at maximum.
            -Don't include any conclusions.
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": None,
        },
    
        "Introduction 3": {
            "prompt": f"""
            Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
    
            ### Software evolutions:
            -Evolutions
            [Instructions]:
                -Software trends and evolutions including ERP,GenAI,Blockchain,Cybersecurity.
                -Introduce the Infrastructure as a services (IaaS), Platform as a service (PaaS) in Egypt.
                -Introduce the E-commerce software evolution.
                -Don't include any conclusions.
                -Don't include any special characters in the response.
                
                -Make it 3 paragrphs long.
                -Avoid contradictions.
                -Include images if possible.
                -Include the citation source.
                - note that today's date is {date_string} anything beyond add it as forcasting
                
            """,
            "bing_query": None
        },
    
        "Introduction 4": {
            "prompt": f"""
            Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
    
            ### Hardware evolutions:
            -Evolutions
            [Instructions]:
                -Hardware new trends such as GPUs for the GenAI, Cisco's firewalls , routers , switches , robotics.
                -Don't include any conclusions.
                -Don't include any special characters in the response.
                
                -Make it 3 paragrphs long.
                -Avoid contradictions.
                -Include images if possible.
                -Include the citation source.
                - note that today's date is {date_string} anything beyond add it as forcasting
            
            """,
            "bing_query": None
        },
        "Market updates in Egypt": {
            "prompt": f"""
            Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
    
            ### Market updates in Egypt latest news the current year:
            -Discuss Egyptian Market updates for Information technology the current year with the latest market updates in this two years exactly.
            -Get the latest news regarding the information technology the current year including Service providers.
            -Get the latest Prices regarding the information technology the current year including (services such as Software services and Hardware services).
            -Get the latest Information technology/Digital transformation Projects in Egypt {current_year} with its investements.
            -Get the latest Information technology/Digital transformation trends in Egypt {current_year}.
            -Each point from the list should be pointed out as a detailed subsection, for example latest news should be as subsection,latest prices should be subsection.
            -Focus on news that's related to enhancing the infrastructure of the information technology.
            -Focus also on the 4G,5G , esim introduction to the Egyptian market with examples for the data you are provided with.
            -Focus on the introduction of the genAI to the Egyptian market with examples for the data you are provided with.
            -Focus on the role of Egyptian Success in cyber secuirty with examples for the data you are provided with.
            [Instructions]:
                -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
                -Write it very detailed and highlight all the required data.
                -For statistics include them in a table.
                -Don't include any conclusions.
                -Don't include any special characters in the response.
                
                -Make it detailed as much as possible.
                -get some more details Or more projects.
                -news for uptrends/downtrends, projects must be very detailed.
                -Be specific , detailed oriented and include details as much as possible.
                
                -Add a subsection for the efforts of Ministry of Telecom Egypt for fighting covid-19 post pandemic.
                -Add a subsection for the efforts of the Telecom in Egypt {current_year} .
                -Add a subsection for the egyptian digital platform {current_year}.
                -Add a subsection for the introduction of GenAI in the Egyptian Market and governmental institutes {current_year} ( all terms should be in [language]).
                -Add a subsection for Egyptian Success in cyber security {current_year} ( all terms should be in [language]).
                -Avoid contradictions.
                -Include the citation source from Egyptian official sources and worldwide.
                -Prices are mandatory here and not an optional.
                - note that today's date is {date_string} anything beyond add it as forcasting
                -The section should be named "Latest prices of developments in the information technology sector in the Egyptian market".
            """,
            "bing_query": ["منصة مصر الرقمية",
                        "البنية التحتية للاتصالات",
                        " جهود وزارة الاتصالات وتكنولوجيا المعلومات لدعم خطط الدولة في مواجهة تداعيات جائحة كورونا",
                        "4G,5G , esim introduction to the Egyptian market",
                        "introduction of the genAI to the Egyptian market",
                        "Egyptian Success in cyber security"
    
                        ]
        },
    
        "Market updates in Egypt 2": {
            "prompt" : f"""
            Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
    
            ### Market updates in Egypt {current_year}:
            -Get the latest Consumptions regarding the Software and Hardware services the current year.
            -Mention how Egypt is powerful at cybersecurity especially during the defence.
            -Introduce the E-commerce evolution in Egypt.
        
            -Each point from the list should be pointed out as a detailed subsection, for example latest news should be as subsection,latest prices should be subsection.
            [Instructions]:
                -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
                -For statistics include them in a table.
                -Each point must have a table illustrating its values , ie consumptions in a table , exports in a table, imports in a table , production in a table .
                -Don't include any conclusions.
                -Be specific , detailed oriented and include details as much as possible.
                -Make sure it contains the actual and predicted for all Information technology consumptions and imports as well get all its values.
                -Make sure it contains the Egyptian market trends for Information technology.
                -Make sure its the most updated.
                -Don't include any special characters in the response.
                
                -Make it detailed as much as possible.
                -Avoid contradictions.
                -Include the citation source
                - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": None,
        },
    
        "Market updates Globally": {
            "prompt": f"""
            Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
    
            ### Market updates in World wide the current year:
            -Discuss World wide Market updates for  Information technology , AI , Software , Cybersecurity the current year with the latest market updates in this two years exactly.
            -Get the latest news regarding the  Information technology , AI , Software , Cybersecurity the current year including .
            -Get the latest Prices regarding the  Information technology , AI , Software , Cybersecurity the current year including .
            -Get the latest Consumptions regarding the  Information technology , AI , Software , Cybersecurity the current year .
            -Get the latest cloud providers such as Azure , GCP , amazon , cloudera ;regarding the  Information technology , AI , Software , Cybersecurity the current year .
            -Get the latest Scalable serverless vs servered solutions regarding the  Information technology , AI , Software , Cybersecurity the current year .
            -Get the latest Mobile Carriers focusing on 5G technologies/e-sim solutions regarding the  Information technology , AI , Software , Cybersecurity the current year .
            -Get the latest Cyber Security solutions regarding the  Information technology , AI , Software , Cybersecurity the current year .
            -Get the latest Worldwide conflicts affections on the prices/supply and demand for  Information technology , AI , Software , Cybersecurity {current_year}.
            -Get the latest  Information technology , AI , Software , Cybersecurity Projects in Gulf / worldwide {current_year} with its investements.
            -Each point from the list should be pointed out as a detailed subsection, for example latest news should be as subsection,latest prices should be subsection.
            [Instructions]:
                -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
                -For statistics include them in a table.
                -Don't include any conclusions.
                -We are in {current_year} , so the news retreieved must be near {date_string}
                -Don't include any special characters in the response.
                -Be specific , detailed oriented and include details as much as possible.
                -No project or number should be mentioned as a dummy everything should have its naming.
                -Avoid contradictions.
                -Paragraph per each point.
                
                -This section must include a detailed analytical about the challenges,consumptions,events and state of the Art solutions, pay as you go stratigies.
                -This section should also include the Global conlficts such as wars and worldwide  Information technology , AI , Software , Cybersecurity production and prices.
                -The Generated content must not contain any local news for egypt.
                -news especially like wars and conflicts must be in details as long as possible.
                -For each event or news that are highly related mention the content in 100 words and how its affecting the industry of Information technology , AI , Software , Cybersecurity the current year.
                -Include the citation source.
                -If there's prices or comparisons list them in a table.
                - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query":None
        },
    
        "Market Statstics": {
                "prompt": f"""
                Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
        
                ### Market forecast:
                -After retreiving the Market updates earlier in the previous prompts , generate a market forecast to analyze the current state of the  Information technology , AI , Software , Cybersecurity industry worldwide in Egypt.
                
                [Instructions]:
                    -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
                    -for the forecast make in in a timerseries graph or tables or charts.
                    -your forecast should be supported with facts,events such as conflicts,statistics from the latest maarket updates in Egypt and worldwide generated before.
                    -Supply and Demand.
                    -Include the citation source.
                    -We are in {date_string} , so that the forecast must after the current year.
                    -Be specific , detailed oriented and include details as much as possible.
                    
                    -Don't include any conclusions.
                    -Make it 3 paragrphs long.
                    -Avoid contradictions.
                    -The results MUST be in a table.
                    - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query":None
            },
        "Competitive Analysis": {
                "prompt": f"""
                Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
        
                ### Competitive analysis for  Information technology according to fitch :
                - Egyptian Market key players.
                - International Market players.
                - Include Numbers statistics , Market shares.
                [Instructions]:
                    -Make 4 to 5 lines maximum for The Egyptian Market key players.
                    -Make 4 to 5 lines maximum for The international Market key players.
                    -Then after you make the 2 paragraphs ,Make them in a structured table with their statistics.
                    -Here we have 4 types of key Players each of them must be present in a separate table , where this tables should contain statistics:
                            --Egyptian market players such as : Vodafone,Itida ,Telecom Egypt.
                            --Worldwide players in IT on premise infrastructure such as : Cisco,Dell,HP,Huwawei,IBM get it in numbers.
                            --Worldwide players cloud serverless:Google,Amazon,Microsoft,Cloudera get it in numbers.
                            --Worldwide players in ERP systems :SAP,Oracle,Oddo get it in numbers.
                    -The marketshares must be retrieved urgently.
                    -If Market shares are not present then don't mention that it's not available.
                    -If not sure skip the sections.
                    -Don't include any conclusions.
                    -Include the citation source.
                    - note that today's date is {date_string} anything beyond add it as forcasting
                    
                """,
                "bing_query": [
            
                "IT market players in Egypt : vodafone , WE , telecom Egypt ,ITIDA market shares in numbers and statitics",
                "Cisco Marketshare percentages in IT managed on premise infrastructure",
                "Dell Marketshare percentages in IT managed on premise infrastructure",
                "IBM Marketshare percentages in IT managed on premise infrastructure",
                "HP Marketshare percentages in IT managed on premise infrastructure",
                "Google Marketshare percentages in cloud serverless Infrastructures",
                "Amazon Marketshare percentages in cloud serverless Infrastructures",
                "Microsoft Marketshare percentages in cloud serverless Infrastructures",
                "Cloudera Marketshare percentages in cloud serverless Infrastructures",
                "SAP Marketshare percentages in ERP softwares",
                "Oracle Marketshare percentages in ERP softwares",
                "Oddo Marketshare percentages in ERP softwares"

            
                ]
            },
        "Competitive Analysis 2": {
                "prompt": f"""
                    Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
            
                    ### Competitive analysis for  Information technology in egypt  according contex  :
                    Generate a detailed comparative analysis between the largest IT  companies in Egypt, including but not limited to the following: IT companies
                    في ايه اس للأنظمة VAS INTEGRATED
                    راية للنظم ش م م
                    ايماك للحلول الرقمية المتكاملة ش م
                    كليك آي تي إس
                    مترا كمبيوترز ش م م
                    الشركة المصرية لصناعات السيليكون
                    اي تي فاكينجز للبرمجيات IT VIKINGS
                    شركه الجيزه للأنظمة
                    شركة الحاسبات المتقدمة ACT
                The table should focus on providing a complete competitive overview
            Instructions:
                -Add numbers that represent the current situation for each section  if existing and be sure these numbers extracted for the context
                -Provide updated data after {int(current_year) - 1} or at least from {int(current_year) - 1}; no need for data before this period.
                -Cite sources for every section and table by name  .
                -Ensure the table is formatted to be clear, readable, and easy to understand.
                -Do not add a conclusion.
                -The output must be related to IT
                -don`t include عدد الموظفين | الإيرادات السنوية (مليون جنيه) , الصادرات السنوية
                -please answer form provided context  , if you dont have the inforamtion dont tell me i can`t
                -comment on the results
                -if you dont have inforamtion about any section any  table  dont include it in your response  
                -if you dont have informatoin dont replay غير متوفر ignor company
                - add source of every section and table
                - if you don't have enough information about the company don't include it in your response
                -source of every section and table
                - note that today's date is {date_string} anything beyond add it as forcasting
                """,
            "bing_query" : [
                "في ايه اس للأنظمة VAS INTEGRATED",
                "راية للنظم ش م م",
                "ايماك للحلول الرقمية المتكاملة ش م",
                "كليك آي تي إس",
                "مترا كمبيوترز ش م م",
                "الشركة المصرية لصناعات السيليكون",
                "اي تي فاكينجز للبرمجيات IT VIKINGS",
                "شركه الجيزه للأنظمة",
                "شركة الحاسبات المتقدم ACT"
            ]
        
            },
        
        "Competitive Analysis 3": {
                "prompt": f"""
                Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
        
                ### Cloud computing service providers in Egypt
                -Companies that provides cloud hosting services in Egypt such as orange , huawei,telecom Egypt.
                [Instructions]:
                -This section should contain a full comparison about service providers such as orange , TE , Huawewi , vodafone.
                -Numbers , statistics and dates must be introudced.
                -Terminologies must be in [language]
                -Introduce the comparison in a table.
                - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": None
            },
        
        
            "SWOT Analysis": {
                "prompt": f"""
                Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
        
                ### Strengths weakness oppourtuintes threas analysis:
                -Generate and Extract Strengths , weakness , opportuinties and threats concerning the Information technology Market in Egypt from the Given Data.
                -Make sure there's no contradictions.
        
                [Instructions]:
                    -Generate the response as a matrix table.
                    -Illustrate the reasons for the swot analysis from the data in context.
                    -Make sure the data is relevant to our context Information technology industry in Egypt.
                    -Be specific , detailed oriented and include details as much as possible.
                    -Don't include any conclusions.
                    -Include the citation source.
                    - note that today's date is {date_string} anything beyond add it as forcasting
                    
                """,
                "bing_query": None
            },
        
            "Anti dumping laws and Regulatory framework": {
                "prompt": f"""
                Generate the following sections in [language] then format them according to the required structure in the [Instructions]:
        
                ### Anti dumping laws and Regulatory framework:
                -Generate antidumping laws for Information technology in egypt if found only!.
                -Genereate the regulatory framework for Information technology in egypt.
                -Laws must be NTRA compliance rules.
                [Instructions]:
                    -just 2 paragraphs one per each
                    -Don't include any conclusions.
                    -Include the citation source.
                    - note that today's date is {date_string} anything beyond add it as forcasting
                    
                """,
                "bing_query":None
            },
        
        "Conclusion": {
                "prompt": f"""
                Generate the following sections in [language]:
        
                ### Conclusion:
                -Highligh the main highlights concerning the Information technology Market in Egypt and worldwide
                -Include a constructive forecast regarding the Information technology after the current year based on the information you knew earlier from the previous prompts.
                -Illustrate your forecasts reasons
        
                [Instructions]:
                    -1 paragraph.
                    -Detailed and focusing on the main highlights.
                    -Include latest projects mentioned earlier or explorations.
                    -Include the Oppourtuinties for it.
                    - note that today's date is {date_string} anything beyond add it as forcasting
                    
                """,
                "bing_query": None
            },
}
oil_gas_prompts = {
    "Introduction": {
        "prompt": f"""
        Generate the following sections in [language] Language:
        # A comprehensive analysis of the oil and gas industry

        ## Industry Overview:

           -Historical overview about the indusrty of the oil and gas in Egypt including its definitions.

           -Industry stages and types of oil and gas manufactures.

           -Oil and Gas types.

           -Characteristic of the Industry

           -Include numbers,facts and dates if present , dont include any ungiven data.

           -Mention the manufacturing stages for oil and Gas.

           -Mention their types as well.

           -Make it in one paragraph not more than 5 lines.

           -Don't include any conclusions.

        ## Overview of the Oil Refining Sector in Egypt:

        Explaining a general overview of the oil refining sector in Egypt, including the following points:
 
        Oil Refining Sector:

            -The Ministry of Petroleum has developed a comprehensive plan to upgrade and improve the efficiency of existing refineries with the aim of:

                1.Keeping pace with the continuous increase and ongoing changes in local consumption patterns.

                2.Enhancing and improving the efficiency of Egyptian refineries to achieve a strategic goal of transforming Egypt into a regional hub for gas and oil trade, taking advantage of its distinguished location at the crossroads of global energy-producing and consuming markets.

            -The Ministry of Petroleum's plan is based on a parallel set of axes, which are:

                1.Eliminating current bottlenecks and upgrading and improving the efficiency of existing refineries, updating their production units, work systems, and safety and security measures.

                2.Increasing refining capacity to reach 2 million tons.

                3.Adding new conversion units to turn low-value mazut into high-value petroleum products needed by the local market.

                4.Implementing a range of new investment projects in refining and manufacturing to increase local production of high economic value petroleum products such as gasoline and butane, in addition to providing petroleum products with the highest quality specifications that meet international standards.

        Egypt has 12 oil refining facilities, the most important of which are:

            1.Middle East Oil Refinery (MIDOR)

            2.Alexandria Petroleum Company (Alexandria Refinery)

            3.Alexandria Mineral Oils Company (AMOC)

            4.Nasr Petroleum Company (NPC)

            5.Amerya Petroleum Company (APRC)

            6.Alexandria National Refining and Petrochemicals Company (ANRPC)

            7.Assiut Oil Refining Company (ASORC)

            8.Egyptian Refining Company

            9.Cairo Oil Refinery

            10.Egypt Petroleum and Fertilizers Manufacturing Company

            11.Assiut National Petroleum Manufacturing Company

            12.Suez Petroleum Manufacturing Company
 
        -provide the Ongoing Projects in Oil, Gas, and Refining Services Companies exactly as follows:

            1.Project for the Production of High-Octane Gasoline at Assiut Oil Refining Company:

                -The project aims to produce high-octane gasoline to meet the petroleum product needs of Upper Egypt. 

                -The project produces approximately 800,000 tons/year of high-octane gasoline, 23,000 tons/year of butane, and 34,000 tons/year of hydrogen-rich gases, with an investment cost of about 450 million USD.            2.Expansion Project of the Middle East Oil Refinery (MIDOR):

            2.Expansion Project of the Middle East Oil Refinery (MIDOR):

                -The investment cost is approximately 2.3 billion USD, and the project was completed in the last quarter of the year.

                -The project aims to expand the refinery and increase production capacity by 60%. The expansion project has a production capacity of approximately 600,000 tons/year of 95-octane gasoline, about 1,300,000 tons/year of diesel, 145,000 tons/year of butane, 700,000 tons/year of jet fuel, 226,000 tons/year of coke, and 65,000 tons/year of sulfur.
 
            3.Hydrocracking Project for Mazut at Assiut National Petroleum Manufacturing Company (ANOPC):

                -The investment cost is around 2.9 billion USD, with plans to complete the project by December {int(current_year) + 1}.

                -The project aims to establish a hydrocracking complex with a feed capacity of 2.5 million tons/year of mazut to produce 1.6 million tons/year of diesel, 100,000 tons/year of butane, 400,000 tons/year of naphtha, 330,000 tons/year of coke, and 65,000 tons/year of sulfur.

            -cite the sources for the projects to be as follows:

                -مشروعات مصر | مجمع التكسير الهيدروجيني للبترول (egy-map.com)

                -(alarabiya.net)

                -(youm7.com)

        Important Notes:

        -ensure to provide all mentioned points and details and don't summarize.

        -avoide hallucination.

        -Avoid conclusions or assumptions.

        -Do not fabricate details; rely on factual information.
        - generate in [langauge]
        - note that today's date is {date_string} anything beyond add it as forcasting

        """,
        "bing_query": None,
        
        
    },

    "Introduction 2": {
        "prompt": f"""
        Generate the following sections in [language]:

        ### Oil and Gas Industry Importance:
        -Industry importance in Egypt and Worldwide.
        -Include Numbers , dates, geographical distributions if possible and present in the data.
        -Make it 2 to 3 lines at maximum.
        -Don't include any conclusions.
        - generate in [langauge]
        - note that today's date is {date_string} anything beyond add it as forcasting
        
        """,
        "bing_query": None,
        
        
    },

    "Market Statstics": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Oil and Gas Industry Production stages:
        -Production stages
        [Instructions]:
            -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
            -For statistics include them in a table .
            -The table should be named "ملخص احصائيات الصناعة في مصر"..
            -Don't include any conclusions.
            -Don't include any special characters in the response.
            
            -Make it 3 paragrphs long.
            -Avoid contradictions.
            -Include images if possible.
            -Include the citation source.
            - note that today's date is {date_string} anything beyond add it as forcasting
            - generate in [langauge]
            
        """,
        "bing_query": ["oil and gas production process from a to z","oil and gas manfacturing stages in Egypt and Worldwide"],
        
    },
    "Market updates in Egypt": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Market updates in Egypt latest news the current year:
           -Discuss Egyptian Market updates for oil and gas the current year with the latest market updates in this two years exactly.
           -Get the latest news regarding the Oil and Gas the current year including (fuel,oil,gas,natural gas).
           -Get the latest Prices regarding the Oil and Gas the current year including (fuel,oil,gas,natural gas).
           -Get the latest Oil and Gas Projects in Egypt {current_year} with its investements(fuel,oil,gas,natural gas).
           -Get the latest Oil and Gas Explorations in Egypt {current_year}.
           -Each point from the list should be pointed out as a detailed subsection, for example latest news should be as subsection,latest prices should be subsection.
        [Instructions]:
            -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
            -Write it very detailed and highlight all the required data.
            -For statistics include them in a table.
            -Don't include any conclusions.
            -Don't include any special characters in the response.
            
            -Make it detailed as much as possible.
            -get some more details Or more projects.
            -Be specific , detailed oriented and include details as much as possible.
            -Avoid contradictions.
            -Include the citation source from Egyptian official sources and worldwide.
            -Prices are mandatory here and not an optional.
            -news especially like wars and conflicts must be in details as long as possible.
            -The section should be named "latest prices for oil and gas for consumers in Egypt"
            - generate in [langauge]
            - note that today's date is {date_string} anything beyond add it as forcasting

            
        """,
        "bing_query": ["الاخبار العالميه و الصراعات الاقليميه المتعلقه بالتاثير علي اسعار المواد البتروليه اكتوبر",
                        "واردات مصر للمواد البتروليه و الغاز الطبيعي اكتوبر",
                       "تصدير مصر للمواد البتروليه اكتوبر",
                       "استهلاك مصر من المواد البتروليه اكتوبر",
                       "اكتشافات مصر في مجال الطاقه و البترول و الغاز اكتوبر",
                       " اخر اسعار الغاز و البترول و البنزين في مصر اكتوبر",
                       "اسعار الغاز الطبيعي في اكتوبر ",
                       "تاثير الصراعات الاقليميه علي اسعار المحروقات في مصر اكتوبر",
                       "احدث المشروعات في مجال الطاقه و الغاز و الوقود في مصر"],
        
    },

    "Market updates in Egypt 2": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Market updates in Egypt consumption, production , import ,exports the current year:
           -Get the latest Consumptions regarding the Oil and Gas the current year including (fuel,oil,gas,natural gas).
           -Get the latest Exports and imports regarding the Oil and Gas the current year including (fuel,oil,gas, natural gas).
           -Get the latest Production values regarding the Oil and Gas the current year including (fuel,oil,gas,natural gas).
           -Each point from the list should be pointed out as a detailed subsection, for example latest news should be as subsection,latest prices should be subsection.
        [Instructions]:
            -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
            -For statistics include them in a table.
            -Each point must have a table illustrating its values , ie consumptions in a table , exports in a table, imports in a table , production in a table .
            -Don't include any conclusions.
            -Be specific , detailed oriented and include details as much as possible.
            -Make sure it contains the actual and predicted for all oil and gas consumptions,Production,exports and imports as well get all its values.
            -Make sure its the most updated.
            -Don't include any special characters in the response.
            -Make it detailed as much as possible.
            -Avoid contradictions.
            -Include the citation source 
            - note that today's date is {date_string} anything beyond add it as forcasting


            
        """,
        "bing_query": None,
        
    },

    "Market updates Globally": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Market updates in World wide the current year:
           -Discuss World wide Market updates for oil and gas in the current year with the latest market updates in this two years exactly.
           -Get the latest news regarding the Oil and Gas in the current year including (fuel,oil,gas,natural gas).
           -Get the latest Prices regarding the Oil and Gas in the current year including (fuel,oil,gas,natural gas).
           -Get the latest Consumptions regarding the Oil and Gas in the current year including (fuel,oil,gas,natural gas).
           -Get the latest Exports and imports regarding the Oil and Gas the current year including (fuel,oil,gas,natural gas).
           -Get the latest Production values regarding the Oil and Gas the current year including (fuel,oil,gas,natural gas).
           -Get the latest Worldwide conflicts such as Israel-Gaza war / Russian Ukraine war / Red sea conflicts affections on the prices/supply and demand for oil and gas in the current year.
           --Get the latest Oil and Gas Projects in Gulf / worldwide in the current year with its investements(fuel,oil,gas,natural gas).
           -Get the latest Oil and Gas Explorations in Gulf / worldwide in the current year.
           -Each point from the list should be pointed out as a detailed subsection, for example latest news should be as subsection,latest prices should be subsection.
        [Instructions]:
            -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
            -For statistics include them in a table.
            -Don't include any conclusions.
            -Don't include any special characters in the response.
            -Make it long and detailed as much as possbile.
            -Be specific , detailed oriented and include details as much as possible.
            -Avoid contradictions.
            -This section must include a detailed analytical about the wars/political/geostatitical challenges,consumptions,events and explorations and the countries.
            -This section should also include the Global conlficts such as wars and worldwide oil and gas production and prices.
            -The Generated content must not contain any local news for egypt.
            -news especially like wars and conflicts must be in details as long as possible.
            -For each event or news that are highly related mention the content in 100 words and how its affecting the industry of oil and gas the current year.
            -Include the citation source.
            -If there's prices or comparisons list them in a table.
            -note that today's date is {date_string} anything beyond add it as forcasting


            

        """,
        "bing_query": ["الاخبار العالميه و الصراعات الاقليميه المتعلقه بالتاثير علي اسعار المواد البتروليه"
                       ,"واردات عالميا للمواد البتروليه و الغاز الطبيعي",
                       "تصدير عالميا للمواد البتروليه",
                       "استهلاك عالميا من المواد البتروليه",
                       "اكتشافات عالميا في مجال الطاقه و البترول و الغاز",
                       " اسعار خام البرنت و اسعار غرب تكساس",
                       "the effect of the MENA region/regional conflicts on the oil and gas industry globally on",
                       "presidential elections effects on oil and gas industry",
                       "countries with the most oil and gas production",
                       "effect of russian-ukraine war on oil and gas prices/supply and demand/production",
                       "effect of Iran-Israel war on oil and gas prices/supply and demand/production",
                       "effect of Lebanon-Israel war on oil and gas prices/supply and demand/production",
                       "effect of hamas-Israel war on oil and gas prices/supply and demand/production",
                       "effect of Mena region conflicts on oil and gas prices/supply and demand/production",
                       "Oil and gas updates in Gulf, USA , Russia ,China and Iran",
                       "International penalties and regulations that bans some countries from the process of oil/gas manufacturing and export/import"
                       
                       ],
        
    },

    "Market Statstics 2": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Market forecast:
           -After retreiving the Market updates earlier in the previous prompts , generate a market forecast to analyze the current state of the oil and gas industry worldwide in Egypt.
           
        [Instructions]:
            -after you fetch all these data make it detailed , to the point , highlight the statistics , numbers , reasons for each number wth the illustration.
            -for the forecast make in in a timerseries graph or tables or charts.
            -your forecast should be supported with facts,events such as conflicts,statistics from the latest maarket updates in Egypt and worldwide generated before.
            -Include the citation source.
            
            -Be specific , detailed oriented and include details as much as possible.
            -Don't include any conclusions.
            -Make it 3 paragrphs long.
            -Avoid contradictions.
            -The results MUST be in a table.
            - note that today's date is {date_string} anything beyond add it as forcasting

            
        """,
        "bing_query":["Forecasting for oil and gas industry worldwide and egypt and the effects of the conflicts on the forecast aftef",
        "all worldwide presedential elections effects on oil and gas production",
        "supply and demand for oil and gas predictions aftef",
        "predictions of the global wars/conflicts on the prices on oil and gas aftef"
        ],
        
        
    },
    "Competitive Analysis": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Competitive analysis for oil and gas according to fitch report:
        - Egyptian Market key players if present in the report.
        - International Market players if present in the report.
        - Include Numbers statistics , Market shares if possible.
        [Instructions]:
            -Make 4 to 5 lines maximum for The Egyptian Market key players.
            -Make 4 to 5 lines maximum for The international Market key players.
            -Then after you make the 2 paragraphs ,Make them in a structured table with their statistics.
            -Include all the market key players with their statistics.
            -Be specific , detailed oriented and include details as much as possible.
            -Include their market shares if present in a table as numbers not percentages.
            -If not sure skip the sections.
            -Don't include any conclusions.
            -Include the citation source.
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
        
    },
    "Competitive Analysis 2": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Competitive analysis for oil and gas according to latest updates:
        - Egyptian Market key players if present in the report.
        - International Market players if present in the report.
        - Include Numbers statistics , Market shares if possible.
        [Instructions]:
            -Make 4 to 5 lines maximum for The Egyptian Market key players.
            -Make 4 to 5 lines maximum for The international Market key players.
            -Then after you make the 2 paragraphs ,Make them in a structured table with their statistics.
            -Include all the market key players with their statistics.
            -Include their market shares if present in a table as numbers not percentages.
            -Be specific , detailed oriented and include details as much as possible.
            -Don't include any conclusions.
            -Include the citation source.
            - note that today's date is {date_string} anything beyond add it as forcasting

            

        """,
        "bing_query": ["اهم اللاعبين الرئيسين في سوق النفط و الغاز الطبيعي في مصر و نسب الاستحواذ",
                       "اهم اللاعبين في سوق النفط و الغاز الطبيعي علي مستوي العالم",
                       "include companies like Eini , total energies, enpi , petrojet , chevron , bb in Egypt"
                ],
                
        
    },
    "BM market research": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Market research:
        -Generate the market research from the given data tables in [Data_1] and [Data_2] where both of them are tables.
        ------------------------------------------------------------
       [Data_1]
        Company EBITDA Margin NPM ROE ROA Current Ratio Fin. Lev. Debt/Equity OCF (EGP Mn) FCF (EGP Mn) FCF/OCF Revenue (EGP Mn) % 4 y-o-y Net income (EGP Mn) % 4 y-o-y Total assets (EGP Mn) Total liab. (EGP Mn)
        Egypt Gas Co SAE -55% 11% 5% 1.30% 1 3.85 3.30% -2,462 -288 -12% 1,318 30% 1,390 48% 16,732 12,394
        --------------------------------------------------------------------------------------
        [Data_2]
        Company EBITDA Margin NPM ROE ROA Current Ratio Fin. Lev. Debt/Equity OCF (EGP Mn) FCF (EGP Mn) FCF/OCF Revenue (EGP Mn) % 4 y-o-y Net income (EGP Mn) % 4 y-o-y Total assets (EGP Mn) Total liab. (EGP Mn)
        Alexandria Mineral Oils Co 6% 5% 31% 19% 2.3 1.7 0.40% 33.58 -13.6 -40% 8,473 21% 393 -5% 7,642 3,142
        TAQA Arabia 8% 3% 4% 1% 1 5.3 250% -12.33 -182.7 -1482% 3,577 22% 99 -2% 17,382 14,076
        Mean Average 7% 4% 17% 10% 1.7 3.5 125% 10.63 -98.15 -761% 6,025 22% 246 -4% 12,512 8,609



            [Instructions]:
            your role is a risk manager who works in credit approvals in banking sector , do the following:
                -The section should be named "تقرير اداره ابحاث السوق".
                -Generate the tables given in [Data_1] and [Data_2] make the columns as rows and rows as columns in the response.
                -Make Names for both [Data_1] and [Data_2] tables from what you understand.
                -Comment on each table separtly in [language] make it detailed .
                -Make sure the data is relevant to our context Oil and Gas industry in Egypt.
                -Don't include any conclusions.
                -Include the citation source here it's market research by Banque misr team.
                - note that today's date is {date_string} anything beyond add it as forcasting

                
        """,
        "bing_query": None,
        
        
    },
    "SWOT analysis": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Strengths weakness oppourtuintes threas analysis:
        -Generate and Extract Strengths , weakness , opportuinties and threats concerning the Oil and Gas Market in Egypt from the Given Data.
        -Make sure there's no contradictions.

        [Instructions]:
            -Generate the response as a table.
            -Illustrate the reasons for the swot analysis from the data in context.
            -Make sure the data is relevant to our context Oil and Gas industry in Egypt.
            -Be specific , detailed oriented and include details as much as possible.
            -Don't include any conclusions.
            -Include the citation source.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

        """,
        "bing_query": ["Swot analysis for oil and gas in Egypt",
        "strengths , weakness,opportuinties,threats for oil and gas industry in Egypt"],
        
    },

    "Regulatory framwork & antidumping laws": {
        "prompt": f"""
        Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### Anti dumping laws and Regulatory framework:
        -Generate antidumping laws for oil and gas in egypt if found only!.
        -Genereate the regulatory framework for oil and gas in egypt.
        [Instructions]:
            -just 2 paragraphs one per each
            -Don't include any conclusions.
            -Include the citation source.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

        """,
        "bing_query": ["Antdumping laws for oil and gas in egypt ",
                       "Regulatory framework for oil and gas in Egypt"
                       ],
        
    },
    "Conclusion": {
            "prompt": f"""
            Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

            ### Conclusion:
            -Highligh the main highlights concerning the Oil and Gas Market in Egypt and worldwide
            -Include a constructive forecast regarding the Oil and Gas after the current year based on the information you knew earlier from the previous prompts.
            -Illustrate your forecasts reasons

            [Instructions]:
                -1 paragraph.
                -Detailed and focusing on the main highlights.
                -Include latest projects mentioned earlier or explorations.
                -Include the Oppourtuinties for it.
                - note that today's date is {date_string} anything beyond add it as forcasting
                
            """,
            "bing_query": None,
            
        },
}
real_estate_prompts = {
    "Introduction": {
        "prompt": f"""
        Generate the following sections in [language]: 

        # A comprehensive analysis of the Real Estate industry

        ### Industry Overview:
        - Discuss the significance of the real estate sector to the economy, including its role in economic growth, job creation, and infrastructure development.
        - Highlight the diversity and importance of the real estate sector, considering various sub-sectors like residential, commercial, and industrial properties, as well as urbanization trends.

        ### Real Estate Market Statistics {int(current_year) - 14} - {current_year}:
        - Provide a detailed analytical statement on the growth of real estate investments, total housing units constructed, and total property transactions.
        - Include a table with the following columns: Year, Total Investments (in billion dollars), Number of Housing Units (in thousands), and Total Property Transactions.
        - Add accurate sources.

        ### Real Estate Sector Performance {int(current_year) - 2} - {current_year}:
        - Discuss key growth drivers, including rising urbanization rates, foreign direct investments (FDI), and major real estate projects by prominent developers. Be specific.
        - Highlight key governmental policies, regulatory updates, and initiatives to promote affordable housing and real estate development. Be specific.
        - Include significant updates from the Ministry of Housing, or related authorities. Be specific.
        - Add sources.

        ### Importance of the Real Estate Industry in Egypt:
        - Your output will be for a risk manager working in credit approvals in the banking sector. Provide information to help them approve or reject credit applications.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
    },
    
    "Market Updates in Egypt": {
        "prompt": f"""Generate the following sections in [language]: 
        Your output will be for a risk manager working in credit approvals in the banking sector. Provide information about the real estate industry to help with credit decisions.
        
        Generate the following section:

        ### Market Updates and Latest News in Egypt {int(current_year) - 2} - {current_year}:
        - Provide the latest news and statistical data from reliable sources concerning the real estate industry, focusing on:
          - Egypt: Highlight recent developments, trends, and statistical insights impacting the real estate sector, including residential, commercial, and infrastructure updates.
          - The impact of the increase in refugees in Egypt on the real estate sector.
          - Consumption, production, exports, and imports.
        - Add the source names (no links).
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": [
            'اخبار السوق العقاري في مصر',
            'تأثير اللاجئين على سوق العقارات في مصر' ,
            'حركه الاسكان و البناء و التصزير العقاري في مصر حاليا' ,
            'احدث قرارات مجلس ادراه هيئه المجتمعات الغمرانيه '
        ],
        
    },
    
    "Market Updates Globally": {
        "prompt": f"""Generate the following sections in [language]: 
        Your output will be for a risk manager working in credit approvals in the banking sector. Provide information about the real estate industry to help with credit decisions.

        ### Market Updates and Latest News Globally {int(current_year) - 2} - {current_year}:
        - Provide the latest news and statistical data from reliable sources concerning the real estate industry, focusing on:
          - Global: Highlight recent developments, trends, and statistical insights impacting the real estate sector, including residential, commercial, and infrastructure updates.
        - Add the source names (no links).
        - note that today's date is {date_string} anything beyond add it as forcasting
        
        """,
        "bing_query": ['اخبار التطوير العقاري عالمياً'],
        
    },
    
    "Market Statstics": {
        "prompt": f"""Generate the following sections in [language]: 
        Your output will be for a risk manager working in credit approvals in the banking sector. Provide information to help them approve or reject credit applications.

        ### Real Estate Sector in Egypt - Analysis:
        - Discuss the following:

        ### Consumption:
        - What are the current trends in real estate consumption in Egypt?
        - How do factors like population growth, urbanization, and economic conditions influence real estate demand?

        ### Production:
        - What is the current state of real estate production in Egypt?
        - Identify major players in the market and their contributions to the housing supply.
        - Discuss any government initiatives or regulations that affect production.

        ### Exports:
        - Examine the role of the real estate sector in Egypt's export economy.
        - What types of real estate products or services are being exported, and to which countries?
        - Assess the impact of foreign investment in the Egyptian real estate market.

        ### Imports:
        - Identify key imports related to real estate, such as building materials and technologies.
        - How do import trends affect the real estate market in Egypt?
        - Discuss any challenges or barriers related to imports in the real estate sector.
        - Add the source names (no links).
        - note that today's date is {date_string} anything beyond add it as forcasting

        
        """,
        "bing_query": None,
        
    },
    
    "Competitive Analysis": {
        "prompt": f"""Generate the following sections in [language]: 
        Your output will be for a risk manager working in credit approvals in the banking sector. Provide information to help them approve or reject credit applications.

        ### Competitive Landscape Analysis:
        - Create a detailed comparison between the largest real estate development companies in Egypt, including Talaat Moustafa Group (TMG), Palm Hills Developments, Amer Group, SODIC, and City Edge Developments.
        - The table should include the following columns:
          - Geographic Spread: Regions, cities, or international markets where the company operates.
          - Notable Properties/Flagship Projects.
          - Ownership/Management: Key executives or strategic partnerships.
          - Property Offerings: Types of developments (residential, commercial, mixed-use).
          - Pricing Strategies.
          - Profits & Financial Performance.
          - Customer Segments.
          - Unique Selling Points.
          - Sales Promotions & Offers.
          - Future Expansion Plans.

        - Provide updated data for {int(current_year) - 1} or later.
        - Add sources (names only, no links).
        - note that today's date is {date_string} anything beyond add it as forcasting
        
        """,
        "bing_query": None,
        

    },
    'BM market research' :{
        "prompt": f"""Generate the following sections in [language]: 
        Your output will be for a risk manager who works in credit approvals in the banking sector. Please ensure that you provide information about the industry to help the risk manager approve or reject credit.

        Generate the following sections in [language] language and format them according to the required structure in the [Instructions]:

        ### Our Bank's Market Research Department Report on the Industry July {current_year}:

        - Generate the market research based on the given data tables in [Data_1], where both of them are tables.

        ------------------------------------------------------------
        [Data_1]
        1Q24 figures, Financial Performance, Financial Position, Cash Flow Position, Key P&L Figures, Key B/S Figures
        EBITDA Margin, NPM, ROE, ROA, Current Ratio, Fin. Lev., Debt/Equity, OCF (EGP Mn), FCF (EGP Mn), FCF/OCF, Revenue (EGP Mn), % 4 y-o-y, Net income (EGP Mn), % 4 y-o-y, Total assets (EGP Mn), Total liab. (EGP Mn)
        Talaat Mostafa, 35%, 61%, 9%, 2.8%, 1.2, na, 31%, 654, "-5,7,844", na, "6,792.1", 53%, "4,136", 490%, "297,511", "18,1,083"
        Sixth of October Development and Investment, 21%, 21%, 19%, 4.3%, 1.4, na, 44%, 312, 284, 90%, "1,839.1", 23%, 392, 105%, "41,197", "32,121"
        Palm Hills, 29%, 17%, 22%, 3.6%, 0.9, na, 114%, 629, 549, 87%, "6,228.6", 77%, "1,050", 309%, "8,6,033", "7,3,415"
        Amer Group, 31%, 5%, 1.7%, 0.2%, 1.1, 6.6, 104%, 98, 88, 90$, 265.4, -32%, 15, -64%, "7,167", "6,098"
        Mean Average, 29%, 26%, 13%, 3%, 115%, 660%, 73%, "42,325", "-1,423,075", 89%, "3,781", 30%, "1,398", 210%, "107,977", "73,179"

        [Instructions]:
        Your role is a risk manager who works in credit approvals in the banking sector. Please do the following:
            - Name the section "Our bank's market research department report on the industry for the month of July {current_year}".
            - Generate the tables given in [Data_1] as part of your response.
            - Assign meaningful names to both [Data_1] tables based on your understanding.
            - generate the table columns as rows and rows as columns
            - Comment on each table separately in [language] and provide detailed analysis.
            - Ensure the data is relevant to the context of the Information real estate industry in Egypt.
            - Do not include any conclusions.
            - Cite the source as: Market research by Banque Misr team.
            - note that today's date is {date_string} anything beyond add it as forcasting
        
        """, 
        "bing_query": None,
        "use_pdf": False,
    
    },
    
    "SWOT analysis": {
        "prompt": f"""Generate the following sections in [language]: 
        Your output will be for a risk manager working in credit approvals in the banking sector. Provide information to help them approve or reject credit applications.

        ### SWOT Analysis for Real Estate in Egypt:
        - Generate a SWOT analysis table that includes strengths, weaknesses, opportunities, and threats for the real estate sector in Egypt.
        - Include Population increase in the analysis.
        - Add the source names (no links).
        - note that today's date is {date_string} anything beyond add it as forcasting
        
        """,
        "bing_query": None,
        

    },
    
    "Conclusion": {
        "prompt": f"""
        Generate a conclusion in [language]:
        ### Conclusion:
        - Summarize the key points concerning the real estate market in Egypt and globally.
        - Provide a constructive forecast for the market after {current_year} based on the information discussed earlier.
        - Highlight key opportunities in the real estate market.
        - note that today's date is {date_string} anything beyond add it as forcasting

        
        """,
        "bing_query": None,
        
    }
}
AUTOMOTIVE_prompts= { 
    "Introduction": {
        "prompt": f"""Generate the following sections in [language]:
        
    # A comprehensive analysis of the AUtomotive, spare parts, Service centers, Logistics and public transportation industry
    
    ### Introduction and Industry Significance
      -Provide an introduction and characteristics about automotive, spare parts,cars service and logistics and public transportation industry in the Egyptian market.
      - Emphasize the previous industry's importance in 2 or 3 pargraphs as follows:
          - Discuss the importance of the industry in economic and industrial development.
          - Explain how the industry contributes to Egypt's GDP, employment, and revenue.
          - Describe its connections with other industries.

    ### Regional Overview
    Autos Investment Round-Up: North Africa-GCC Investment Competition Heating Up
        - Provide the major trends,projects and developments for automotive,spare parts and logistice and publice transportations in the MENA.
        - Discuss the Middle East And North Africa - Autos Production Investment (Q323).   

    Formatting Notes:
    - Ensure the report is well-structured, with clear headings and subheadings for each section. Include data visualization (tables or charts) where necessary to support the analysis.
    - Ensure the report is comprehensive and provides statistical information and a clear picture of the current state and future prospects of the contracting, construction, and building industry in Egypt. Cite sources found under each section. Do not add a conclusion.
    - Ensure that the analysis is professionally structured in [language].
    - Avoid hallucinating information and ensure accuracy by relying on credible sources.
    - Cite sources if found under each section.
    - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
    },
   "Automotive Types": {
      "prompt": f"""Generate the following sections in [language]:
    ### Automotive Types:
    - Provide detailed information on various types of vehicles, including electric vehicles and traditional combustion engines, highlighting their market performance and sales.
    - Include a comparison table for the Total Market Split for YTD {int(current_year) - 1} vs. YTD {int(current_year) - 2}.
    - Focus on the automotive industry in Egypt, covering the following categories:
      - **Passenger Cars**: Market Split YTD {current_year} vs. YTD {int(current_year) - 1}
      - **Buses, Mini Buses, and Microbuses**: Market Split YTD {current_year} vs. YTD {int(current_year) - 1}
      - **Trucks and Commercial Vehicles**: Market Split YTD {current_year} vs. YTD {int(current_year) - 1}
    - Provide production, sales statistics, and latest updates for each vehicle type in the Egyptian market. Present these in a table format with values and specific dates, where applicable.
    - note that today's date is {date_string} anything beyond add it as forcasting
    """,
      "bing_query": None,
    },
    "Market Updates": {
        "prompt": f"""Generate the following sections in [language]:
        ### Market Updates and News:
    - Provide a deeply comprehensive and detailed update on the automotive industry in Egypt, covering the following aspects:
        - detailed Key market insights and trends for AUtomotive, spare parts, Service centers, Logistics and public transportation industries.
        - Latest developments, projects, and initiatives in details for AUtomotive, spare parts, Service centers, Logistics and public transportation industries.
        - Impact of financial, economic, and political factors (e.g., wars, policies) on production, sales, and pricing within the automotive sector in Egypt and globally.
   - Clearly distinguish between global and local news, with separate sections for Egypt-specific updates.
    - Include tables or charts summarizing the performance of different vehicle types and spare parts.
    - Cite sources where available, ensuring that all information is accurate, detailed, and free from hallucination.
    - Extract data from any charts or graphs into appropriate table formats where applicable.
    - note that today's date is {date_string} anything beyond add it as forcasting
    """,
      "bing_query": [
        "أحدث تطورات قطاع السيارات في مصر",
        "أسعار السيارات الكهربائية ووسائل النقل مصر",
        "ابرز موردو قطع غيار السيارات في مصر",
        "توزيع قطع غيار السيارات مصر",
        "مراكز خدمه وصيانة السيارات المعتمدة مصر",
        "شركات الخدمات اللوجستية ومقدمو حلول النقل مصر",
        "أداء قطاع السيارات وقطع الغيار في مصر",
        "تأثير السياسات والاقتصاد على مبيعات السيارات مصر",
      ],
    },
    "Market Statstics": {
        "prompt": f"""Generate the following sections in [language]:
        #### Sales and production Analysis:
        1-Total Sales Figures: 
            -Extract and present a table showing Total Market April {current_year} Sales Analysis in volume figures for different vehicle categories. Ensure accuracy by pulling the data directly from any relevant charts, graphs or any viualize insights.

        2-Comparative Sales Performance of Leading Brands: 
            -Generate a table presenting and comparing sales performance across brands (top 5), ensuring accuracy without any extrapolation or predictions.

        3-PC Market Sales Analysis: 
            -Present a detailed PC Market Split April {current_year} April {int(current_year) - 1} in volume Include the monthly sales volume and any relevant data points from relevant charts, graphs or any viualize insights and tables.
            -Present a detailed PC Market Split YTD {current_year} YTD  {int(current_year) - 1} in volume
            -Present a detailed PC Market April {current_year} Sales Analysis in volume, Include the monthly sales volume and any relevant data points from relevant charts, graphs or any viualize insights and tables.

        4-PC Market YTD by Brand Origin: 
            -Extract and present a year-to-date comparison of sales by PC Market YTD {current_year} - {int(current_year) - 1} By Brand Origin by pulling the data directly from any relevant charts, graphs or any viualize insights..

        5-Buses Market Sales Analysis: 
            -Extract and present the Buses Market Sales analysis in volume for April {current_year} and December {int(current_year) - 1} in table format by pulling the data directly from any relevant charts, graphs or any viualize insights.
            -Extract and present the Buses Market Sales April  {current_year} Analysis in volume in table format by pulling the data directly from any relevant charts, graphs or any viualize insights.
            -Extract and present the Buses Market Split April {current_year} April {int(current_year) - 1}
            -Buses Market Split YTD {current_year} - YTD {int(current_year) - 1}
        6-Trucks Market Split: 
            -Present the Trucks Market Split April {current_year} – April {int(current_year) - 1} in table format by pulling the data directly from any relevant charts, graphs or any viualize insights.
            -Present the  Trucks Market Split YTD {current_year} – YTD {int(current_year) - 1} in table format by pulling the data directly from any relevant charts, graphs or any viualize insights.
            -Present the sales analysis for the Trucks Market April {current_year} Sales Analysis in volume, in table format by pulling the data directly from any relevant charts, graphs or any viualize insights.

        -Instructions:
            -Ensure each category is represented accurately and Double-check that all data points and values from the relevant charts and tables are captured in the analysis based on the data available by pulling the data directly from any relevant charts, graphs or any viualize insights.
            -Ensure leaving no missing values.
            -Language: All tables and text should be in [language], with proper right-to-left alignment.
            -Data Extraction: Accurately extract data and all values from charts and graphs and present it in table format.
            -Source Citation: Cite sources under each section.
            -Ensure data accuracy by using only the available figures without forecasting or predictions.
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
        "bing_query": None,
    },
    "Competitve Analysis": {
        "prompt": f"""Generate the following sections in [language]:
        ### Competitive Landscape of Egypt's Automotive Sector
        -Provide an overview of the competitive landscape in Egypt's automotive sector, focusing on key players and brand performance. 
        -Generate a comprehensive analysis that includes the following data points:
        1.Total Market by Brand:
          Extract and present the following in a table format by pulling the data directly from any relevant charts, graphs or any viualize insights:
            -Total Market by Brand April {current_year} - April {int(current_year) - 1}– in Volume.
            -Total Market by Brand April {current_year} - April {int(current_year) - 1} –in Market Share.
            
        2.PC Market by Brand:
           -Extract and present the following in a table format by pulling the data directly from any relevant charts, graphs or any viualize insights:
                -PC Market April {current_year} Sales Analysis in volume.
                -PC Market by Brand April {current_year} April {int(current_year) - 1} in volume
                -PC Market by Brand April {current_year} – April {int(current_year) - 1} in Market Share 
        3.PC CKD by Brand:
          -Extract and present the following in a table format by pulling the data directly from any relevant charts, graphs or any viualize insights:
            -CPC CKD By Brand April {current_year} April {int(current_year) - 1} in Volume.
            -PC CKD By Brand April {current_year} April {int(current_year) - 1} in Market Share.
            
        4.PC CBU by Brand:
            -Present the PC CBU By Brand April {current_year} April {int(current_year) - 1} in Volume in table format by pulling data and values from any relevant charts, graphs or any viualize insights
            -Present the PC CBU By Brand April {current_year} April {int(current_year) - 1} in Market Share by pulling data and values from any relevant charts, graphs or any viualize insights.
            
        5.Buses Market by Brand:
          -Extract and present the following in a table format by pulling the data directly from any relevant charts, graphs or any viualize insights:
            - Provide a Buses Market By Brand April {current_year} –April {int(current_year) - 1} in volume.
            - provide a Buses Market By Brand April {current_year} – April {int(current_year) - 1} in market share.
           
        6.Trucks Market by Brand:
          -Extract and present the following in a table format by pulling the data directly from any relevant charts, graphs or any viualize insights:        
            - Include the Trucks Market By Brand April {current_year} April {int(current_year) - 1} in Volume
            - Trucks Market By Brand April {current_year} – April {int(current_year) - 1} in Market Share.
        [instruction]
    - Data Extraction: Accurately extract all data and values from charts, graphs, or any visualized insights and present them in a table format.
    - Ensure to extract all relevant data directly from the visualizations, leaving no values empty or missing.
    - Clearly indicate each brand's market position based on the extracted data.
    - Format the table in [language], ensuring right-to-left alignment, with bold and centered headers.
    - Provide consistent and accurate data for both sales volumes and market shares across all metrics.
    - Use proper numerical formatting (e.g., currencies, units) and align data correctly in each column.
    - Ensure all data is clearly labeled with units (e.g., currencies, percentages, units).
    - note that today's date is {date_string} anything beyond add it as forcasting
    """,
        "bing_query": None,
    },
    "BM Market Research":{
        "prompt": f"""Generate the following sections in [language]:
        ### Bank Market Research Department Industry Report:
        -Extract and Generate a Table: Based on the provided financial performance data from the ODF file, create a clear table with correct alignment and formatting. Separate and organize the financial metrics for GB Auto, MTI Auto, and MTI Consumer Electronics into the following categories:
                | Company                    | Financial Performance | Financial Performance | Financial Performance | Financial Performance | Financial Position | Financial Position | Financial Position | Cash Flow Position | Cash Flow Position | Cash Flow Position | Key P&L Figures   | Key P&L Figures          | Key P&L Figures   | Key P&L Figures              | Key B/S Figures    | Key B/S Figures            |
        |----------------------------|-----------------------|-----------------------|-----------------------|-----------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|-------------------|-------------------------|-------------------|----------------------------|--------------------|----------------------------|
        |                            | EBITDA Margin          | NPM                   | ROE                   | ROA                   | Current Ratio       | Fin. Lev.          | Debt /Equity        | OCF (EGP Mn)        | FCF (EGP Mn)        | FCF/OCF            | Revenue (EGP Mn)   | % D y-o-y (Revenue)     | Net Income (EGP Mn)| % D y-o-y (Net Income)     | Total Assets (EGP Mn) | Total Liabilities (EGP Mn) |
        | GB Auto                    | 19%                   | 7%                    | 12%                   | 5%                    | 1.3                | 2.4                | 72%                | 1,359              | -152               | -11.2%             | 9,006             | 90%                     | 667               | 542%                       | 53,297             | 30,795                     |
        | MTI Auto                   | 23%                   | 15%                   | 9%                    | 6%                    | N/A                | 1.6                | N/A                | N/A                | N/A                | N/A                | 608               | 102%                    | 93                | 118%                       | 1,560              | 582                        |
        | Mean Average               | 21%                   | 11%                   | 11%                   | 6%                    | 1.3                | 2.0                | 72%                | 1,359              | -152               | -11.2%             | 4,807             | 96%                     | 380               | 330%                       | 27,429             | 15,689                     |
        | MTI Consumer Electronics    | 10%                   | 7%                    | 11%                   | 6%                    | N/A                | 1.9                | N/A                | N/A                | N/A                | N/A                | 2,097             | 9%                      | 149               | 45%                        | 2,606              | 1,218                      |

        -Source Citation: Cite all sources directly under the table "internal market reseach by our sectof"
        - note that today's date is {date_string} anything beyond add it as forcasting
        - generate the table columns as rows and rows as columns
        """,
        "bing_query": None,
    },
    "SWOT Analysis": {
        "prompt": f"""Generate the following sections in [language]:
      ### SWOT Analysis:
        - Provide in a matrix table SWOT analysis for the industry in Egypt as follows:
            - Strengths: List and describe key strengths in points format.
            - Weaknesses: List and describe key weaknesses in points format.
            - Opportunities: List and describe potential opportunities in points format.
            - Threats: List and describe potential threats in points format.
        Ensure that each category (Strengths, Weaknesses, Opportunities, Threats) is centered and bolded in the table matrix.
        Provide citations from credible sources directly under each section.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
    },
    "Economic Conditions": {
        "prompt": f"""Generate the following sections in [language]:
        ### Economic Conditions:
        -Detailed Discussion: Provide an in-depth discussion of Egypt's current economic conditions impacting the construction sector, including:
            -Tax Regime and Incentives: Outline Egypt's tax policies, incentives, and regulations in the construction industry, highlighting any recent changes and their impact on the sector.
            -Global Dependency and Egypt’s Economic Concerns: Discuss four key issues Egypt faces due to global dependencies:
                -International market fluctuations
                -Trade dependencies
                -Currency exchange rate impacts
                -Economic stability concerns
                -POLITICAL concerns including wars...etc.
        -Data Extraction from Graphs/Charts: Extract relevant data from graphs or charts and present them in table format, ensuring the numbers are clearly represented.
        -Source Citation: Cite all sources directly under each section.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
    },
    "Conclusion": {
        "prompt": f"""
        Generate the following sections in [language]:
       ### Conclusion:
         -Data-Backed Summary: Offer a balanced conclusion on whether Egypt's automotive industry is likely to face challenges in the coming years. Base your analysis on:
            -Current economic conditions
            -Market dynamics
        -Make sure the conclusion aligns with the previous sections and relies strictly on available facts without speculative predictions.
        -Cite all sources directly under each section.
        - note that today's date is {date_string} anything beyond add it as forcasting
    """,
        "bing_query": None,
    },
}
construction_prompts = { 
    "Introduction": {
            "prompt": f"""Generate the following sections in [language]: 

            # A comprehensive analysis of the Construction industry

            ### Introduction and Industry Significance
            - Provide an introduction and characteristics about the industry in the Egyptian market in one paragraph.
            - Address the capital-intensive nature of the sector and its market dynamics in one paragraph.
            - دور قطاع المقاولات في الصناعات المكملة والتي تعتمد بشكل اساسى على العمليات التي يتم تنفيذها سواء داخليا او خارجيا 
        اضافه امثلة اكبر عن الشركات العاملة في السوق المصرى او الدولى  ( ريدكون - ccc ) وغيرها 
                - دور النشاط في الصناعات المكملة والتي تساهم على خدمه القطاع 

            - Emphasize the industry's importance as follows:
                - Discuss the importance of the industry in economic and industrial development.
                - Explain how the industry contributes to Egypt's GDP, employment, and revenue.
                - Describe its connections with other industries.

            ### Construction Sector Overview in the Middle East
                - Provide the major trends and developments in the MENA construction sector.
                - Discuss in detail the broader trends, challenges, and developments in the industry across the MENA region.
                - Discuss the most recent projects in MENA.
                -امثله عن المشروعات في السعودية والامارات والتي تقوم بتنفيذها شركات مصرية 
                -Examples about the projects in KSA and UAE ( with names and statistcs) in which Egyptian companies are supervising it.
                - Projects should be mentioned by name , statistics , numbers ( no generic information).


            Formatting Notes:
            - Ensure the report is well-structured, with clear headings and subheadings for each section. Include data visualization (tables or charts) where necessary to support the analysis.
            - Ensure the report is comprehensive and provides statistical information and a clear picture of the current state and future prospects of the contracting, construction, and building industry in Egypt. Cite sources found under each section. Do not add a conclusion.
            - Ensure that the analysis is professionally structured in [language].
            - Avoid hallucinating information and ensure accuracy by relying on credible sources.
            - Cite sources if found under each section.
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": ["major trends and developments in the MENA construction sector"
                        "construction projects in MENA region",
                        "Construction Projects in KSA",
                        "Construction projects in UAE",
                        "Partnership between Egyptian Construction companies and Gulf countries"
                        
                        
                        ],
            
        },
    "Market Updates in Egypt": {
            "prompt": f"""Generate the following sections in [language]: 
        ### Market Updates and News Locally:
        - Provide industry updates, news, trends, initiatives, and all projects in Egypt based on the following categories:
        - The latest developments, trends, and projects in Residential/Non-Residential Building.
        - The latest developments, trends, and projects for properties, real estate, and infrastructure updates.
        - The latest updates, trends, projects, and initiatives for ports and airport projects.
        - The latest updates and initiatives for transportation and road projects.
        - Partnerships or agreements between banks and realestate companies such a banque misr-NBE-palmhills agreement.
        - Projects should be mentioned by name , statistics , numbers ( no generic information).
        
        
        Formatting Notes:
            - Clearly discuss the local news in Egypt in detailed sections.
            - Projects should be mentioned by name , statistics , numbers ( no generic information).
            - Every headline or event or project must contain ( specific naming, numbers and statistics).
            - Avoid fabricating information and ensure accuracy by relying on credible sources.
            - Cite sources for each section where available.
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            """,
            "bing_query": [
                "latest news in Egypt about developments in residential buildings",
                "latest news in Egypt about developments in non residential buildings",
                "latest news in Egypt about developments in administration buildings",
                "latest news in Egypt about airport expansions",
                "investements in realestate projects in Egypt ",
                "investements in transportation projects in Egypt ",
                "Egyptian banks such as banque misr,NBE funding for construction projects",
                "Egyptian military investements in construction sector in Egypt",
                "Egyptian investements in constructions such as new adminstrative capital , el alamin el gedida",
                "Investements in Ras el hikma",
                "شركات ترسانة البحر الاحمر"


            ],
            
        },
    "Market Updates Globally": {
            "prompt": f"""Generate the following sections in [language]: 
        ### Market Updates and News Globally:
        - Provide industry global updates, news, trends, and initiatives based on the following:
        - Mention any significant economic measures and their impact on the industry.
        - Mention any significant projects, initiatives, and news that help the industry.
        - Provide insights on global trends, along with any factors influencing these trends.
        - Geopolictical effects and conflicts on the Egyptian industry of construction {current_year}.
        - examples for construction projects in KSA , UAE in which the Egyptian companies will supervise. 
        - Egyptian construction companies that are working on contructional projects in the MENA region {current_year}.
        - Projects should be mentioned by name , statistics , numbers ( no generic information).
        
    
        [Instructions]:
            - Clearly discuss the global news related to Egypt in two distinct, detailed sections.
            - Be specific , detailed and to the point.
            - Projects should be mentioned by name , statistics , numbers ( no generic information).
            - Every headline or event or project must contain ( specific naming, numbers and statistics).
            - Avoid fabricating information and ensure accuracy by relying on credible sources.
            - Cite sources for each section where available.
            - note that today's date is {date_string} anything beyond add it as forcasting

            """,
            "bing_query": [ "Egyptian companies partnerships with Gulf companies in constructional sector",
                        "latest constructional projects in KSA",
                        "KSA investements in constructional projects",
                        "latest constructional projects in MENA region",
                        "MENA region investements in constructional projects",
                        "Geopolitical threats for construction industry such as Russia-ukraine war, Israel-Gaza war, Lebanon-Israel war, Iran-Israel waf",

                        
            

            ],
            
        },
    "Market Updates in egypt 2": {
            "prompt": f"""Generate the following sections in [language]: 
            #### Residential/Non-Residential Building
            - Mention the latest developments and projects in Residential/Non-Residential Building.
            - Mention the main Property Developers' updates and projects in detail.
            - Mention the numbers and statistics.
            - Mention expected/forecasted projects related to Construction
                --New cities , 
                --railways,
                --Power and electricity,
                --Airports,
                --Harbors in Egypt 
                ---either by external investment or internal investement each in a subsection.
            - Projects should be mentioned by name , statistics , numbers ( no generic information).

            [Instructions]:
            - Avoid hallucinating information and ensure accuracy by relying on credible sources.
            - Projects should be mentioned by name . statistics , numbers and investement(no generic information).
            - Be specific , detailed and to the point.
            - Generate in [language] language.
            - Cite sources at the end.
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            """,
            "bing_query": None,
            
        },
    "Market Updates in egypt 3": {
            "prompt": f"""Generate the following sections in [language]: 
            #### Energy Sector Infrastructure and Utilities:
            1. Latest Developments:
            - Provide an overview of the latest developments and key projects in the energy sector infrastructure and utilities.

            2. Sectors/Projects:
            **Nuclear Power Plants:**
            - Detail the latest developments and ongoing projects related to nuclear power plants in Egypt.
            **Green Hydrogen Projects:**
            - Present the latest updates and projects focused on green hydrogen, such as electric vehicles and green hydrogen electrolyzers production in Egypt.

            ##### Egypt - Major Energy And Utilities Infrastructure Projects
            - Indicators:
                - Project Name
                - Sector
                - Volume (USDmn)
                - Size
                - Status
            - Format:
            - Ensure the table is structured with indicators as columns.
            - The table should be in [language], with proper right-to-left and center alignment.
            - The first row and first column should be bold and centered.
            - Ensure the [language] text is correctly formatted with right alignment, and numerical data is clear.
            
            - Source Citation:
            - Cite sources directly under the table for each section, ensuring accuracy.

            Important Note:
            - Use accurate and available data. Do not attempt to forecast or predict numbers.
            - Avoid generating empty tables or any information that isn't directly supported by existing data.
            - Avoid hallucination; extract the table with all values and don't omit any information.
            - Projects should be mentioned by name , statistics , numbers ( no generic information).
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            """,
            "bing_query": None,
            
        },
    "Market Updates in egypt 4": {
            "prompt": f"""
            Generate the following sections in [language]: 
            #### Egypt - Major Energy And Utilities Infrastructure Projects:
            - Discuss how investment in power infrastructure in Egypt is expected to rise. Provide specific data and details about upcoming investments and projects.
            - Highlight the Major Energy and Utilities Infrastructure Projects in a detailed table format. include available information without mentioning or speculating about missing data.
            - Cite all sources directly under this section.
            
            ### Transport,harbors,airports,railways:
            - Latest Developments:
                - Provide an overview of the latest developments and key projects in Egypt's transportation sector.
                - mention Examples for the transportation sector with names, numbers and statistics.
                - Provide an overview of the latest developments and key projects in Egypt's harbors sector.
                - mention Examples for the harbors sector with names, numbers and statistics..
                - Provide an overview of the latest developments and key projects in Egypt's airports sector.
                - mention Examples for the airports sector with names, numbers and statistics..
                - Provide an overview of the latest developments and key projects in Egypt's road infrastructure.
                - mention Examples for the road infrastructure sector with names, numbers and statistics..
                - Provide an overview of the latest developments and key projects in Egypt's railways.
                - mention Examples for the railways sector with names, numbers and statistics.
                
            -[instructions]:

                --Projects should be mentioned by name , statistics , numbers ( no generic information).
                --For the latest Developments include some examples for each sector.
                --Cite all sources directly under this section.
                --avoid hallucination and ensure to provide accurate, appropriate values and table format.
                --Provide refrences for each information.
                - note that today's date is {date_string} anything beyond add it as forcasting

                
            """,
            "bing_query": ["latest news about latest Developments in Egyptian transportation sector",
                        "key projects in the Egyptian Transportation sector and investement like frequency bus",
                        "latest news about latest Developments in Egyptian harbors sector",
                        "key projects in the Egyptian harbors sector investement like ain el sokhna",
                        "the latest developments and key projects in Egypt's airports sector like sphynx airport",
                        "latest developments and key projects in Egypt's road infrastructure",
                        "the latest developments and key projects in Egypt's railways in like the monoreal"
                        "استثمارات النقل الحديث في مصر",
                        "استثمارات مصر في قطاع الموانئ البحريه",
                        "استثمارات مصر في توسيع المطارات",
                        "استثمارات مصر في قطاع تحسين الطرق",
                        "استثمارات مصر في قطاع السكه الحديد و منظومه النقل الحديث",
                        "استثمارات مصر في العاصمه الاداريه الجديده و العلمين الجديده"

                        ],
            
        },
    "Market Statstics": {
            "prompt": f"""Generate the following sections:
        ### Construction Forecast Scenario
        - Highlight the key view for industry expectations and the forecasted scenario.
        - Mention the latest expected developments for the industry.
        
        #### Forecasting for Construction Industry during {int(current_year) - 1} till 2033:
            - Construction And Infrastructure Industry Data (Egypt {int(current_year) - 1}-2033).
            - Indicators:
            - Construction industry value, EGPbn
            - Construction industry value, real growth, % y-o-y
            - Construction industry value, % of GDP
        - Format:
        - Ensure the table is structured with years as columns and indicators as rows, in horizontal format.
        - The table should be in [language], with proper right-to-left alignment and centered.
        - The first row and column should be bold and centered.
        - Ensure the [language] text is correctly formatted with right alignment, and numerical data is clear.

        - Source Citation:
        - Cite the sources directly under the table for each section, ensuring accuracy.
        - Commentary:
        - Provide a brief analysis of the data trends under the table, based on the extracted numbers.
        - Provide it in one paragraph, and mention that the prediction analysis is depending on current market factors.
        - note that today's date is {date_string} anything beyond add it as forcasting
        
            """,
            "bing_query": None,
            
        },
    "Competitive Analysis": {
            "prompt": f""" Generate the following sections:
            ### Competitive Landscape:
            - Mention the competitive landscape in the Egyptian market for key players.
            - Present an overview of the competitive landscape, detailing key companies, market shares of the companies, and their market positions for the construction industry.
            - Highlight significant local and foreign investments and partnerships.
            - Ensure sources are cited at the end.
            - Present this information in a detailed table in [language].
            
            ### Our Bank's latest Market Research Department Report on the Industry
            Provide latest market research updates table as the following indicators:
            -column index
                -EBITDA Margin 
                -NPM 
                -ROE 
                -ROA 
                -Current Ratio 
                -Fin. Lev. 
                -Debt /Equity
                -OCF(EGP Mn)
                -FCF(EGP Mn)
                -FCF/OCF
                -Revenue (EGP Mn)
                -% D y-o-y
                -Net income (EGP Mn) 
                -% D y-o-y
                -Total assets (EGP Mn)
                -Total liab. (EGP Mn)
            -row indicators:
                -Orascom
                -Giza Contracting and Real Estate
                -El-Saeed Contracting & Real Estate
                -Mean Average
        - Commentary:
            Provide a brief analysis of the data trends under the table, based on what u will find under the table if found.
            ensure to provide the table with well formatted index as well.
            Ensure sources are cited at the end.
            - note that today's date is {date_string} anything beyond add it as forcasting

            
            """,
            "bing_query": None,
            
        },
    "SWOT Analysis": {
            "prompt": f"""
            Generate the following sections:
            ### SWOT Analysis:
            - Provide in a matrix table SWOT analysis for the construction industry in Egypt as follows:
                - Strengths: List and describe key strengths in points format.
                - Weaknesses: List and describe key weaknesses in points format.
                - Opportunities: List and describe potential opportunities in points format.
                - Threats: List and describe potential threats in points format.
            Ensure that each category (Strengths, Weaknesses, Opportunities, Threats) is centered and bolded in the table matrix.
            Provide citations from credible sources directly under each section.
            - note that today's date is {date_string} anything beyond add it as forcasting

            
            """,
            "bing_query": None,
            
        },
    "Conclusion": {
            "prompt": f"""
            Generate the following sections:
            ### Economic Conditions:
            Provide a detailed discussion of the current economic conditions affecting Egypt's construction sector, including:
                - Tax Regime and Incentives: Outline the current tax policies, incentives, and regulations in Egypt's construction industry. Highlight any recent changes and discuss how they impact the sector.
                - Global Dependency and Egypt’s Economic Concerns: Describe four key issues Egypt faces due to global dependencies, such as:
                    - International market fluctuations
                    - Trade dependencies
                    - Currency exchange rate impacts
                    - Economic stability concerns
            Extract relevant data from graphs or charts in appropriate table format, ensuring numbers are clearly represented.
            Cite all sources directly under each section.

            ### Conclusion:
                - Provide a comprehensive, data-backed conclusion on whether the construction industry in Egypt is expected to face challenges in the coming years.
                - Offer a balanced view based on economic conditions, market dynamics, and other relevant factors.
                - Ensure the conclusion aligns with the previous sections and reinforces the overall analysis presented throughout the report.
            
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            """,
            "bing_query": None,
            
        },
}
tourism_prompts = {
    "Introduction": {
        "prompt": f"""
        Generate the following sections in [language]: 
        
        # A comprehensive analysis of the Tourism industry

        ### Industry Overview:
            - Introduction to Discuss the importance of the tourism industry to Egypt's economy, including its contribution to foreign exchange reserves and employment.
            - Highlight the diversity and vitality of the tourism sector in Egypt, considering the country's unique climate, rich history, cultural heritage, and geographical landmarks.
                - every player in a bullet point
        - Add the sources and the domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - keep the introduction consice 
            - All should be in [language]
            - never output you have no results
            - note that today's date is {date_string} anything beyond add it as forcasting   
        """,
        "bing_query" : None,
        
    },
    "Industry Statistics": {
        "prompt": f"""
        Generate the following sections in [language]:  

        ### Tourist Statistics in Egypt {int(current_year) - 3}-{current_year}):
           - Provide a detailed analytical statement of the Total arrivals, '000",
            visiting Egypt and the "International tourism receipts, USDbn" from {int(current_year) - 3} to {current_year}. Include a table with the following columns: Year, Number of Tourists (in millions), and Tourism Revenue (in billion dollars).
           - Add the sources and the domain name not the whole url like this [domain-name.top-level-domain].

        Instructions: 
            - do not add conclutions
            - All should be in [language]
            
            - statstics in {current_year} is not forcasting or expecting it is real numbers
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": ['Tourist Statistics in Egypt'],
        
    },
    "Industry Statistics 2": {
        "prompt": f"""
        Generate the following sections in [language]: 

        ### Tourism Sector Performance in Egypt ({int(current_year) -2} - {current_year}):
            - Discuss key growth drivers, including the increase in hotel occupancy rates and investments by leading global hotel groups, Be specific.
            - Highlight major developments and governmental efforts to re-evaluate and enhance hotel standards, Be specific.
            - Include significant updates from the Ministry of Tourism, Be specific.
            - Add the sources and the domain name not the whole url like this [domain-name.top-level-domain].

        ### Future Outlook in Egypt {int(current_year) + 1} - {int(current_year) + 4}:
           - Provide projections for the tourism sector, considering factors such as the impact of the Russia-Ukraine war, expected growth in tourist numbers, and anticipated revenue.
           - Include a table with projections for the number of tourists and tourism revenue for each year.
           - Add the sources and the domain name not the whole url like this [domain-name.top-level-domain].
        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - Note that Travco, Emaar Properties and Talaat Moustafa Group are not International
            - All should be in [language]
            
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
    },
    "Industry Statistics 3": {
        "prompt": f"""
        Generate the following sections in [language]: 

        ### Expectations of the tourism sector in Egypt during the coming period and the impact of any global conflict on the sector:
           - Create a table for Hotel Accommodation (Egypt {int(current_year) - 3} - {int(current_year) + 4}
             - Indicators: "Accommodation & food service nominal GVA, EGPbn", "Accommodation & food service EGP nominal GVA growth, % y-o-y"
               "Number of hotels and establishments,'000", "Total overnight stays, '000", "Average length of stay, nights",
               "Hotel rooms, '000", "Occupancy rate, % ".
             - Add comment on the table and inference (Dodn't add title).
             - Add the sources and the domain name of the url if there are any urls.
           - Include The impact of any global conflict on the Egyptian tourism sector.
             - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Note: every impact should have it's own paragraph


        Instructions: 
            - do not add conclutions
            - All should be in [language]
            
            - note that today's date is {date_string} anything beyond add it as forcasting            
        """,
        "bing_query": ['اخر اخبار الصراعات في العالم في', 'اخبار الفنادق في مصر','غزه',"اوكرانيا و روسيا"],
        
    },
    "Market updates in Egypt and Globally": {
        "prompt": f"""
        Generate the following sections in [language]: 

        ### Market Updates and Latest News {int(current_year) - 1}-{current_year}
            - Provide the latest news and statistical data from reliable sources concerning the tourism industry, focusing on:
              - Egypt: Highlight recent developments, trends, and statistical insights impacting the tourism sector.
              - Global Trends: Discuss overarching global trends influencing tourism worldwide, backed by credible statistics and analyses.
            - Include proper citations and sources for all information presented.
            - Add news about the major players in the tourism sector in Egypt

            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

        Instructions: 
            - do not add conclutions
            - All should be in [language]
            
            - note that today's date is {date_string} anything beyond add it as forcasting
            
        """,
        "bing_query": ['اخر اخبار السياحه في مصر', 'اخر اخبار السياحه العالميه',
         "ما هي آخر أخبار الفنادق في مصر",
        "ما هي آخر أخبار مجموعة طلعت مصطفى (TMG) في الفنادق ؟",
        "ما هي آخر أخبار مجموعة ترافكو (Travco) ؟" ,
        "ما هي آخر أخبار مجموعة بيك ألباتروس (Pickalbatros) ؟",
        "ما هي آخر أخبار مجموعة صن رايز (Sunrise) ؟",
        "ما هي آخر أخبار مجموعة ريكسوس (Rixos)؟",
        "ما هي آخر أخبار أوراسكوم للتنمية في الجونة ",
        "ما هي آخر أخبار فنادق ماريوت (Marriott) في مصر ",
        "ما هي آخر أخبار فنادق هيلتون (Hilton) في مصر ",
        "ما هي آخر أخبار فنادق أكور (Accor) في مصر ",
        "ما هي آخر أخبار مجموعة إنتركونتيننتال (IHG) في مصر؟",
            ],
        
    },
    "Market updates in Egypt and Globally 2": {
        "prompt": f"""
        Generate the following sections in [language]: 

        ### Industry Risks and Mitigation Strategies:
           - Identify key risks to the tourism industry, including geopolitical tensions, economic cycles, and potential terrorist threats.
           - Discuss strategies to mitigate these risks and ensure the sustainability of the tourism sector in egypt.
           - Add the sources and the domain name of the url if there are any urls.

        ### Industry Characteristics Analysis:
           - Create a table and evaluate the maturity, cyclicality, dependence, substitutes, profitability, and regulatory environment of the tourism industry.
            - Include industry analysis for each characteristic.
            - Use a risk rating (low, moderate, high) for each characteristic.
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

        Instructions: 
            - do not add conclutions
            - All should be in [language]
            - note that today's date is {date_string} anything beyond add it as forcasting
            
         """,
        "bing_query": ["صراعات البحر الاحمر ","صراعات الشرق الاوسط",'اخر اخبار الصراعات في العالم في ','غزه ',"اوكرانيا و روسيا"],# regions
        
    },
    "Competitive Analysis": {
        "prompt": f"""
        Generate the following sections in [language]: 

        ### Competitive Landscape Analysis in Egypt:
            - The Largest Egyptian Domestic Hotel Management Groups
              - Create a table for domestic hotel management groups (such as TMG, Travco, Pick Albatrous, Sunrise, Rixos, Orascom Development El Gouna ) with two columns: "Hotel Group" and "Presence". In the "Presence" column, provide details such as the number of hotels, geographic spread, notable properties, and ownership/management information.
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        
        Instructions: 
            - do not add conclutions
            - All should be in [language]
            - note that today's date is {date_string} anything beyond add it as forcasting
            
        """,
        "bing_query": [' اخبار الفنادق في مصر',
        # مجموعة طلعت مصطفى (TMG) - الضيافة
        "كم عدد الفنادق التي تملكها مجموعة طلعت مصطفى ",
        "كم عدد الغرف في مجموعة طلعت مصطفى للضيافة ",
        
        # مجموعة ترافكو (Travco) - حمد الشتي
        "كم عدد الفنادق التي تملكها مجموعة ترافكو ؟",
        "كم عدد الغرف في فنادق ترافكو ",
        
        # مجموعة بيك ألباتروس (Pickalbatros) - كامل أبو علي
        "كم عدد الفنادق التي تملكها مجموعة بيك ألباتروس ؟",
        "كم عدد الغرف في فنادق بيك ألباتروس ",
        
        # مجموعة صن رايز (Sunrise) - حسام الشاعر
        "كم عدد الفنادق التي تملكها مجموعة صن رايز ؟",
        "كم عدد الغرف في فنادق صن رايز ؟",
        
        # مجموعة ريكسوس (Rixos) - ناصر عبد اللطيف
        "كم عدد الفنادق التي تديرها مجموعة ريكسوس في مصر ؟",
        "كم عدد الغرف في فنادق ريكسوس في مصر ؟",
        
        # أوراسكوم للتنمية - الجونة (Sameh Sawiris)
        "كم عدد الفنادق التي تملكها أوراسكوم للتنمية في الجونة ؟",
        "كم عدد غرف فنادق أوراسكوم للتنمية الجونة ؟",
        
        # استفسارات مشتركة (إجمالي عدد الفنادق والغرف لكل مجموعة)
        "ما هي أكبر مجموعة فنادق في مصر ؟"
        ],
        
        },
        "Competitive Analysis 2": {
            "prompt": f"""
            Generate the following sections in [language]: 
                - The Most Famous International Hotel Groups in Egypt
                - Create a table for international hotel groups operating in Egypt (such as Accor, Radisson Hotel Group, Hilton, Hyatt, InterContinental Hotels Group (IHG), Marriott International) with two columns: "Hotel Group" and "Presence".  In the "Presence" column, provide details such as the number of hotels, geographic spread, notable properties, and ownership/management information.
                - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

            Instructions: 
                - do not add conclutions
                - note that today's date is {date_string} anything beyond add it as forcasting
                
            """,
            "bing_query": [' اخبار الفنادق في مصر'
                # ماريوت (Marriott) - Marriott Hotels in Cairo | Marriott Bonvoy
        "كم عدد الفنادق التي تديرها ماريوت في مصر ؟",
        "كم عدد الغرف في فنادق ماريوت في مصر ؟",
        
        # هيلتون (Hilton) - Hotels in Egypt - Find Hotels - Hilton
        "كم عدد الفنادق التي تديرها هيلتون في مصر ",
        "كم عدد الغرف في فنادق هيلتون في مصر ؟",
        
        # أكور (Accor) - Discover Our Hotels in Egypt | Book Online | Accor
        "كم عدد الفنادق التي تديرها أكور في مصر؟",
        "كم عدد الغرف في فنادق أكور في مصر",
        
        # مجموعة إنتركونتيننتال (IHG) - Top 7 Hotels in Egypt by IHG - August {current_year}
        "كم عدد الفنادق التي تديرها مجموعة إنتركونتيننتال (IHG) في مصر؟",
        "كم عدد الغرف في فنادق IHG في مصر؟",
        
        # استفسارات مشتركة (إجمالي عدد الفنادق والغرف لكل مجموعة),
        "ما هي فنادق العالميه في مصر؟"
    ]
    },
    "BM market research" :{
        "prompt": f"""Generate the following sections in [language]: 

            ### The Most important contents of our bank’s market research report on the tourism industry July {current_year}
            
            - Generate the following Table as it is even leave the Hyphens:
            | EBITDA Margin | NPM | ROE | ROA | Current Ratio | Fin. Lev. | Debt /Equity | OCF (EGP Mn) | FCF (EGP Mn) | FCF/OCF | Revenue (EGP Mn) | % 4 y-o-y | Net income (EGP Mn) | % 4 y-o-y | Total assets (EGP Mn) | Total liab. (EGP Mn) | - |
            | Orascom Development Egypt (Hotels Segment) | NA | 51% | 11% | NA | NA | 2 | 85% | NA | NA | NA | 699 | 22% | 354 | 11% | 6,684 | 2,849 |
            | TMG Holding (Tourism Segment) | NA | 84% | 2% | NA | NA | 1.1 | 16% | NA | NA | NA | 2,338 | 193% | 1,958 | 792% | 97,587 | 13,517 |
            | Mean Average | NA | 67% | 4% | NA | NA | 1.6 | 50% | NA | NA | NA | 1,518 | 107% | 1,156 | 390% | 52,136 | 8,183 |

            - generate the table columns as rows and rows as columns
            
            - Generate insights about the table

            - add the source [July {current_year} Market Research]

            Instructions: 
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": None,
            
            
                },
    
    "SWOT Analysis and Conclusion": {
        "prompt": f"""
        Generate the following sections in [language]: 

        ### SWOT Analysis:
           - Conduct a SWOT analysis table of the tourism sector, identifying strengths, weaknesses, opportunities, and threats.
                - Note: classify all internal parameters (inside egypt) as strengths and weakness, while  all external parameters are classified between opportunities and threats.

           - Provide specific examples for each point, focusing on market diversity, recovery from COVID-19, geopolitical challenges such as Gaza war, and investment opportunities.
           - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

        ### Conclusion:
           - Provide a comprehensive conclusion on industry trends (growing or not) for credit decision reviewers with showing some statistics and make it a bit longer.
       
        Instructions: 
           - All should be in [language]
           - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
    }
}
Electricity_prompts = {
    "Introduction" :{"prompt": f"""Generate in [language] the following sections: 
            
            # A comprehensive analysis of the Electricity industry

            ### Industry Overview:
                - Introduction to Discuss the importance of the electricity industry to Egypt's economy
                - highlight the role the electricity sector plays in powering key industries, supporting the country’s development goals,
                and providing energy access to both urban and rural communities. Additionally, mention the impact of electricity on job creation, infrastructure development, and Egypt's growth as a regional energy hub.
                -Subsection named Industry manufacturing stages discussing manufacturing stages of electricty.

            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
            instructions: 
                - keep the introduction consice 
                - never output you have no results
                - note that today's date is {date_string} anything beyond add it as forcasting
                    """,
        "bing_query": None,
        },
   
    "Electricity Statistics": {"prompt": f"""Generate in [language] the following sections: 
        ### Electricity Statistics in {current_year}
            write about:
                #### Egypt total eletricity Generated
                #### Egypt electricity consumption
                #### Egypt prices changes
                #### Egypt electricity segments
                #### Egypt electricity total users
                #### Egypt future electricity plans
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
            - note that today's date is {date_string} anything beyond add it as forcasting
            
        """,
                "bing_query": ["إجمالي الكهرباء المولدة في مصر","استهلاك مصر للكهرباء","اسعار الكهرباء في مصر","شرائح الكهرباء في مصر","مستخدمي الكهرباء في مصر","خطط مصر المستقبليه للكهرباء"],
                "use_pdf":True},
   
    "Market updates in Egypt" : 
        {"prompt": f"""Generate in [language] the following sections: 
        
        ### Market Updates and Latest News {int(current_year) - 1}-{current_year}

        #### Domestic Updates and Latest News
                - Provide the latest news and statistical data from reliable sources concerning the electricity industry, focusing on:
                    - Egypt: Highlight recent developments, trends, statistical insights, prices changes, projects, consumption, producion, electricity exports, electricity imports that impacting the electricity sector in egypt.
                        - Egypt Power & Renewables Projects Database, Egypt Top 10 Power
                    - Regional Overviews
                - Add news about the major players in the electricity sector in Egypt

                - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
                    """,
        "bing_query": ["اخبار الكهرباء في مصر","صادرات الكهرباء مصر","استيراد الكهرباء في مصر"],
        },

    "Market updates in Globally": {"prompt": f"""Generate in [language] the following sections: 

        #### Global Updates and Latest News
        - Global Trends: Highlight recent developments, trends, statistical insights, prices changes, projects, consumption, producion that impacting the electricity sector Globaly.
                    
                    
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
       
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting

        """,
            "bing_query": ["اخبار الكهرباء في العالم"],
            }, 

    "Competitor Analysis": {"prompt": f"""Generate in [language] the following sections: 
        ### Competitve Analysis
            - write about Competitive Landscape the electricity sector in egypt
            - Egyptian Electric Holding Company (EEHC)
            - Privately Owned And Financed Power Plants
       Instructions: 
            - no news needed to be added just information
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
                        """,
            "bing_query": None,
            },

    "Key players" : {
            "prompt": f"""Generate in [language] the following sections: 


            ## Companies that supports the Electricity sector in Egypt
            - add news about the key players in egypt

            ## Supplementary industries companies for Electricity sector in Egypt
                ### talk about Lighting tools companies in egypt like elsewedy electric , Alshater Cables, egydir, Egypt cable and 10th of Ramadan Company for Electrical Industries (GAD)
                    - News about Lighting tools companies in egypt
                ### talk about Lightening poles companies in egypt like Arab Organization for Industrialization, Egyptian German Lighting Poles, Al-Huda Solar Energy
                    - News about Lighting poles companies in egypt
                ### talk about Electricity towers companies in egypt like Egyptian Company for Electrical Transformers, General Cable Egypt (formerly BICC Cables), Ankom Egypt, JST Forlead Company, Omega Company for Consultations and Mechanical & Electrical Contracting, Al-Shaheed Company for Metal and Plastic Processing and MB Industrial  
                    - News about the electricity towers companies in egypt
                    
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
            Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query":["""اخبار
                            الشركة المصرية الصينية المشتركة للاستثمار
                            شركة دلتا للإنشاءات وإعادة الإعمار 
                            مجموعة الهندسة للطاقة الكهربائية 
                            شركة مدينة للطاقة الكيميائية الكهربائية 
                            نيو جيزة إترنال للخدمات الفاخرة والمدن 
                            شركة الطاقة العالمية 
                            أم الغريفات 
                            الشركة الوطنية لتكنولوجيا الكهرباء (كهرباء) 
                            شركة ميراج 
                            شركة كونسوكورا للوكالات التجارية والاستشارات الفنية 
                            شركة باور هاوس 
                            شركة الجونة للكهرباء 
                            شركة جينيرجيت للطاقة المتجددة 
                            شركة إماك للمرافق والخدمات""","اخبار شركه الكابلات الكهربائية المصرية",
                            "اخبار اكوا باور ايجيبت للطاقة",
                            "اخبار انيرجيا لكابلات الطاقة",
                            "اخبار شركه السويدى اليكتريك ش م م",
                            "اخبار انيرجيا للطاقة و التليكوم سليوشنز",
                            "اخبار سيمنس تكنولوجيز",
                            "اخبار شركه المشروعات الهندسيه للانشات ا",
                            "اخبار شركة البابطين للطاقة والاتصالات مصر",
                            "اخبار المصرية الاوروبية لتكنولوجيا الطاقة",
                            "اخبار المكتب العربي الاستشاري",
                            "اخبار اجيماك لمهمات الجهد العالى",
                            "اخبار اكوا باور كوم امبو للطاقة",
                            "اخبار الشركة الوطنية لتكنولوجيا الكهرباء",
                            "اخبار الهيئة العربية للتصنيع ",
                            "اخبار المصرية الالمانية لاعمدة الانارة",
                            "اخبار الهدى للطاقة الشمسية",
                            "اخبار شركه شنايدر",
                            "اخبار شركه فينوس الليد ",
                            "اخبار الشركة المصرية للمحولات الكهربائية",
                            "اخبار جنرال كابل مصر سابقا",
                            "اخبار شركة إنكم إيجيبت",
                            "اخبار شركة جست فوردليد",
                            "اخبار شركة أوشيبا للإستشارات والمقاولات الميكانيكية والكهربائية",
                            "اخبار شركة الشهيد لتشغيل المعادن والبلاستيك",
                            "اخبار شركة ام بي للصناعة",
                            "اخبار كابلات الشاطر",
                            "اخبار إيجيدير",
                            "اخبار كابلات مصر",
                            "اخبار شركة العاشر من رمضان للصناعات الكهربائية (جاد)"
                        ],
               },

                    
    "BM Market Research":{"prompt":  f"""Generate in [language] the following sections: 

                ### The Most important contents of our bank’s market research report on the electricity industry July 2024
                
                - Generate the following Table as it is even leave the Hyphens:
        | 1Q24 figures | EBITDA Margin | NPM | ROE | ROA | Current Ratio | Fin. Lev. | Debt /Equity | OCF (EGP Mn) | FCF (EGP Mn) | FCF/OCF | Revenue (EGP Mn) | % 4 y-o-y | Net income (EGP Mn) | % 4 y-o-y | Total assets (EGP Mn) | Total liab. (EGP Mn) |
        | Electro Cable Egypt Co SAE | 31% | 17% | 65% | 19% | 1.3 | 3.5 | 183% | -627 | -720 | -115% | 3,072 | 100% | 535 | 164% | 10,736 | 7,704 |
        | El Sewedy Electric Co SAE | 13% | 9% | 30% | 7% | 1.2 | 4.2 | 112% | -3,282 | -5,168 | -157% | 45,249 | 36% | 4,236 | 33% | 201,164 | 153,622 |
        | Average | 22% | 13% | 48% | 13% | 1.2 | 3.9 | 148% | -1,955 | -2,944 | -136% | 24,161 | 68% | 2,386 | 99% | 105,950 | 80,663 |
                - Generate insights about the table
                - generate the table columns as rows and rows as columns
                - add the source [July 2024 Market Research]

            Instructions: 
            - note that today's date is {date_string} anything beyond add it as forcasting
                """,
        "bing_query": None,
        },
    

    "Regulatory framework & Antidumping laws":{
        "prompt": f"""Generate in [language] the following sections: 
        ### Regulatory framework & Antidumping laws
            - Write the most important regulations in egypt regarding the electricity sector
        Instructions: 
            - do not add conclutions
            
            - note that today's date is {date_string} anything beyond add it as forcasting
                    """,
                
        "bing_query": ["اهم قوانين تخص الكهرباء في مصر"],
        },
    
    "SWOT Analysis and Conclution": {"prompt": f"""
        Generate in [language] the following sections: 

                ### SWOT Analysis:
                - Conduct a SWOT analysis table of the electricity sector, identifying strengths, weaknesses, opportunities, and threats.
                - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

                ### Conclusion:
                - Provide a comprehensive conclusion on industry trends (growing or not) for credit decision reviewers with showing some statistics and make it a bit longer.
            Instructions: 
            - note that today's date is {date_string} anything beyond add it as forcasting
            
                        """,
            "bing_query": None,
            },
}
steel_prompts = {
    "Introduction": {
        "prompt": f"""

        Generate in [language] the following sections with detailed analysis, relevant statistics, and recent developments:

        # A comprehensive analysis of the Steel industry

        ### The Introduction and Importance
        - **Discuss the Critical Role of the Steel Industry**: Elaborate on the steel industry’s pivotal role in driving economic and industrial growth, highlighting its capital-intensive nature and its influence on global market dynamics. Emphasize how steel serves as a fundamental material in construction, infrastructure, and various production processes, underscoring its integral role in industrialization.
        - **Contribution to Egypt’s Economy**: Provide an in-depth analysis of how the steel industry contributes to Egypt’s GDP, employment, and government revenue. Discuss the industry’s interconnections with key sectors such as construction, automotive manufacturing, and other related industries, and how these synergies drive economic growth.
        - **Global Impact of the Steel Industry**: Discuss the global significance of the steel industry, including its role in international trade, its influence on global supply chains, and its impact on the economies of major steel-producing nations.

        ### Global and Local Market Developments the current year
        - **Recent Developments in the Egyptian Steel Market**: Present in points the updates on the latest developments in the Egyptian steel market, incorporating mandatory relevant numbers, statistics, and dates. Don't repeat yourself.
        - **Global Steel Market Trends**: Analyze in points the recent developments in the global steel market, with a focus on major players like China and the United States. Include the most recent and significant news, supported by relevant statistics and dates, to provide a comprehensive overview of the current state of the global steel industry.
        - **Data-Driven Insights**: Use your industry knowledge and experience to provide insights and context to these developments.
        - **Sources**: cite the sources of the updates.
        **Note**: Do not include a conclusion in this analysis.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": [
        "اخبار صناعة الحديد في مصر",
        "global steel industry Chinaa USA",
        ],
        
    },
    "Market Updates": {
        "prompt": f"""
        Generate the following section: in [language]
        ### Market Updates in Egypt {int(current_year) - 1}-{current_year}
            - Create a table for market updates for Steel, including production volumes, exports, and steel consumption.
              - You can provide projected figures for current or upcoming years, noting that they are estimates. However, it's important to include actual numbers whenever possible. If the year is still ongoing, it's preferable to give data up to the most recent available date.
            - **Comment**: Discuss the possible reasons for the increase or decrease in numbers, considering economic conditions and relevant factors within the country. Ensure to be accurate.
            - Mention the source.

        
        Don't add any additional text or conclusion.
        - note that today's date is {date_string} anything beyond add it as forcasting
            """,
        "bing_query": ["حجم انتاج و صادرات واستهلاك حديد التسليح في مصر","اخبار صناعة الحديد في مصر"],
        
    },
    "Market Updates 2": {
        "prompt": f"""
        Generate the following section in [language]:
        ## Latest Steel Prices
          ### In Egypt
              - Create a table for the steel prices in Egypt of various companies in the market.
              - **Source**: Mention the source and the date of the updates below the table.
          ### World-wide
              - Provide latest USA steel prices.
              - **Source**: Mention the source and the date of the updates.

          - Compare prices in Egypt with global markets, considering the latest exchange rates. Highlight key differences and discuss possible reasons.

        - note that today's date is {date_string} anything beyond add it as forcasting
        Don't add any additional text or conclustion that wasn't requested.
        """,
        "bing_query": [ "اسعار الحديد في مصر اليوم","steel usa price", "سعر الصرف اليوم"],
        
    },
    "BM market research": {
        "prompt": f"""
        Generate the following tables in [language]:
        ### The market research department report at our bank on the industry for july {current_year}
        EBITDA Margin	NPM	ROE	ROA	Current Ratio	Fin. Lev.	Debt /Equity	OCF (EGP Mn)	FCF (EGP Mn)	FCF/OCF	Revenue (EGP Mn)	% 4 y-o-y	Net income (EGP Mn)	% 4 y-o-y	Total assets (EGP Mn)	Total liab. (EGP Mn)	
        Ezz Steel Co SAE (Quarter ending 31/12/2,023)	25%	3%		-1%	1	54	5964%	6,084	3,766	62%	39,672	70%	1,039	82%	113,371	112,074
        Misr National Steel SAE	7%	6%	45%	23%	2	1.9	22%	-194	-194	100%	1,013	154%	60	-52%	3,554	1,729
        Iron And Steel for Mines and Quarries	59%	46%	45%	34%	2.4	1.2	0.00%	83	46	55%	85	32%	39	39%	445	110
        Average	30%	18%	45%	19%	1.8	19.1	1995%	1,991	1,205	72%	13,590	85%	379	23%	39,123	37,971

            - Generate insights about the table
            - generate the table columns as rows and rows as columns
            - Extract all relevant details about Iron & Steel from the document, including any data, financial metrics, and key analysis. Ensure to include all tables (Ensure that the indicators to be in rows and companies in coloumns) and figures, and provide a comprehensive summary of the text, highlighting key financial performance and other relevant details.
            - Don't add conclusion.
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
    },
    "Competitve Analysis": {
        "prompt": f"""
        Generate the following section in [language] with adhering to the specified markdown ###:
        ### Key Players
            - Provide a table listing major companies, and their market shares.
            - Cite sources and date.
            According to data released by the Arab Iron and Steel Union:
            - Ezz Steel controls approximately 42% of the iron production in Egypt, thus leading the market.
            - The Suez Steel Company comes in second place with a market share of 19%.
            - Beshay Steel ranks third with a 15% share.
            - The Egyptian Steel Group, owned by businessman Ahmed Abou Hashima, holds the fourth position with a market share of 12%.
            - The remaining 12% is shared among other companies.
            - note that today's date is {date_string} anything beyond add it as forcasting

        Don't add conclusion.
        """,
        "bing_query": ['Egypt major steel companies and their market shares'],
        
    },
    "SWOT Analysis and Conclusion": {
        "prompt": f"""
        Generate the following sections in [language]:

        ### Create a detailed table for SWOT Analysis
            - Strengths (based on most recent updates)
            - Weaknesses
            - Opportunities (Don't include foreign investment opportunities)
            - Threats

        ### Anti-Dumping Laws and Regulatory Framework
            Write a summary about the anti-dumping laws and regulatory framework of the steel industry in Egypt, covering:

          1- Anti-Dumping Laws
              - Protection of local steel industry.
              - Law No. 161 of 1998.
              - Role of the Ministry of Trade and Industry.
              - Recent anti-dumping cases and the countries.
          2- Regulatory Framework:
              - Roles of Ministry of Trade and Industry, GOEIC, EOS.
              - Investment incentives under Law No. 95 of 1995.
              - Environmental compliance by EEAA.

        ### Conclusion:
              - Provide a comprehensive analysis of current industry trends, highlighting whether the industry is growing or declining. Include relevant statistics and data to support your conclusions, tailored specifically for credit decision reviewers.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": ['Egypt Steel industry SWOT'],
        
    }
}
food_Retail_prompts={

    "Introduction": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            # A comprehensive analysis of the Food and beverage retail industry named as : (نشاط تجارة الأغذية والمشروبات)

            ### The Introduction and Importance food and beverage industry
            - Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            - Food retail industry in Egypt.
            - History of food beverage retail industry in Egypt.
            - main food beverage retail products in Egypt.
            [Instructions]
            -Generate a paragraph of 6 lines and introduce the main points as instructed earlier.
            -include dates , statistics , history.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query": [
        "المواد الغذائيه الرسميه في الاقتصاد المصري",
        "تاريخ صناعه الاغذيه و المعلبات الغذائيه في مصر",
        "اهم المواد الغذائيه الموجوده في السوق المصري",
        "Retail/whole food and beverage traders in Egypt"

                ],
                
            },

    "Introduction 2": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### The Introduction and Importance of soft drinks 
            - soft Drinks retail industry in Egypt.
            - History of soft drinks retail industry in Egypt.
            - main soft drinks retail products in Egypt.
            [Instructions]:
            
            -Generate a paragraph of 6 lines and introduce the main points as instructed earlier.
            -include dates , statistics , history
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            - note that today's date is {date_string} anything beyond add it as forcasting

            """,
            "bing_query": [
        "history about soft drinks industry in Egypt",
        "Retail/whole soft drinks traders in Egypt"

                ],
                
            },
    "Introduction 3": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### Industry characteristics
            - Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            - Rice trade characteristics and production stages and its derivatives.
            - Pasta industry characteristics and production stages and its derivatives.
            - Tea industry characteristics and production stages and its derivatives.
            - Tuna/Renga/feseekh characteristics and production stages and its derivatives.
            - Coffee industry characteristics and production stages and its derivatives.
            - Milk and cheese industry characteristics and production stages and its derivatives.
            - Soft drinks industry characteristics and production stages and its derivatives.
            [Instructions]:
            -Don't add introduction or conclusion.
            -Generate a paragraph of 6 lines per each industry mentioned above.
            -Each Industry should be detailed as much as possible
            -You can list the characteristics of each industry in a table.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            

            """,
            "bing_query":["characteritics of food and beverage retail/whole sale trade in Egypt"
                        
                        
                        ],
            
        },

    "Market updates in Egypt": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### Market updates in Egypt {current_year} investments:
            - Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            - Investments in Egypt in Retail/wholesale trade {current_year}.
            - New Projects in Egypt related to Retail/wholesale such as new hyper markets
            
            [Instructions]:
            -Don't add introduction or conclusion.
            -Generate a paragraph describing food and beverage retail/wholesale.
            -Each Industry should be detailed as much as possible
            -You can list the characteristics of each industry in a table.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            - note that today's date is {date_string} anything beyond add it as forcasting

            """,
            "bing_query":["current food and beverage wholesale/retail industry in Egypt",
                        
                        "Investment in food and beverage wholesale/Retail sector in Egypt",
                        "Comparison between wholesale/Retail industry investment in Egypt {int(current_year) - 1} vs",
                        "Hyper markets in Egypt openings/offerings in",
                        "Name of New hypermarkets in Egypt"],
            
        },

    "Market updates in Egypt 2": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### Market updates in Egypt {current_year} Main products in Food in Egypt {current_year} :
            - Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            - Rice Industry Production , Consumption , Imports and Exports.
            - Pasta Industry Production , Consumption , Imports and Exports.
            - Tuna/Renga/Feseekh Industry Production , Consumption , Imports and Exports.
            - milk Industry Production , Consumption , Imports and Exports.
            - cheese Industry Production , Consumption , Imports and Exports.
            - butter Industry Production , Consumption , Imports and Exports.
            - tea Industry Production , Consumption , Imports and Exports.
            - coffee Industry Production , Consumption , Imports and Exports.
            - Soft drinks Industry Production , Consumption , Imports and Exports.
            
            [Instructions]:
            -Don't add introduction or conclusion.
            -Generate a paragraph describing each point in the mentioned above food and beverage retail/wholesale.
            -Each Industry should be detailed as much as possible.
            -Each industry must have Production , Consumption , Imports and Exports subsection.
            -Include top products per each industry in the Egyptian market and link them to each relevant industry.
                --Products in Rice/pasta/oil industry.
                --Products in canned food.
                --Products in soft drinks.
                --Products in Juices.
                --Products in tea and coffeee.
                --Products in cheese and milk.
                --Products in butter/fat.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            
            
            """,
            "bing_query":[
        "Rice consumption/production in Egypt",
        "Rice imports/exports to/from Egypt",
        "Pasta consumption/production in Egypt",
        "Pasta consumption/production in Egypt",
        "Tuna/Renga/feseekh consumption/production in Egypt",
        "Tuna/Renga/feseekh consumption/production in Egypt",
        "Milk consumption/production in Egypt",
        "Milk imports/exports to/from Egypt",
        "cheese consumption/production in Egypt",
        "cheese imports/exports to/from Egypt",
        "butter consumption/production in Egypt",
        "butter imports/exports to/from Egypt",
        "tea consumption/production in Egypt",
        "tea imports/exports to/from Egypt",
        "coffee consumption/production in Egypt",	
        "coffee imports/exports to/from Egypt",
        "Soft drinks such as pepsi cocacola sevenup in Egypt",
        "Boycott Effect on Softdrinks products in Egypt",
        "top 5 Market Prodcuts statistics for canned food (such as tuna sunshine,halawany.....etc) in Egypt",
        "top 5 Market Products statistics for Drinks such as (pepsi , cocacola , spirospathis, v7...etc) in Egypt",
        "top 5 Market Products statistics for Tea-coffee ( abo ouf , shay el 3arosa , Ahmed Tea , lipton....etc ) in Egypt",
        "top 5 Market Products statistics for butter/fat industry in Egypt",
        "top 5 market Products statistics for soft drinks such as Juhayna , best , faragallah... in Egypt",
        "top 5 Market Products statistics for Cheese/milk industry industry in Egypt such as obbour land , domety , juhayna ",

        "top 5 Market Products statistics for Rice/pasta/oil  industry in Egypt such as regina, el doha rice, abad el shams oil ",],
        },


    "Market updates in Globally ": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            ### Market updates in Worldwide {current_year}:
            - Rice Industry.
            - Pasta Industry.
            - milk Industry.
            - cheese Industry.
            - butter Industry.
            - tea Industry.
            - coffee Industry.
            - Soft drinks Industry.
            
        
            
            [Instructions]:
            -Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            -Don't add introduction or conclusion.
            -Each Industry should be detailed as much as possible.
            -You can list the characteristics of each industry in a table with a descriptive title to the table.
            -Include citations,numbers and statistics for each requirement.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":["top 5 countries for Rice industry/agriculture",
                        
                        "top 5 countries statistics for Pasta industry/agriculture",
                        "top 5 countries statistics for Milk industry/agriculture",
                        "top 5 countries statistics for Cheese industry/agriculture",
                        "top 5 countries statistics for butter industry/agriculture",
                        "top 5 countries statistics for tea industry/agriculture",
                        "top 5 countries statistics for coffee industry/agriculture",
                        "top 5 countries statistics for softdrinks industry",
                        "top 5 countries statistics for tuna/renga/feseekh industry",
                        
                        ],
            
        },

        "Competitve Analysis": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### Main market players retail and whole sale trade in Egypt :
            - Retail/Whole ( Super market Seoudi, carrefour , hyperone , breadfast, kazion ,(خير زمان- مترو ماركت - فريش فود)المنصور جروب),BIM,جورمية ,الفا ماركت.
            
            [Instructions]:
            -Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            -Don't add introduction or conclusion.
            -It should be in [language].
            -Include market players as much as possible.
            -Statistics must be introduced like number of branches in Egypt,Geographical areas per city , money and so on.
            -Each market player must be in numbers no generic descriptions.
            -Each market player must be presented separately.
            -Specifiy the Local and Global suppliers to each market player presented with their names.
            -Include citations.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            -List all the information in table.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":[
                        "Seoudi Hyper markets chains their sepcific locations in Egypt",
                        "Number of Seoudi Hyper markets branches their sepcific locations in Egypt",
                        "Seoudi Hyper markets and their main suppliers in Egypt",
                        "Carrefour Hyper markets chains their sepcific locations in Egypt",
                        "Number of Carrefour Hyper markets branches their sepcific locations in Egypt",
                        "Carrefour Hyper markets and their main suppliers in Egypt",
                        "hyperone Hyper markets chains and their sepcific locations in Egypt",
                        "Number of hyperone Hyper markets branches and their sepcific locations in Egypt",
                        "hyperone Hyper markets and their main suppliers in Egypt",
                        "breadfast Hyper markets chainsand their sepcific locations in Egypt",
                        "Number of breadfast Hyper markets branches their sepcific locations in Egypt",
                        "breadfast Hyper markets and their main suppliers in Egypt",
                        "kazion Hyper markets chains and their sepcific locations in Egypt",
                        "Number of kazion Hyper markets branches and their sepcific locations in Egypt",
                        "kazion Hyper markets and their main suppliers in Egypt",
                        "(خير زمان- مترو ماركت - فريش فود)المنصور جروب) Hyper markets chains and their sepcific locations in Egypt",
                        "Number of (خير زمان- مترو ماركت - فريش فود)المنصور جروب) Hyper markets branches their sepcific locations in Egypt",
                        "BIM,جورمية ,الفا ماركت Hyper markets chains in Egypt their sepcific locations",
                        "Number of BIM,جورمية ,الفا ماركت. Hyper markets branches in Egypt their sepcific locations",
                        "main local and global suppliers for Hyperone,Carrefour,Seuodi,Breadfast,Kazion,Freshfood,metro market in Egypt"

                        ""

                        
                        

                        
                        ],
            
        },
        

    "SWOT Analysis": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### SWOT analysis for Food and beverage industry in Egypt in [language] language
            - Retail/Wholesale food and beverage Strenghths,Weakness,Oppourtuinties , Threats.
            
            [Instructions]:
            -Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            -Don't add introduction or conclusion.
            -Generation language is in [language] language.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            -For the beverage its specified to be soft drinks and juices no alcohols.
            -Don't include any alcohols.
            -Make it in a table 
            - note that today's date is {date_string} anything beyond add it as forcasting

            

            """,
            "bing_query":[ "Strengths for food Retail/Whole sale in Egypt", 
                        "weakness for food Retail/Whole sale in Egypt",
                            "oppourtuinties for food Retail/Whole sale in Egypt",
                            "threats for food Retail/Whole sale in Egypt",
                        

                    ],
            
        },


        "Market forecasts": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### Market forecasts
            - food Retail.
            - canned food.
            - Soft Drinks.
            - Tea-coffee.
            - butter.
            
            
            
            
            [Instructions]:
            -Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            -Don't add introduction or conclusion.
            -We are in septmeber {current_year} , so your forecasts must be after this date.
            -Mention the reasons for this forecasts.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":[ "forecasts for food Retail in Egypt",
                        "forecasts, weakness, oppourtuinties , threats for canned food in Egypt",
                        "forecasts, weakness, oppourtuinties , threats for soft drinks in Egypt",
                        "forecasts, weakness, oppourtuinties , threats for Tea-Coffee in Egypt",
                        "forecasts, weakness, oppourtuinties , threats for butter in Egypt",

                    ],
            
        },

    "Conclusion": {
            "prompt": f"""

            Generate in [language] the following section and follow up the [Instructions] strictly:

            

            ### Conclusion
            - food Retail.
            - canned food.
            - Soft Drinks.
            - Tea-coffee.
            - butter.
            
            
            
            
            [Instructions]:
            -write a full detailed conclusion in [language] language about all the information we have passed through.
            -The conclusion is one paragraph and highlight it on Retail/wholesale food beverage with statistics without digging into too much details.
            -include all details in summmarization.
            -Food and beverage industry should be named as (نشاط تجارة الأغذية والمشروبات) if generated.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":None,
            
        },
}
sugar_prompts = {
    "Introduction": {"prompt": f"""Generate the following sections in [language]:
            
            # A comprehensive analysis of the Sugar industry

            ### Industry Overview:
                - Introduction to Discuss the importance of the Sugar industry to Egypt's economy
                - highlight the role the Sugar sector plays in powering key industries, supporting the country’s development goals,
            ### About Sugar industry in egypt
                - write about the how is sugar created from growing sugarcane and beets till it be sugar
                - write in details the growing and manufacture stages of Sugar in egypt
                - write about why beet is used to create sugar like sugarcane
            instructions: 
                
                - keep the introduction consice 
                - never output you have no results
                - do not add conclutions
                - note that today's date is {date_string} anything beyond add it as forcasting
                    """,
        "bing_query": ['صناعه السكر في مصر','صناعه السكر في مصر wikipedia'],
        "use_pdf": True},
     
    "Industry Statstics in Egypt": {"prompt": f"""Generate the following sections in [language]:
        
        ### Sugar Industry Statstics in {current_year}
                - Table For
                    ### Sugar Sales Egypt {int(current_year) - 3}- {int(current_year) + 4}
                        - Sugar and sugar products, sales, EGPmn, % growth yo-y
                        - Sugar and sugar products, sales, EGPmn

                    - Generate insights about the table 
        Instructions:
            
                
            - if there are no information provided for an item in the section do not generate it
            - numbers in the tables make them real numbers do not add numbers after decimal except for percentage numbers
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query":None,
            "use_pdf": True},

    "Industry Statstics in Egypt 2": {"prompt": f"""Generate the following sections in [language]:

                - Table For

                    #### Sugar Production And Consumption Egypt {int(current_year) - 5} - {int(current_year) + 4}
                        - Sugar production, '000 tonnes
                        - Sugar production, % y-o-y
                        - Sugar consumption, '000 tonnes
                        - Sugar consumption, % y-o-y
                        - Sugar Consumption, kg per capita
                        - Sugar production balance, '000 tonnese
                        - Sugar self sufficiency, %
                - Generate insights about the table 
        Instructions:
                
            
            - if there are no information provided for an item in the section do not generate it
            - numbers in the tables make them real numbers do not add numbers after decimal except for percentage numbers
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
            "use_pdf": True},

    "Industry Statstics in Egypt 3": {"prompt": f"""Generate the following sections in [language]:

                    ### The amount of Egypt’s production of sugar from cane sugar
                    ### The amount of Egypt’s production of sugar from beet
                            Integrated Industries targets a 50% increase in beet sugar production
                            Salah Omar: Payment of one billion pounds, the value of 450 thousand tons received in {current_year}
                            Integrated Industries targets a 50% increase in beet sugar production from one of the sugar factories
                            The Sugar and Integrated Industries Company aims to produce about 110,000 tons of sugar from beets during the new {int(current_year) + 1} season, an increase of 50% over the {current_year} season, which witnessed the production of 56,000 tons, according to Engineer Salah Omar, the technical managing director of the company.
                            Omar added in statements to Hapi newspaper that the company aims to receive 700 to 800 thousand tons of beets from farmers in the governorates of Beni Suef, Minya, Assiut, Sohag, and Qena, for the benefit of the Abu Qurqas factory, during the new supply season.
                            He pointed out that the company received during the {current_year} beet harvest season a quantity amounting to 450 thousand tons, and about one billion pounds were paid for the value of the quantities supplied.
                            Omar explained that these quantities did not achieve the target estimated at about 600 thousand tons, out of the total cultivated area, which amounted to 22 thousand acres.
                            He continued that the beet crop that the company obtains through the Abu Qurqas factory, 90% of which is contract cultivation and the rest is agreed upon through the farmers, noting that there are many advantages that are offered and vary from one season to another, according to the competition that takes place between different companies, whether governmental or sector. private.   
                            The Technical Managing Director of the Sugar Company indicated that the quantities of beets grown in Upper Egypt are directed to the Abu Qurqas Factory “government” and the Canal Sugar Company Factory “private sector,” noting that the Abu Qurqas Factory received about 430 thousand tons of beets during the {current_year} season, It is less than the target by about 150 thousand tons, as a result of climate change.
                            It is noteworthy that Egypt produces about 2.7 million sugar, of which the sugar company’s share is 700 thousand tons and the rest is from beet companies. The consumption rate is about 3 million tons of sugar, and 300 thousand tons are imported to fill the gap between production and consumption.                    
                    ### Amount Egypt's imports of sugar
                            A report by the US Department of Agriculture expects Egypt's sugar production to decline during the new {current_year}-{int(current_year) + 1} season to record 2.86 million tons, down 110.2 thousand tons compared to the ministry's previous expectations due to the decline in sugarcane production.
                            A recent report by the US Department of Agriculture said that last year witnessed a decline in global sugar production, as sugar prices rose and the pound recorded a new decline, which limited the possibility of Egypt importing sugar.
                            During the past year, Egypt suffered a crisis of a sharp rise in free sugar prices, with the price of a kilo reaching 50 pounds ($1.02), before it declined again and became available in the markets at lower prices.
                            Inflation in Egypt hit record levels last year, reaching 38 percent in September, before declining again.

                            Although Egypt has expanded its sugar beet and cane cultivation, its production is not enough for its consumption and it is imported from abroad.

                            Sugar consumption in Egypt increases
                            The report expects Egypt's sugar consumption to increase during the new season {current_year}/{int(current_year) + 1} to reach 4.1 million tons compared to 3.9 million tons in the previous season, due to population growth and increased demand for sugar.
                            Egypt is one of the highest sugar consuming countries in the world. According to the Organization for Economic Co-operation and Development, the individual in Egypt consumes 51.4 kilograms of sugar annually, which is nearly double the global average consumption per person.
                            Sugar is sold in Egypt at the free price and the subsidized price, and those with a support card can obtain subsidized sugar.
                            The report expects Egypt's imports in the new season {current_year}-{int(current_year) + 1} to reach 1.65 million tons, an increase of 551 thousand tons over the previous season {int(current_year) - 1}-{current_year}, to cover the shortage in local production and the increase in demand.
                            Egypt primarily imports raw sugar cane from Brazil and raw sugar beets from the European Union.
                            Market fluctuations in the fiscal year {int(current_year) - 1}-{current_year} led the General Authority for Supply Commodities to purchase raw and refined sugar cane from Saudi Arabia.
                            Egypt's sugar stock is estimated to end the new season {current_year}-{int(current_year) + 1} at nearly 1.1 million tons, an increase of 1.03 million tons over the stock estimates in the {int(current_year) - 1}-{current_year} season, with Egypt establishing a strategic reserve to protect against future shocks.
                            Last March, the Egyptian Cabinet announced that Egypt intends to import one million tons of white sugar during the current the current year to confront rising prices and scarce supply.
                            The Ministry of Supply and Internal Trade, represented by the General Authority for Supply Commodities, contracted last April to purchase 200,000 tons of imported raw sugar, bringing the total contracted at the time to 450,000 tons of raw sugar.              
                    ### Amount Egypt's exports of sugar
                        - there are no sugar exports from egypt due to political restrictions 
               - Generate insights about the table 
                Write insights regarding this context and statstics
            
        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

        Instructions:
            - Add justfication for every insight
            
            - note that today's date is {date_string} anything beyond add it as forcasting            
            - if there are no information provided for an item in the section do not generate it
            - numbers in the tables make them real numbers do not add numbers after decimal except for percentage numbers
        """,
            "bing_query": [
                "إنتاج مصر من قصب السكر",
                "إنتاج مصر من بنجر السكر",
                "استيراد السكر في مصر",
                "القيود السياسية على تصدير السكر في مصر",
                ],
                "use_pdf": True},

    "Market updates in Egypt": {"prompt": f"""Generate the following sections in [language]: 
        
        ### Market Updates and Latest News {int(current_year) - 1}-{current_year}

        #### Domestic Updates and Latest News
                - Provide the latest news and statistical data from reliable sources concerning the Sugar industry, focusing on:
                    - Egypt: Highlight recent developments, trends, statistical insights, prices changes, projects, consumption, producion, Sugar exports, Sugar imports that impacting the Sugar sector in egypt.
                        -  Egypt's Sugar Beet Expansion Drives Output Growth

                    - Write about beet rhizomania in egypt and how egypt is solving this issue

                    - News related to sugar industry
                - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            - if there are no information provided for an item in the section do not generate it
     
         """,
        "bing_query": ['اخبار صناعه السكر في مصر', "اخبار واردات مصر من سكر القصب والبنجر","اخبار صادرات مصر من سكر القصب والبنجر","اخبار محصول البنجر و القصب في مصر","مصر اخبار عن مرض البنجر ريزومانيا"],
        "use_pdf": True},
    
    "Market updates in Globally": {"prompt": f"""Generate the following sections in [language]:

        #### Global Updates and Latest News
        - Write about the countries that exports sugar to egypt    
            - Brazil: Brazil is one of the largest exporters of sugar to Egypt, playing a major role in meeting the needs of the Egyptian market.

            - India: India also contributes to sugar exports to Egypt, despite the challenges it faces in local production.

            - European Union: The European Union contributes to sugar exports to Egypt, benefiting from high production in some member states

        - Global Trends: Highlight recent developments, trends, statistical insights, prices changes, projects, consumption, producion that impacting the sugar sector Globaly.
                    
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it

        """,
            "bing_query": ["sugar industry global news",'من اين تستورد مصر السكر',"اكبر الدول المصدره للسكر لمصر"],
            }, 

    "Competitve Analysis": {"prompt": f"""Generate the following sections in [language]:
        ### Competitve Analysis sugar industry in egypt
            - write about Competitive Landscape the sugar industry in egypt
                - Governmental companies affiliated with the Holding Company for Food Industries, which was previously under the control of the Ministry of Investment, and the Authority currently, which is the Sugar and Integrated Industries Company, which is responsible for providing sugar for ration cards, and the Delta, Dakahlia, Fayoum and Nubaria Company.
                - Privately Owned like Nile sugar and savola
        ### Key Players News in the Sugar industry in Egypt
            - write about Key players news and updates like the Nile sugar, savola, and the Sugar and Integrated Industries Company and its companies
        do not add conclutions
            - News should be in {current_year}

        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it
         """,
        "bing_query": ["اخبار الفيوم لسكر","اخبار الدقهلية لسكر","اخبار شركة الدلتا لسكر","اخبار شركة السكر والصناعات التكاملية","اخبار شركه صافولا سكر","اخبار شركه النيل للسكر",'اخبار شركة أبو قرقاص'],
        "use_pdf": True},
    
    "BM Market Research": {"prompt": f"""Generate the following sections in [language]:
        ### The most important points mentioned in our bank’s market management report on the industry, July {current_year}
        - write the following analysis as it is
            1. Sugar Price Index (FAO)
                - In {int(current_year) - 1}, the Sugar Price Index increased by 27%.
                - In {current_year} (YTD), the Sugar Price Index decreased by 10%.
                
            2. Delta Sugar Company (Financial Performance and Position)
                    - EBITDA Margin: 24.2%
                    - Net Profit Margin (NPM): 29.3%
                    - Return on Equity (ROE): 72.0%
                    - Return on Assets (ROA): 30.9%
                    - Current Ratio: 1.40
                    - Debt to Equity Ratio: 9.2%
                    - Operating Cash Flow (OCF): 298.9 EGP mn
                    - Free Cash Flow (FCF): 289.2 EGP mn
                    - Revenue: 740.5 EGP mn, with a year-over-year growth of 4% 
                    - Net Income: 216.8 EGP mn, with a year-over-year growth of 33.06%
                    - Total Assets: 5,741.9 EGP mn
                    - Total Liabilities: 3,416.2 EGP mn
                
                3. Price Changes (April - June)
                    - The price of refined sugar dropped by 14% during April to June, due to improved supply conditions.
        
        - write insights about the previous analysis
        - note that today's date is {date_string} anything beyond add it as forcasting
        
         """,
        "bing_query": None,
        "use_pdf": True},

    "Regulatory framework & Antidumping laws": {"prompt": f"""Generate the following sections in [language]: 

        ### Regulatory framework & Antidumping laws
                - Write the most important regulations in egypt regarding the sugar industry
                
        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions:
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
                        """,
                
        "bing_query": ["اهم قوانين تخص السكر في مصر"],
        },
    
    "SWOT Analysis and Conclusion": {"prompt": f"""Generate the following sections in [language]:

                ### SWOT Analysis on sugar industry:
                - Create a SWOT analysis table of the Sugar industry, identifying strengths, weaknesses, opportunities, and threats.
                    the items in strengths and weaknesses should be internal parameters in egypt and items in opportunities and threats should be external parameters
                - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

                ### Conclusion:
                - Provide a comprehensive conclusion on industry trends (growing or not) for credit decision reviewers with showing some statistics and make it a bit longer.
                - Any predictions should till {int(current_year) + 1}

                Instructions: 
                    - the table items shouldn't be empty should if empty write hyphen -
                    - note that today's date is {date_string} anything beyond add it as forcasting
                    
                        """,
            "bing_query": ['swot analysis للسكر في مصر',"sugar swot analysis in"],
            },
}
grain_prompts = {
    "Introduction": {
        "prompt": f"""
        Generate the following sections in [language]:
        # A comprehensive analysis of the Grain industry

        ### Introduction and Importance

            **overview**: Provide an overview of the significance of the grain milling and feed manufacturing industries to the Egyptian economy, highlighting their role in food security and agricultural sustainability.

            **grain milling industry**:

              - Discuss the key activities of grain milling, including the processing of wheat, corn, and other grains.
              - Detail the types of grains used, focusing on wheat and corn, their production volumes, and their contribution to the food industry.
              - Explain the importance of wheat and corn to Egypt, including domestic production figures and the quantities imported, primarily from countries like Russia and Ukraine.
              - Highlight the role of the Egyptian government in supporting grain milling through pricing and subsidies.

            **corn and wheat production**:

              - Provide specific data on Egypt's wheat and corn production, including cultivated areas, average yields, and seasonal growing and harvesting periods.
              - Discuss the gap between local production and demand, and explain why Egypt remains a large importer of these grains.
              - Include current import prices and their effect on the market.

            **feed manufacturing industry**:

              - Detail the importance of the feed manufacturing sector to livestock, poultry, and aquaculture industries.
              - Discuss the types of feeds produced, including the difference between manufactured and integrated feeds.
              - Explain the raw materials used in feed production, such as corn, soybean meal, and other protein sources, and their relative proportions in the mix.
              - Provide information on the production process, including grinding, mixing, and pelletizing, and how these methods affect feed quality.

            **types of grains and feeds**:

              - Outline the different types of grains (wheat, corn, barley, etc.) used in feed and food processing.
              - Explain the different types of feed (manufactured and integrated) and the specific needs they address in animal nutrition.

            **economic impact**:

              - Discuss the economic importance of both industries to Egypt, focusing on their role in reducing import dependency, supporting rural livelihoods, and stabilizing food prices.
              - Highlight the challenges faced by these industries, including the gap between local production and demand, and the impact of global price fluctuations.

            - Make sure the response is structured with clear heading and provides a detailed, fact-based analysis of each section.
            - note that today's date is {date_string} anything beyond add it as forcasting
                  """,
        "bing_query": None,
        
    },
    "Market Updates in Egypt": {
        "prompt": f"""
        Generate the following sections in [language]:
        ### Latest updates
            1. **grains**
              - **Egypt**
                - Include wheat, corn imports
                - Include recent price changes and any relevant government policies regarding wheat,corn, and rice imports.
                - Mention any initiatives to diversify import sources or impacts from geopolitical events.

              - **Worldwide**
                - Discuss the effects of geopolitical events (like the Ukraine war) on global wheat production and prices.
                - Provide information on current global price trends and forecasts.

            2. **Feed**
              - **Egypt**
                - Report on the current prices of animal feed with its different types and soybean meal.
                - Highlight any significant changes in import sources or domestic production.

              - **Worldwide**
                - Address any global supply challenges for feed and the implications for prices.
                - Discuss trends in demand for animal feed, especially in emerging markets.

            **citations**: Include credible sources for all data and statistics.
            - All data should be the last updated {current_year}
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            """,
        "bing_query": ["wheat corn barley rice prices Egypt","Egypt wheat corn barley rice import sources production","global wheat production forecast","animal feed prices Egypt","soybean meal import prices Egypt","global feed market trends"],
        
    },
    "Market Updates in Egypt 2": {
        "prompt": f"""
        Generate the following sections in [language]:
        ### Market Updates
            - Provide {current_year} data for corn and wheat, including production, consumption, self-sufficiency ratio (calculated by production/consumption), and imports (calculated by consumption - production) in a single line for each crop.
        
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
    },
    "Market Statistics": {
        "prompt": f"""
        Generate the following sections in [language]:
            - Provide {current_year} data for rice, including production, consumption, self-sufficiency ratio (calculated by production/consumption), and imports (calculated by consumption - production) in a single line.
            - Don't add any additional text
            - **sources**: cite sources.
        
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
    },

    "Competitive Analysis": {
        "prompt": f"""
        Generate the following section in [language]:
        ### Competitive Landscape
            #### Companies in Grain Sector
                 - Create a table with the following companies and their descriptions:

                   - Cairo 3A
                     Description: A prominent Egyptian company specializing in agricultural products, focusing on grains and oils.

                   - Cargill
                     Description: A global leader in agribusiness involved in grain trading, food production, and agricultural services.

                   - EL-Nour Trading
                     Description: A trading firm in Egypt specializing in agricultural commodities, including grains.

                   - Louis Dreyfus
                     Description: A multinational corporation engaged in the trading, processing, and logistics of food products.

                   - Oils & Grains
                     Description: A key player in sourcing and distributing oils and grains for local and international markets.

                 - Also, provide the latest updates for Cairo 3A, Cargill, and Louis Dreyfus dynamically.
                 - Cite sources.

            #### Key Players in the Poultry Feed Market in Egypt
                 - List in a table the key players in the poultry market in Egypt, including their names and a brief description of their operations.

            #### Mills Companies:
                 - Create two separate tables based on the following data:
                   - Mills Companies
                      Upper Egypt Mills Company
                      Middle Egypt Mills Company
                      South Cairo Mills Company
                      North Cairo Mills Company
                      West and Middle Delta Mills Company
                      Alexandria Mills and Bakeries Company
                      East Delta Mills
                   - Private Sector Companies Producing Fine Flour
                      Egyptian Millers Company
                      Al-Khattab Mills Company
                      Dahab Mills Company
                 - Also, provide the latest updates for Egyptian Mills Companies dynamically.
                 - Cite sources.
        - note that today's date is {date_string} anything beyond add it as forcasting
        
        """,
        "bing_query": ["Cairo 3A","Cargill","Louis Dreyfus","أكبر شركات الدواجن في مصر","Egypt Mills Companies updates"],
        "use_pdf": False,
    },
    "BM market research": {
        "prompt": f"""
        Generate the following sections in [language]:
        ### The market research department report of july at our bank on the industry

        ,Financial Performance,Financial Position,Cash Flow Position,Key P&L Figures,Key B/S Figures
        1Q24 figures,EBITDA Margin,NPM,ROE,ROA,Current Ratio,Fin. Lev.,Debt /Equity,OCF (EGP Mn),FCF (EGP Mn),FCF/OCF,Revenue (EGP Mn),% 4 y-o-y,Net income (EGP Mn),% 4 y-o-y,Total assets (EGP Mn),Total liab. (EGP Mn)
        Ismailia Misr Poultry Co,57.3%,35.1%,6.8%,2.5%,0.13,2.74,14.6%,-0.81,-0.82,1.01,6.25,-90%,2.20,-109.26%,319.6,218.5
        Mansoura Poultry Co,18.2%,17.1%,75.9%,46.4%,1.44,1.64,24.4%,16.47,12.23,0.74,158.8,70%,27.10,16.27%,343.8,142.0
        Cairo Poultry Company,26.2%,16.2%,42.1%,21.3%,1.75,1.97,14.2%,597.0,382,0.64,"3,432.9",23%,555.4,0.00%,"6,094.0","2,763.4"
        Poultry - Average,33.9%,22.8%,41.6%,23.4%,1.10,2.12,17.7%,204.2,131,0.80,"1,199.3",1%,194.9,-30.99%,"2,252.5","1,041.3"
        Atlas for Inv. & Food Industries,-20%,-87%,-5%,-3%,1.4,1.7,1.6%,7.07,6.53,0.92,3.11,-56%,-2.71,-247.22%,133,56
        Arab Moltaka Investments Company,11%,12%,19%,4%,1.0,5.1,355.8%,-29.12,-33.08,1.14,367.4,37%,45.14,169.16%,"6,113","4,914"
        "El Nasr for Manuf. Agri. Crops SAE (Quarter end. 31/12/2,023)",,,-9%,,0.1,2.2,0.9%,-0.17,-0.17,1.00,,,-0.57,32%,65,36
        Int. Co for Agricultural Corps,14%,17%,71%,49%,1.9,1.5,6.2%,-161.1,-171.2,1.06,469.9,-40%,78.44,-52.36%,"1,623",437
        Misc. - Average,2%,-19%,19%,16%,1.1,2.6,91%,-46,-49,103%,280,-20%,30,-25%,"1,984","1,361"

            - generate the table columns as rows and rows as columns
            - Extract all the data and table related to Agriculture & Forestry from the report. Present the companies as columns and the financial indicators as rows in the table for better clarity.
            - Don't add conclusion.
            - note that today's date is {date_string} anything beyond add it as forcasting
        
        """,
        "bing_query":None,
        "use_pdf":  False,
    },
    "SWOT Analysis and conclution": {
        "prompt": f"""
        Generate in [language] the following sections:
        ### SWOT Analysis
            - Generate a detailed SWOT analysis seperately for both the grain and feed industry in Egypt. Present and format it as a table. The analysis should include specific strengths, weaknesses, opportunities, and threats, avoiding generic statements. Provide a clear and structured layout.
        ### Conclusion
            - Provide a comprehensive analysis for both the grains and feed industry trends, highlighting whether each industry is growing or declining. Include relevant statistics and data to support your conclusions, tailored specifically for credit decision reviewers.
            - note that today's date is {date_string} anything beyond add it as forcasting
        
        """,
        "bing_query": None,
        
    }
}
cotton_prompts = {
    "Introduction": {
            "prompt": f"""
        Generate the following sections in [language]:

        # A comprehensive analysis of the Cotton industry

        ### Industry Overview:
        - Discuss the significance of the cotton industry to the economy, including its role in economic growth, job creation, and infrastructure development.

        - Highlight the diversity and importance of the cotton industry, considering various sub-sectors like agricultural production, textile manufacturing, and retail, as well as urbanization trends.

        ### Cotton Industry Market Statistics {int(current_year) - 14} - {current_year}:
        - Provide a detailed analytical statement on the growth of cotton industry investments, total cotton production (in tons), and total cotton product transactions

        - Include a table with the following columns:
            - Year
            - Total Investments (in billion dollars)
            - Total Cotton Production (in tons)
            - Total Cotton Product Transactions (in units)
        - Add the accurate source for the data presented in the analysis.

        ### Cotton Industry Performance {int(current_year) - 2} - {current_year}:
        - Discuss key growth drivers, including rising demand for cotton products, foreign direct investments (FDI) in cotton manufacturing, and major cotton production initiatives by prominent producers. Be specific.

        - Highlight key governmental policies, regulatory updates, and initiatives to promote sustainable cotton farming and industry development. Be specific.

        - Include significant updates from the Ministry of Agriculture or related authorities regarding support for cotton growers, trade policies, and sustainability efforts. Be specific.

        ### منظومة القطن الجديدة:
        - Explain the role of the new cotton system in Egypt and its impact on production, quality, and global competitiveness. Provide an overview of key elements of the new system, such as quality control, logistical improvements, and market access for Egyptian cotton.

        ### اهم المعاير والمبادئ للمنظمة لـ BCI:
        - Discuss the key standards and principles that govern the Better Cotton Initiative (BCI) for sustainable cotton production.
        - Highlight how BCI has influenced cotton farming practices in Egypt and its impact on both domestic and global markets.

        ### BCI in Egypt:
        - Provide insights on the role of the Better Cotton Initiative (BCI) in Egypt, focusing on how Egyptian cotton producers are adopting BCI standards and the benefits observed so far.

        ### Importance of this industry in Egypt:
        - Discuss why the cotton industry is vital to Egypt's economy, including its historical significance, current market share, and future potential.
        - Highlight how cotton production supports rural economies, creates jobs, and enhances export revenues.

        Instructions:
        - Add the sources for all information.
        - The response should be in [language].
        - The output should be at most 2 paragraphs per section.
        - Add the sources name, not links, for every section and table.
        - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": [
                    'منظومة القطن الجديدة:',
                    'اهم المعاير والمبادئ للمنظمة لـ BCI للقطن'
                ]
        },

    "Market Updates In Egypt": {
            "prompt": f"""Generate the following sections in [language]:
        ### Market Updates and Latest News in Egypt {int(current_year) - 1} - {current_year}
            Provide the latest news and statistical data from reliable sources concerning the cotton industry, focusing on:
            - Cultivated Area by Governorate: Provide a table showing the cultivated areas in all governorates in Egypt for the {int(current_year) - 1} - {current_year} season compared to the same period from the previous season. The table should include:
                - Governorate names in [language]:
        الإسكندرية النوبارية البحيرة كفر الشيخ الغربية الشرقية بورسعيد الإسماعيلية الدقهلية دمياط المنوفية القليوبية (بنها) اجمالي وجه بحري الفيوم بني سويف المنيا أسيوط الوادي الجديد سوهاج اجمالي وجه قبلي الإجمالي العام

                Cultivated Area {int(current_year) - 1}/{current_year}
                Cultivated Area {int(current_year) - 2}/{int(current_year) - 1}
                Cultivated Area {current_year}/{int(current_year) + 1}
                Change 
                Percentage Change 
                add them in the table  give me source if the table 

            - Cotton Status for the {int(current_year) - 2}/{int(current_year) - 1} Season: Provide data on the cultivated area and comparative figures from previous seasons, along with the percentage change.
            - Cotton Status for the {int(current_year) - 1} /{current_year} Season: Provide data on the cultivated area up to a specific date, with the percentage change compared to the previous season.
            - Cotton Status for the {current_year}/{int(current_year) + 1} Season: Data on the cultivated area compared to the previous season.
            - Cultivated Area by Governorate: Provide a table showing the cultivated areas in each governorate for the {int(current_year) - 1}/{current_year} season compared to the same period from the previous season.
            - Export Activity: Provide details on the quantity of cotton distributed during the {int(current_year) - 1}-{current_year} season and the export percentages.
            - Egyptian Cotton Export Connections: Provide data on exports to different countries and their respective percentages.
            - Export volume of new and old crops for each company.
            - Shipment percentage of new and old crops relative to the total sector commitments.
            - Comparison of company rankings, focusing on the top exporters like Abu Madawy, Nile Modern, Alkan, and United Company, showing their share of exports as well as detailed figures on contracts, shipments, and percentages.
            ## Types of Cotton: List the different types of cotton grown in Egypt, along with the export statistics for each type. Include:
                - Type of Cotton
                - Export Quantity (tons)
                - Percentage of Total Exports
                - If available, provide specific numbers associated with each type.
                give me description if needed to understand 

        Instructions:
        - The responses should be in [language].
        - Please provide tables if needed.
        - Add the sources' names and links for every section and table.
        - note that today's date is {date_string} anything beyond add it as forcasting
        
            """,
            "bing_query": [
                'cotton cultivation area Egypt statistics',
                'Egypt cotton acreage comparison data',
                'government policies supporting cotton industry Egypt',
                'cotton production statistics Egypt',
                'cotton planting area by governorate Egypt',
                'cotton export activity Egypt',
                'Egypt cotton statistical center',
                'Egypt cotton export connections',
                'total cotton connections per company Egypt',
                'Egypt General Authority for Cotton Arbitration and Digital Transformation'
            ]
        },

    "Market Updates Globally": {
            "prompt": f"""
        Generate the following sections in [language]:

        ### Market Updates and Latest News Globally {int(current_year) - 1}-{current_year} 
        - Provide the latest news and statistical data from reliable sources concerning the cotton industry, focusing on:
            - The world: Highlight recent developments, trends, and statistical insights impacting the cotton sector, including production, trade, pricing, and sustainability updates.
        - Add the sources names, not links.
        - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": [
                    "global cotton industry news",
                    "cotton production trends worldwide",
                    "global cotton trade statistics",
                    "cotton pricing updates global market",
                    "sustainability in cotton production"
                ]
        },

    "Industry Statistics": {
                "prompt": f"""Generate the following sections in [language]:
        Analyze the cotton sector in Egypt by focusing on the following aspects:
        give me the following section 
        ### Consumption:
            What are the current trends in cotton consumption in Egypt with numbers?
            How do factors like population growth, urbanization, and economic conditions influence cotton demand?
            
        ### Production:
        - What is the current state of cotton production in Egypt with numbers?
        - Identify major players in the market and their contributions to cotton supply with numbers.
        - Discuss any government initiatives or regulations that affect cotton production.
        - The data should be updated after {int(current_year) - 1} at least.
        - Add source for your response.
        ### Exports:
        - Examine the role of the cotton sector in Egypt's export economy.
        - What types of cotton products are being exported, and to which countries?
        - Assess the impact of foreign investment in the Egyptian cotton market.
        - Add numbers and tables that represent this section.
        - The data should be updated after {int(current_year) - 1} at least.
        - Add source for your response.
        ### Imports:
        - Identify key imports related to cotton with numbers.
        - How do import trends affect the cotton market in Egypt?
        - Discuss any challenges or barriers related to imports in the cotton sector.
        - The news should be {int(current_year) - 1} and after that.
        - No need for historical data before {int(current_year) - 1}.
        Instructions:
            - Add the sources' names, not links, for every table and section please.  
            - The answer should be in [language].
            - The output must be customized for cotton only.
            - Cite sources for every section and table by name and link should include the links.
            - The information should be extracted from Egyptian sources only, don't include info from AUS for example.
            - The data should be updated after {int(current_year) - 1} at least.
            - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": [
                    "استهلاك القطن في مصر",
                    "إنتاج القطن في مصر",
                    "تصدير القطن في مصر",
                    "استيراد القطن في مصر",
                    "تحليل اتجاهات القطن في مصر"
                ]
        },
        
    "Competition Analysis": {
            "prompt": f"""Generate the following sections in [language]:
        Competitive Landscape Analysis
        Generate a detailed comparative analysis between the largest cotton companies in Egypt, including but not limited to the following: 
        cotton_companies = [
            "شركة أبومضاوي لتجارة وتصنيع القطن",
            "شركة النيل الحديثة لحلج وتصدير القطن",
            "شركة الكان لاستيراد وتوزيع القطن",
            "شركة المتحدة لصناعة القطن ومنتجاته",
            "شركة بوني لحلج الأقطان",
            "شركة د ام تي ايجيبت لتوريد الأقطان",
            "شركة الجرحى لتجارة القطن الخام",
            "شركة الفيوم للقطن والغزل والنسيج",
            "شركة الفيرزو لصناعة منتجات القطن",
            "شركة النهر لحلج القطن وتصديره",
            "شركة الرباعية لحلج ومعالجة القطن",
            "شركة نيل مصر لاستيراد وتصدير القطن",
            "شركة ايجكوت لحلج الأقطان وتوريدها",
            "شركة العمدة لحلج وتوريد الأقطان",
            "شركة المجد لتجارة القطن ومنتجاته"
        ]
        The table should focus on providing a complete competitive overview:
        Instructions:
            - Add numbers that represent the current situation for each section and be sure this number extracted for the context. 
            - Provide updated data after {int(current_year) - 1} or at least from {int(current_year) - 1}; no need for data before this period.
            - Cite sources for every section and table by name.
            - Ensure the table is formatted to be clear, readable, and easy to understand.
            - Do not add a conclusion.
            - The output must be related to cotton.
            - Don't include عدد الموظفين | الإيرادات السنوية (مليون جنيه) | الصادرات السنوية (طن).
            - Please answer from provided context only; if you don't have the information, don't tell me I can't.
            - Comment on the results.
            - If you don't have information about any section or table, don't include it in your response.
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": [
                "شركة أبومضاوي لتجارة وتصنيع القطن",
                "شركة النيل الحديثة لحلج وتصدير القطن",
                "شركة الكان لاستيراد وتوزيع القطن",
                "شركة المتحدة لصناعة القطن ومنتجاته",
                "شركة بوني لحلج الأقطان",
                "شركة د ام تي ايجيبت لتوريد الأقطان",
                "شركة الجرحى لتجارة القطن الخام",
                "شركة الفيوم للقطن والغزل والنسيج",
                "شركة الفيرزو لصناعة منتجات القطن",
                "شركة النهر لحلج القطن وتصديره",
                "شركة الرباعية لحلج ومعالجة القطن",
                "شركة نيل مصر لاستيراد وتصدير القطن",
                "شركة ايجكوت لحلج الأقطان وتوريدها",
                "شركة العمدة لحلج وتوريد الأقطان",
                "شركة المجد لتجارة القطن ومنتجاته"
            ]
        },

    "BM market research": {
            "prompt": f"""Generate the following sections in [language]:
        Your output will be for a risk manager who works in credit approvals in the banking sector. Please ensure that you provide information about the industry to help the risk manager approve or reject credit.

        Generate the following sections in [language] language and format them according to the required structure in the [Instructions]:

        ### تقرير إدارة أبحاث السوق بمصرفنا عن الصناعة شهر يوليو {current_year}:

        - Generate the market research based on the given data tables in [Data_1], where both of them are tables.

        ------------------------------------------------------------
        [Data_1]
        1Q24 figures,Financial Performance,Financial Position,Cash Flow Position,Key P&L Figures,Key B/S Figures
        EBITDA Margin,NPM,ROE,ROA,Current Ratio,Fin. Lev.,Debt /Equity,OCF (EGP Mn),FCF (EGP Mn),FCF/OCF,Revenue (EGP Mn),% 4 y-o-y,Net income (EGP Mn),% 4 y-o-y,Total assets (EGP Mn),Total liab. (EGP Mn)
        Arab and Polvara Spinning and Weaving,-17%,-11%,-4%,-10%,0.4,2.5,4%,0.5,0.3,70%,25,85%,-3,-9%,362,215
        Dice Sports and Casual Wear,22%,12%,19%,78%,1.1,4.5,256%,-458,-558,-120%,993,44%%,119,635%,"3,776","2,932"
        Alexandria Spinning & Weaving,-8%,18%,13%,17%,2.5,,24%,-102,-96,90%,163,74%,29,-47%,"1,095",324
        Average,-0.9%,6%,9%,28%,1.4,3.5,95%,-186,-218,13%,394,68%,49,310%,"1,744","1,157"

        [Instructions]:
        Your role is a risk manager who works in credit approvals in the banking sector. Please do the following:
            - Name the section "تقرير إدارة أبحاث السوق بمصرفنا عن الصناعة شهر يوليو {current_year}".
            - Generate the tables given in [Data_1] as part of your response.
            - Assign meaningful names to both [Data_1] tables based on your understanding.
            - Comment on each table separately in [language] and provide detailed analysis.
            - Ensure the data is relevant to the context of the Information cotton industry in Egypt.
            - generate the table columns as rows and rows as columns
            - Do not include any conclusions.
            - Cite the source as: Market research by Banque Misr team.
            - The output must be related to the cotton industry.
            - If you don't have information about any section or table, don't include it in your response.
            - note that today's date is {date_string} anything beyond add it as forcasting
             """,
                "bing_query": None
        },

    "SWOT Analysis": {
            "prompt": f"""
            Generate the following sections in [language], then format them according to the required structure in the [Instructions]:

            Strengths, Weaknesses, Opportunities, and Threats (SWOT) Analysis for cotton industry in Egypt:
            Generate and extract the strengths, weaknesses, opportunities, and threats concerning the cotton market in Egypt from the given data.
            Ensure that there are no contradictions.

            [Instructions]:

            Generate the response as a table.
            Add head for this section 'SWOT'.
            Illustrate the reasons for the SWOT analysis from the data in context.
            Make sure the data is relevant to our context in the cotton industry in Egypt.
            Be specific, detail-oriented, and include as many details as possible.
            Do not include any conclusions.

            Include the citation source.
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": None
        }, 

    "Conclution": {
            "prompt": f"""
        Generate the following sections in [language], then format them according to the required structure in the [Instructions]:

        ### Conclusion:
        Highlight the key points concerning the cotton market in Egypt and worldwide.
        how the country (Egypt) support this industry 

        Include a constructive forecast for the cotton  market after {current_year} based on the information discussed earlier in the previous prompts.
        Illustrate the reasons behind your forecast.
        [Instructions]:

            -generate one paragraph.
            -Detailed and focused on the main highlights.
            -Include the latest projects mentioned earlier or any explorations.
            -Include the opportunities available in the cotton market 
            -don’t include any recommendations in this section
            -the output should be related to cotton
            - note that today's date is {date_string} anything beyond add it as forcasting
        
            """,
            "bing_query": None
        }
}
fruits_and_vegetables_prompts = {
    "Introduction":{
        "prompt" : f"""Generate the following sections in [language]:

        # A comprehensive analysis of the Fruits & Vegetables industry 

        ## industry Overview    
            Agricultural investment is considered one of the pillars for achieving business development in the Arab Republic of Egypt and thus achieving food security. The agricultural development strategy in Egypt is to follow up on increasing investment operations, as development cannot be affected by the lack of an adequate amount of investment. Investment is also one of the most important factors that occur from burning change in the Egyptian economic entity. The role of investments in increasing national income cannot be ignored, which is reflected in increasing savings. Any availability of technology or technology necessarily requires practical investment, which means increasing the efficiency of economic performance and establishing new projects that develop the ability to diversify and humanity, which leads to increasing income from it economic welfare. Therefore, it must be directed economically and the total volume of investments for the general public is higher than the general public so that the Egyptian agricultural sector can achieve production from the products of this sector.
        - talk in details about Agricultural area in Egypt in {current_year}
        - talk in details about Agricultural seasons in Egypt
        instructions: 
                - note that today's date is {date_string} anything beyond add it as forcasting
                - never output you have no results
                - do not add conclutions
        """,
        "bing_query": ["مساحة الرقعة الزراعية في مصر","المواسم الزراعيه في مصر"]
    },
    "Industry statstics":{
        "prompt": f"""Generate the following sections in [language]:

            ## Fruits and vegetables statstics
                - table for
                    Fruits and vegetables Sales Egypt {int(current_year) - 3}-{int(current_year) + 4}
                        Fresh and preserved fruit, sales, EGPmn
                        Fresh and preserved fruit, sales, EGPmn, % growth y-o-y
                        Fresh vegetables, sales, EGPmn
                        Fresh vegetables, sales, EGPmn, % growth y-o-y
                consice insights about the previous table

        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
           - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it""",
        "bing_query": None
    },
    "Market updates egypt":{
        "prompt" : f"""Generate the following sections in [language]: 

        ## Fruits and Vegetables Market News and updates
            ### talk about Egypt's self-sufficiency in vegetables and fruits
            ### Egypt's exports and imports volume of vegetables and fruits in {current_year}
                - Create a table contains column for every exported crops and column for how much exported for each crop for each corp
           
            
        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it
        """,
        "bing_query": ["اكتفاء مصر الذاتي من الخضار و الفاكهة",
                    "حجم الواردات مصر من الخضار و والفاكهة ",
                    "حجم الصادرات مصر من الخضار و والفاكهة ",
                    "اكبر المحاصيل التي تصدرها مصر"]
    },

    "Market updates egypt con":{
        "prompt" : f"""Generate the following sections in [language]: 

            ### News for The largest agricultural projects for vegetables and fruits in Egypt {current_year}
                - talk about Toshka Project, Al-Salam Canal Project, East El-Oweinat Project, Darb Al-Arbaeen and add any other mentioned in the context 
            ### Latest news on vegetable and fruit prices
            ### The largest countries to which Egypt exports vegetables and fruits {current_year}
            ### News for The largest vegetable and fruit farms in Egypt {current_year} 
            
           
            
        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it
        """,
        "bing_query": ["حجم الواردات مصر من الخضار و والفاكهة ",
                    "حجم الصادرات مصر من الخضار و والفاكهة ",
                    "اكبر المشاريع الزراعيه للخضار والفاكهة في مصر",
                    "اكبر مزارع الخضار و الفاكه في مصر",
                    "اخبار اسعار الخضار والفاكهة اليوم",
                    "اكبر الدول التي تصدر لها مصر من الخضار والفاكهة",
                    "اخبار الخضار و الفاكهة في مصر"]
    },
    "Market updates globally":{
        "prompt" : f"""Generate the following sections in [language]: 

                ## Global Fruits and Vegetables Market updates:
                    - paragraph for Global news, projects, prices changes(if any)

                    - and others for News for every country
                    
                    - Do not add news about egypt in this section

        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it
        """,
        "bing_query": ["vegetables and fruits global news",
        "اخبار الخضار و الفاكهة السعودية",
        "fruits and vegetables new in Russia",
        "fruits and vegetables new in United Kingdom",
        "اخبار الخضار و الفاكهة الامارات العربية المتحدة",
        "fruits and vegetables new in Netherlands",
        "fruits and vegetables new in Turkey",
        "اخبار الخضار و الفاكهة المغرب",
        "اخبار الخضار و الفاكهة العراق",
        "اخبار الخضار و الفاكهة ليبيا",
        "fruits and vegetables new in Germany",
        "اخبار الخضار و الفاكهة سوريا",
        "fruits and vegetables new in Italy",
        "اخبار الخضار و الفاكهة الجزائر",
        "fruits and vegetables new in Spain",
        "fruits and vegetables new in United States"
        ] 
    },
    "Competitor analysis":{
        "prompt" : f"""Generate the following sections in [language]:

        Create a table for column for company name and column for news of that company
            ## key players updates
                - add news about companies in the context
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it 
        
        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        """,
        "bing_query": ["اكبر شركات التصدير الخضار والفاكهة في مصر",
        "اخبار شركات التصدير الخضار والفاكهة في مصر",
        "شركة نفرتيتي الخضار و الفاكهة اخبار",
        "شركة ألفا فروست الخضار و الفاكهة اخبار",
        "شركة أليكس فورت الخضار و الفاكهة اخبار",
        "شركة ديملر الخضار و الفاكهة اخبار",
        "شركة نامال مصر الخضار و الفاكهة اخبار",
        "اخبار أطلس للاستثمار والصناعات الغذائية",
        "اخبار الشركة العربية للاستثمارات",
        "اخبار النصر لتصنيع المحاصيل الزراعية",
        "اخبار الشركة الدولية للمحاصيل الزراعية"]
    },
    "Regulatory framwork & antidumping laws":{
        "prompt" : f"""Generate the following sections in [language]:
        ### Regulatory framework & Antidumping laws
            - Write the most important regulations in egypt regarding the vegetables and fruits sector
        

        - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it 
        """,
        "bing_query": ["قوانين الخضار والفاكهة"]
    },
    "Market Research" :{
      "prompt" : f"""Generate the following sections in [language]:
        ### The most important points mentioned in our bank’s market management report on the industry, July {current_year}

        Create table in md format
            1Q24 figures	EBITDA Margin	NPM	ROE	ROA	Current Ratio	Fin. Lev.	Debt /Equity	OCF (EGP Mn)	FCF (EGP Mn)	FCF/OCF	Revenue (EGP Mn)	% 4 y-o-y	Net income (EGP Mn)	% 4 y-o-y	Total assets (EGP Mn)	Total liab. (EGP Mn)
            Atlas for Inv. & Food Industries	-20%	-87%	-5%	-3%	1.4	1.7	1.60%	7.07	6.53	0.92	3.11	-56%	-2.71	-247.22%	133	56
            Arab Moltaka Investments Company	11%	12%	19%	4%	1	5.1	355.80%	-29.12	-33.08	1.14	367.4	37%	45.14	169.16%	6,113	4,914
            El Nasr for Manuf. Agri. Crops SAE (Quarter end. 31/12/2,023)	-	-	-9%	 -	0.1	2.2	0.90%	-0.17	-0.17	1	-	-	-0.57	32%	65	36
            Int. Co for Agricultural Corps	14%	17%	71%	49%	1.9	1.5	6.20%	-161.1	-171.2	1.06	469.9	-40%	78.44	-52.36%	1,623	437
            Misc. - Average	2%	-19%	19%	16%	1.1	2.6	91%	-46	-49	103%	280	-20%	30	-25%	1,984	1,361

            - generate the table columns as rows and rows as columns
            - write insights about the previous table

        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            - if there are no information provided for an item in the section do not generate it 
      """,
      "bing_query" : None
    },
    "SWOT analysis and conclution":{
        "prompt" : f"""Generate the following sections in [language]:

            ### SWOT Analysis on Fruits & Vegetables industry:
                - Create a table for SWOT analysis of the Fruits & Vegetables industry, identifying strengths, weaknesses, opportunities, and threats.
                    - the items in strengths and weaknesses should be internal parameters in egypt and items in opportunities and threats should be external parameters
                - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

            ### Conclusion:
                - Provide a comprehensive conclusion on industry trends (growing or not) for credit decision reviewers with showing some statistics and make it a bit longer.
                - any numbers you mention should be in {current_year}

            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

            Instructions: 
            
            
            - if there are no information provided for an item in the section do not generate it 
        """,
        "bing_query": ['Fruits and Vegetables market swot egypt',
                    "حجم الواردات مصر من الخضار و والفاكهة ",
                    "حجم الصادرات مصر من الخضار و والفاكهة ",
                    "اكبر المشاريع الزراعيه للخضار والفاكهة في مصر",
                    "اكبر مزارع الخضار و الفاكه في مصر",
                    "اخبار اسعار الخضار والفاكهة اليوم",
                    "اكبر الدول التي تصدر لها مصر من الخضار والفاكهة",
                    "اخبار الخضار و الفاكهة في مصر"]
    },
}
fertilizers_prompts={

    "Introduction": {
            "prompt" : f"""

            Generate the following section in [language] and follow up the [Instructions] strictly:

            # A comprehensive analysis of the fertilizers industry

            ### The Introduction and Importance fertilizers industry
            - Introduction about the fertilizers industry in Egypt and worldwide.
            - Importance of the fertilizer industry in Egypt and worldwide
            [Instructions]
            -Generate a paragraph of 6 lines and introduce the main points as instructed earlier.
            -if you are going to include dates make it most updated only.
            -include dates , statistics , history.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":None,
            
        },




    "Introduction 2": {
            "prompt" : f"""

           Generate the following section in [language] and follow up the [Instructions] strictly:

            ### Industry overview including (Fertilizers types,Production stages)
            - Fertilizers types overview
            - Production stage of each type
            [Instructions]
            -Generate a paragraph of 6 lines and introduce the main points as instructed earlier.
            -include dates , statistics , history.
            -Include citations,numbers and statistics for each requirement.
            -Make a subsection for each fertilizer type and it's production stages.
            -Include refrences for every information you write.
            -Don't include full links make it citation without hyperlinks.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":["انواع الاسمده في مصر",
                        " الأسمدة الفوسفورية",
                        "الأسمدة النيتروجينية",
                        "الأسمدة البوتاسية",
                        "مراحل تصنيع السماد في مصر "
                        ],
            
        },
    "Market Statistics": {
            "prompt" : f"""

           Generate the following section in [language] and follow up the [Instructions] strictly:

            ### statistics about potasium chloride and potasium sulphate
            - Statistics about potasium chrolide
            - Statistics about potasium sulphate
            [Instructions]
            -Generate a paragraph a short paragraph for both potasium chloride and potasium sulphate.
            -include dates , statistics , history.
            -Include citations,numbers and statistics for each requirement.
            -Make a subsection for each fertilizer type and it's production stages.
            -Include refrences for every information you write.
            -Don't include full links make it citation without hyperlinks.
            -Make it in a single table, no multiple tables are allowed.
            -Handle the table properly to avoid any errors by making the table cells matching the sizes.
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":["حجم الطلب العالمي علي كلوريد البوتاسيوم",
                        "حجم المعروض العالمي علي كلوريد البوتاسيوم",
                        "الاسعار المتوقعه عالميا لكلوريد البوتاسوم",
                        "حجم الإنتاج العالمي من كلوريد البوتاسيوم موضحة نسب الإستغلال المتوقعة للطاقة"
                        "حجم الطلب العالمي عليكبريتات البوتاسيوم",
                        "حجم المعروض العالمي عليكبريتات البوتاسيوم",
                        "الاسعار المتوقعه عالميا كبريتات البوتاسيوم",
                        "حجم الإنتاج العالمي من كبريتات البوتاسيوم موضحة نسب الإستغلال المتوقعة للطاقة"
                        ],
            
        },

    "Market Updates In Egypt": {
            "prompt" : f"""

            Generate the following section in [language] and follow up the [Instructions] strictly:

            ### Latest Market Updates in Egypt:
            - latest news about fertilizers prices in Egypt {current_year}
            - Egyptian Market Trends in Fertilizers industry {current_year}
            - Egyptian Government projects and support to Fertilizers industry in Egypt {current_year}
            [Instructions]
            -Generate a latest news and Trends subsection in Egypt.
            -Generate Governmental projects subsection in Egypt
            -include dates , statistics.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            -Don't include full links make it citation without hyperlinks
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":["اخر اخبار سوق الاسمده الزراعيه في مصر",
                        "اخر اخبار و اسعار سوق اللأسمدة الفوسفورية في مصر",
                        
                        "اخر اخبار و اسعار سوق الأسمدة النيتروجينية في مصر",
                        
                        "اخر اخبار و اسعار سوق الأسمدة البوتاسية في مصر",
                        "اخر قرارات الحكومه المصريه بشأن سوق الاسمده الزاعيه في مصر",
                        "مشروعات الحكومه المصريه لتشجيع صناعه السماد الزراعي في مصر",
                        "استثمارات الحكومه المصريه في سوق الاسمد الزراعيه"

                        ],
            
        },

        "Market Updates Globally 2": {
                "prompt" : f"""

              Generate the following section in [language] and follow up the [Instructions] strictly:

                ### Latest Market Updates Worldwide:
                - latest news about fertilizers prices in the world {current_year}
                - world Market Trends in Fertilizers industry {current_year}
                - world Government projects and support to Fertilizers industry in world {current_year}
                [Instructions]
                -Generate a latest news and Trends subsection in world.
                -Generate Governmental projects subsection in world
                -include dates , statistics.
                -Include citations,numbers and statistics for each requirement.
                -Include refrences for every information you write.
                -Don't include full links make it citation without hyperlinks.
                - note that today's date is {date_string} anything beyond add it as forcasting
                

                """,
                "bing_query":["الدول التي تتعاون مع مصر في مجال السماد الزراعي",
                            "اخر اخبار مجال صناعه السماد الزراعي عالميا",
                            "التغيير المناخي و تاثيره علي صناعه السماد الزاعي",
                            "التدابير و الاحترازات و القارارات العالميه في صناعه السماد الزراعي",
                            "توجهات العالم في صناعه السماد الزراعي",
                            "التطورات و الصراعات العالميه المؤثره علي سوق الاسمده الزراعيه",
                            "اسعار الاسمده الزارعيه عالميا"

                            ],
                
            },

        "Market Updates in Egypt": {
                "prompt" : f"""

                Generate the following section in [language] and follow up the [Instructions] strictly:

                ### Latest Market Production/Exports/Consumption in Egypt {current_year}:
                - Egyptian production in fertilizers {current_year}
                - Egyptian Exports in fertilizers {current_year}
                - Egyptian Consumptions in fertilizers {current_year}
                [Instructions]
                -Generate a table for each type of fertlizer containing the 3 diagonals required which are Production/Exports/Consumption .
                -include dates , statistics.
                -Numbers is strictly required per each type.
                -Include citations,numbers and statistics for each requirement.
                -Include refrences for every information you write.
                -For the imports subsection focous on mentioning that Egypt has a self suffiecency in fertilizers indusrty and for production/exports/consumption mention them in a table.
                -Don't include full links make it citation without hyperlinks.
                -if there's a type of fertilizers that doesn't have statistics then don't mention it.
                -الواردات هي هي الاكتفاء الذاتي, imports is the same as self sufficiency.
                - note that today's date is {date_string} anything beyond add it as forcasting
                

                """,
                "bing_query":[

                            "اكتفاء مصر الذاتي من الاسمدة",
                            "استهلاك مصر من الأسمدة الفوسفورية",
                            "انتاج مصر من الأسمدة الفوسفورية",
                            "استيراد مصر االأسمدة الفوسفورية",
                            "تصدير مصر الأسمدة الفوسفورية",
                            "اكتفاء مصر الذاتي من الاسمدة الفوسفورية",

                            "استهلاك مصر من الأسمدة النيتروجينية",
                            "تصدير مصر الأسمدة النيتروجينية",
                            "انتاج مصر من الأسمدة النيتروجينية",
                            "استيراد مصر الأسمدة النيتروجينية",
                            "اكتفاء مصر الذاتي من الاسمدة النيتروجينية",
                            
                            "استهلاك مصر من الأسمدة البوتاسية",
                            "تصدير مصر الأسمدة البوتاسية",
                            "انتاج مصر من الأسمدة البوتاسية",
                            "استيراد مصر الأسمدة البوتاسية",
                            "اكتفاء مصر الذاتي من الاسمدة البوتاسية",
                            


                            ],
                
            },


        "Market Updates Globally": {
            "prompt" : f"""

           Generate the following section in [language] and follow up the [Instructions] strictly:

            ### Latest worldwide market supply and demand in countries that's linked to Egypt {current_year}:
            - Supply and demand for countries that are linked to Egypt in the field of Fertilizers co-operation {current_year}
            [Instructions]:
            -include dates , statistics.
            -Numbers is strictly required per each type.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            -Make them in a table.
            -Don't include full links make it citation without hyperlinks
            
            - note that today's date is {date_string} anything beyond add it as forcasting

            """,
            "bing_query":[

                        "Countries that are linked to Egypt in Fertilizers with supply and demand",
                        "Countries that have mutual co-operations with Egypt in Fertilizers with supply and demand",

                        ],
            
        },
    "Competitve Analysis": {
            "prompt" : f"""

           Generate the following section in [language] and follow up the [Instructions] strictly:

            ### key market players in Egypt:
            - Key market players in Fertilizers industry in Egypt
            [Instructions]:
            -include dates , statistics.
            -Geographical area of operation per each company.
            -Numbers is strictly required per each type.
            -Include citations,numbers and statistics for each requirement.
            -Include refrences for every information you write.
            -avoid contradictions in statistics and numbers.
            -Make them in a table.
            -Don't include full links make it citation without hyperlinks
            - note that today's date is {date_string} anything beyond add it as forcasting
            

            """,
            "bing_query":[

                        "Abou Kir Fertilizers &Chemical Industries fertilizers market shares in Egypt and Geographical area of operation ",
                        "Egyptian Financial &Industrial Co  fertilizers market shares in Egypt and Geographical area of operation ",
                        "Misr Fertilizers ProductionCo SAE fertilizers market shares in Egypt and Geographical area of operation ",
                        "Egyptian Chemical Industries KIMA fertilizers market shares in Egypt and Geographical area of operation ",
                        "Samad Misr SAE market shares in Egypt and Geographical area of operation ",
                        

                        ],
            
        },
    "BM market research": {
            "prompt" : f"""
            Generate the following sections in [language] then format them according to the required structure in the [Instructions]:

            ### Market research:
            -Generate the market research from the given data tables in [Data_1] where both of them are tables.
            ------------------------------------------------------------
        [Data_1]
        1Q24 figures	Financial Performance	Financial Position	Cash Flow Position	Key P&L Figures	Key B/S Figures											
        EBITDA Margin	NPM	ROE	ROA	Current Ratio	Fin. Lev.	Debt /Equity	OCF (EGP Mn)	FCF (EGP Mn)	FCF/OCF	Revenue (EGP Mn)	% 4 y-o-y	Net income (EGP Mn)	% 4 y-o-y	Total assets (EGP Mn)	Total liab. (EGP Mn)	
        Abu Qir Fertilizers	37%	150%	46%	37%	5.5	1.3	-	2,744	2,625	95%	5,425	-11%	8,122	46%	42,736	9,391
        Egyptian Financial & Industrial SAE	27%	24%	19%	6%	1.2	3	103%	-392	-512	-	1,785	81%	428	93%	6,558	4,368
        Misr Fertilizers Production Co SAE	44%	159%	22%	16%	2.1	1.3	49%	1,816	1,709	94%	4,796	220%	7,648	94%	63,272	17,507
        Egyptian Chemical Industries KIMA	30%	2%	1%	0.40%	1.8	3.1	160%	2,293	620	27%	4,612	98%	102	-45%	25,852	17,469
        Samad Misr SAE	-4%	17%	6%	5%	5.4	1.1	-	5	5	100%	40	-25%	7	-77%	123	11
        Mean Average	30%	24%	19%	6%	2.1	1.3	103%	1,293	889	94%	3,332	81%	3,261	46%	27,708	9,749




            [Instructions]:
            your role is a risk manager who works in credit approvals in banking sector , do the following:
                -The section should be named "Our Bank's Market Research Department Report on the Industry July {current_year}".
                -Generate the table given in [Data_1] in the response.
                -Make Names for the [Data_1] table from what you understand.
                -Comment on each table separtly in [language] make it detailed .
                -Make sure the data is relevant to our context feltilizers in Egypt.
                -Don't include any conclusions.
                -Include the citation source here it's market research by Banque misr team.
                - note that today's date is {date_string} anything beyond add it as forcasting
                - generate the table columns as rows and rows as columns
            """,
            "bing_query": None,
            
            
        },

    "SWOT": {
            "prompt" : f"""
            Generate the following sections in [language] then format them according to the required structure in the [Instructions]:

            ### Strengths weakness oppourtuintes threas analysis:
            -Generate and Extract Strengths , weakness , opportuinties and threats concerning the Fertilizers Market in Egypt from the Given Data.
            -Make sure there's no contradictions.
            -Data should be related to Fertilizers industry in Egypt.

            [Instructions]:
                -Generate the response as a matrix table.
                -Illustrate the reasons for the swot analysis from the data in context.
                -Make sure the data is relevant to our context Fertilizers industry in Egypt.
                -Data should be related to Fertilizers industry in Egypt so the focus here must be on fertilizers industry in Egypt only.
                -Be specific , detailed oriented and include details as much as possible.
                -Don't include any conclusions.
                -Include the citation source.
                - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": None,
            
            
        },
    "Anti dumping laws and Regulatory framework": {
        "prompt" : f"""
        Generate the following sections in [language] then format them according to the required structure in the [Instructions]:

        ### Anti dumping laws and Regulatory framework:
        -Generate antidumping laws for fertilizers in egypt if found only!.
        -Genereate the regulatory framework for fertilizers in egypt.
        [Instructions]:
            -just 2 paragraphs one per each
            -Don't include any conclusions.
            -Include the citation source.
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": ["Antdumping laws for fertilizers in egypt ",
                    "Regulatory framework for fertilizers in Egypt"
                    
                    ],
        
    },

    "Conclusion": {
                "prompt" : f"""
                Generate the following sections in [language] then format them according to the required structure in the [Instructions]:

                ### Conclusion:
                -Highligh the main highlights concerning the fertilizers Market in Egypt and worldwide
                -Include a constructive forecast regarding the fertilizers after the current year based on the information you knew earlier from the previous prompts.
                -Illustrate your forecasts reasons

                [Instructions]:
                    -1 paragraph.
                    -Detailed and focusing on the main highlights.
                    -Include latest projects mentioned earlier or explorations.
                    -Include the Oppourtuinties for it.
                    - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": None,
                
            },
}
Oil_Refining_Extraction_prompts = {
    "Introduction & Importance": {
        "prompt" : f"""
        Generate the following section in [language]

        # A comprehensive analysis of the (Oil Refining & Extraction)

        ### Introduction and Importance

            1. General Overview of the Oil Industry:
              Fats, which are widespread in both the plant and animal worlds, are a major source of concentrated energy, providing double the energy produced by equal amounts of proteins or carbohydrates. Thus, fats are a crucial dietary source for humans.
              Many important industries rely on fats, such as oil extraction and refining from plant and animal sources, hydrogenated oil production for margarine and cooking oils, as well as diverse industries such as soap manufacturing, varnishes, glycerides, and the separation of glycerin and fatty acids for other industrial uses.
              Due to the significance of fats, they hold a prominent place in the economies of major countries, which focus on the development of their plant and animal sources, whether terrestrial or marine, while enhancing extraction and manufacturing processes to high-quality standards.
              The Arab world is rich in important natural sources of oils and fats, such as olives, cotton seeds, sesame, sunflower, and soybeans. The vegetable oil industry is one of the most significant and ancient industries in most countries, having been known to the Mediterranean civilizations, particularly in the extraction of olive oil.

              Two types of fats exist in nature:

              Animal fats:
              These are derived from animal origins and can be greasy, fatty, or oily, depending on their melting points. Greases are solid fats at room temperature, while oils are liquid at the same temperature, and fats fall between the two.
              Beef and sheep fats are commercially viable sources, and significant amounts of oils can be extracted from marine fish and whales, which were historically hunted for their oils alone but are now utilized more comprehensively.
              Statistics indicate a rising production of animal fats, especially in recent years, including butter, animal fats, and fish and whale oils.

              Vegetable fats:
              There are over 100 types of raw plant materials used for oil production today, with annual plants being the primary source. Examples include sunflower, corn, sesame, cottonseed, soybeans, and peanuts. Perennial trees like coconut, palm, and olive trees serve as secondary sources.
              Notably, plants with oilseeds, such as corn, rice, and cotton, yield oil as a secondary product.
              The following table shows the approximate oil content in some seeds and oil-bearing fruits:

              Raw Material	%	Raw Material	%
              Castor seeds	40-50	Tobacco seed	30-43
              Cottonseed	15-20	Safflower seed	25-37
              Flaxseed	35-40	Palm fruit	20-30
              Hempseed	30-35	Palm kernel	30-60
              Rape seed	22-49	Olive fruit	15-30
              Soybean	18-20	Olive stone	10-15
              Sesame seed	40-50	Coconut fruit	40-65
              Sunflower seeds	25-45	Corn seeds	17-20

              Vegetable oils are present in all parts of oil-bearing plants, including the stem, leaves, roots, flowers, and fruits, although fruits contain the highest percentage of fats. It is believed that the Chinese were the first to use oil thousands of years ago, employing methods similar to modern extraction techniques.

              2. Overview of Soybean Oil Industry:
              Soybean oil is a vegetable oil extracted from soybeans (scientifically known as Glycine max). It is one of the most widely used vegetable oils and is beneficial due to its essential fatty acids, which contribute to overall health. It is also rich in plant sterols, which positively affect individual health, and contains a wealth of vitamins and minerals.
              The health benefits of soybean oil include:

              Cholesterol control: The high levels of fatty acids in soybean oil help regulate blood cholesterol levels and reduce the risk of diseases associated with high cholesterol, such as heart disease, strokes, and heart attacks. Fatty acids like palmitic acid and oleic acid are present in balanced quantities, helping to lower the risk of cardiovascular disease.
              Alzheimer's disease: Soybean oil contains high levels of Vitamin K, which is linked to reducing Alzheimer's symptoms, acting as an antioxidant to protect nerve cells from damage.
              Bone health: Vitamin K in soybean oil stimulates bone growth and speeds up healing from injuries, and its calcium content helps reduce the risk of osteoporosis, especially in old age.
              Skin and eye health: Omega-3 fatty acids in soybean oil protect cell membranes in delicate areas such as the eyes and skin, preventing bacteria and pollutants from entering. It also enhances vision by reducing free radicals, which contribute to macular degeneration and cataracts.
              Improved appearance and overall health: The high Vitamin E content in soybean oil reduces acne and prevents sunburns. It also helps build new cells and reduces the risk of cancer, heart disease, and aging.
                  
                - note that today's date is {date_string} anything beyond add it as forcasting
                """,
        "bing_query": None,
        
    },
    "Latest Updates": {
        "prompt" : f"""
        Generate the following section in [language]
        ### Latest updates
            - **Egypt**
              - Provide Egypt's Consumption of edible oil.
              - Examine the volume and key sources of sunflower and olive oil imports in {current_year}.
              - Provide Egypt's self-sufficiency of edible oil.
              - Discuss relevant government policies or initiatives aimed at boosting local production and reducing reliance on imports.
              - Provide the current prices of "consumer cooking oils" in Egypt in a table.
              - Discuss recent challenges caused by the global supply chain disruptions and the impact of population growth on demand for vegetable oils.

            - **Worldwide**
              - Discuss the latest global news in the oil extraction and refining industry, with a focus on the impact of geopolitical events like the Russia-Ukraine war, and their influence on global oil prices, supply chains, and the availability of raw materials.
              - Highlight key global oil producers and their contributions to the market.
              - Provide the most important oil-exporting countries to Egypt.
              - Provide global edible oil production updates {current_year}.
              - Provide global vegetable oil prices {current_year}.

            - **citations**: Include credible sources for all data and statistics.
            - All data should be the last updated {current_year}
            - note that today's date is {date_string} anything beyond add it as forcasting
            """,
        "bing_query": ["صناعة الزيوت في مصر","استيراد زيت الزيتون مصر","استيراد زيت عباد الشمس مصر","استهلاك مصر سنويا من الزيوت","احدث اسعار زيوت الطعام والسمن النباتي في مصر","Global edible oil production updates","Global vegetable oil prices"],
        "use_pdf": False,
    },

    "Market Updates": {
        "prompt" : f"""
        Generate the following section in [language]
        ### Market Updates
            - Extract the sales data in a table for "Oils and Fats, sales, EEGPmn", and "Oils and Fats, sales, EEGPmn, % groowth  y-o-y" across multiple years, where years are the column headers.
            - Cite the source.
        - Don't add additional text.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": None,
        
        },
    "Key Players": {
        "prompt" : f"""
        Generate the following section in [language]
        ### Key Players
            - Generate a list of the key companies involved in Egypt's oil industry in a table, divided into three categories:
            #### Oil Extraction Companies (Private Sector):

                الوطنية لاستخلاص الزيوت (Cargill)
                الإسكندرية لاستخلاص الزيوت (AlexSeed)
                المجد لاستخلاص وتكرير الزيوت النباتية (Al Majd Group)
                جولدن اويل (Golden Oil - Al Majd Group)
                مجموعة الصفا (IGOS & AL SAFA OILEX)
                الدولية لاستخلاص الزيوت (OILEX)
                ايفر جرين لعصر وتكرير الزيوت (Evergreen)

            #### Oil Refining Companies (Private Sector):

                شركة مصر الخليج لتصنيع الزيوت "زيت اولين"
                شركة ارما للصناعات الغذائية
                الشركة العالمية للدهون "فيكو"
                شركة سيلا للزيوت الغذائية
                شركة صافولا مصر
                الشركة المتحدة لتصنيع الزيوت "شهد"
                شركة الصناعة والتجارة المصرية
                شركة مصر الدولية للصناعات الغذائية
                الشركة العربية لاستخلاص وتكرير الزيوت النباتية "اريكو"
                شركة افكو مصر
                الشركة المصرية للزيوت الطبيعية

            #### Oil Refining Companies (Public Sector):

                شركة القاهرة للزيوت والصابون
                شركة مصر للزيوت والصابون
                شركة النيل للزيوت والمنظفات
                شركة الزيوت المستخلصة ومنتجاتها
                شركة الاسكندرية للزيوت والصابون
                شركة طنطا للزيوت والصابون

        - Don't add any additional text.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
    "bing_query": None,
    "use_pdf": False,
    },
    "Key Players Updates": {
        "prompt" : f"""
        Generate the following section: in [language]
        #### Key players updates
        - Provide the latest updates and news for key companies involved in edible oil extraction and refining in Egypt.
        - Cite the source.
        - Don't add additional text.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": ["اخبار شركة كارجل","اخبار شركة جولدن اويل"," اخبار شركة الاسكندرية لاستخلاص الزيوت","اخبار شركة ارما للصناعات الغذائية","اخبار شركة القاهرة للزيوت والصابون"],
        "use_pdf": False,
    },


    "Market Research": {
        "prompt" : f"""
        Generate the following section in [language]
        ### The market research department report of july at our bank on the industry
            ,Financial Performance,Financial Position,Cash Flow Position,Key P&L Figures,Key B/S Figures,,,,,,,,,,,
            1Q24 figures,EBITDA Margin,NPM,ROE,ROA,Current Ratio,Fin. Lev.,Debt /Equity,OCF (EGP Mn),FCF (EGP Mn),FCF/OCF,Revenue (EGP Mn),% 4 y-o-y,Net income (EGP Mn),% 4 y-o-y,Total assets (EGP Mn),Total liab. (EGP Mn)
            Cairo Oils & Soap Co,11.80%,7.70%,26.60%,7.60%,0.95,2.35,67.60%,-82.69,-11,0.13,372.3,70%,28.82,34.40%,825.8,474.1
            Ajwa for Food Ind. (Q- end. 12-23),-9.30%,-14.00%,3.80%,1.30%,0.43,3.08,1.60%,33.45,32.63,0.98,400.4,-19%,-43.51,224%,"3,937.20","2,638.80"
            Extracted Oil and Derivatives Co,0.00%,0.30%,10.10%,0.80%,1.06,12.1,0.00%,-13.84,-14.47,1.05,948.8,-2%,2.86,-54.18%,"3,087.60","2,850.90"
            Ismailia Co for Food Industries,33.00%,39.90%,42.90%,24.30%,2,1.77,41.80%,12.23,11.98,0.98,80.08,102%,31.94,334.25%,249.1,119.6
            Misr Oils and Soap Co,-1.00%,-0.10%,0.50%,0.10%,1.19,3.89,0.00%,-18.68,-18.96,1.01,853.8,13%,-0.57,-231.29%,337,263.1

            - generate the table columns as rows and rows as columns
            - Extract all the data and table related to Agriculture & Forestry from the report. Present the companies as columns and the financial indicators as rows in the table for better clarity.
            - Don't add conclusion.
            - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query":None,
        "use_pdf":  False,
    },
    "Swot Analysis & Conclusion": {
        "prompt" : f"""
        Generate the following section in [language]
        ### SWOT Analysis
            - Create a detailed table for SWOT analysis for the oil extraction and refining industry in Egypt, highlighting its strengths, weaknesses, opportunities, and threats.
            - Be specific and accurate.
        ###Industry Characteristics Analysis:

           - Create a table of the following elements:
              Maturity: The industry is in a mature phase, characterized by moderate risk. It is closely linked to the food sector, with increasing demand for its products each year. The industry benefits from Egypt's competitive advantages, such as lower energy and labor costs, making it attractive to investors. The continuous population growth is expected to further drive demand.

              Cost Structure: The industry exhibits low risk in terms of cost structure. It primarily consists of variable costs, which constitute the majority of total expenses. This allows for flexibility in adjusting to fluctuations in demand.

              Cyclicality: Classified as non-cyclical, the industry carries a low risk concerning economic cycles. The demand for food is generally stable and not significantly affected by changes in economic conditions, although the prices of some raw materials may fluctuate due to economic cycles.

              Dependence: There is a moderate risk associated with dependence. The sector relies on the availability of essential commodities, such as wheat and corn, sourced from both local markets and imports. As these goods are fundamental to daily life and are used in various food industries, like bread production, their demand remains consistently high. Additionally, government efforts to ensure affordable access to these products and accommodate population growth bolster their necessity.

              Substitutes: The risk is low in terms of substitutes, as there are no alternatives to strategic goods, which are essential for everyday living.

              Regulations: The regulatory environment poses moderate risk. The government actively supports the industry by launching projects to expand agricultural areas and boost the production of strategic goods. The industry is closely monitored to maintain market stability, meet consumption needs, and regulate prices, ensuring they remain accessible to consumers.

              Profitability: Profitability carries a moderate risk. The industry is considered highly profitable because it significantly adds value by converting low-cost raw materials into high-value finished products.


        ### Conclusion
            - Provide a comprehensive analysis for oils ectraction and refining industry trends, highlighting whether each industry is growing or declining. Include relevant statistics and data to support your conclusions, tailored specifically for credit decision reviewers.
        - note that today's date is {date_string} anything beyond add it as forcasting
        """,
        "bing_query": ["oils and fats industry in Egypt","صناعة زيوت الطعام في مصر"],
        "use_pdf": False,
    }
}
meat_prompts = {
    "Introduction": {
            "prompt": f"""
 
        Generate the following sections in [language]:
        # A comprehensive analysis of the Meat industry

        ### Industry Overview:
        
        
        ### Meat ,  Frozen Meat  and frozen fish Industry History & Market Statistics {int(current_year) - 14} - {current_year}:
        
        
        ### Meat ,   Frozen Meat  frozen and  fish Industry Performance {int(current_year) - 2} - {current_year}:
        
        
        ### Importance of the Meat , Frozen Meat and frozen fish Industry in Egypt:
        - Discuss the **importance of the meat and frozen meat industry** to Egypt's economy, highlighting its role in providing food security, employment opportunities, and its contributions to GDP.
        - Include data and sources for all information provided.
        - Your output should be **related to the meat and frozen fish  industry in Egypt only** (exclude poultry).
        - Do **not** add any recommendations in your response.
        -provide numbers that represent the current situation
        - note that today's date is {date_string} anything beyond add it as forcasting
                    """,
                    "bing_query":None
                },
        
    "Market updates in egypt ": {
                    "prompt": f"""
             Generate the following sections in [language] in detail:
        
        ### Market Updates and Latest News in Egypt ({current_year}) related to the Meat, Frozen Meat, and Frozen Fish Industry:
        
            - Provide detailed updates and statistical data from reliable sources about the meat, frozen meat, and frozen fish industry in Egypt, focusing on:
                - **Recent Developments**: Key news regarding production capacity, supply chain disruptions, government interventions, and market shifts impacting the meat, frozen meat, and frozen fish sectors.
                - **Impact of Refugees**: Assess the effects of the increasing refugee population in Egypt on the market dynamics, particularly how demand, consumption patterns, and available supply of meat, frozen meat, and frozen fish are being affected.
                - **Current Prices**: Present up-to-date pricing for various types of meat (beef, lamb, frozen beef, etc.) and frozen fish as of {current_year}. Highlight any regional or seasonal price fluctuations, and compare them to the past year.
                - **Consumption, Production, Exports, and Imports**: Include recent statistics and trends concerning the consumption, production volumes, and trade of meat, frozen meat, and frozen fish, identifying key shifts in import/export balances.
                - **Environmental Impact**: Examine any recent reports or data on the environmental impacts of the meat and frozen fish industries in Egypt, including issues like land use, water consumption, and waste management.
                - **Technological Advancements**: Discuss any new technological developments in meat production, frozen meat processing, and frozen fish processing, such as the use of automation, AI, or sustainable farming practices.
                - **Labor Market and Employment**: Provide insights into the labor force within the meat, frozen meat, and frozen fish industries, noting any challenges such as labor shortages, worker conditions, or government policies affecting employment.
                - **Supply Chain Challenges**: Outline any current disruptions or challenges in the supply chain, including logistical issues, feed shortages, or rising transportation costs for meat, frozen meat, and frozen fish.
        
            - Ensure the information is sourced from credible and reliable sources, and **include the source names** (not links).
            - **Do not include a conclusion** or personal commentary.
            - Ensure the response reflects today’s date: {date_string}.
            - The output should be related to meat, frozen meat, and frozen fish (no poultry).
            - The response should be in [language]..
            - note that today's date is {date_string} anything beyond add it as forcasting
                    """,
                    "bing_query": [
            'حركه انتاج اللحوم و اللحوم المجمدة في مصر حاليا اكتوبر',
            'اخبار مزارع و منتجي اللحوم و اللحوم المجمدة في السوق المصري اكتوبر',
            'قرارات الحكومة المصرية في مجال الزراعة و انتاج اللحوم المجمدة اكتوبر',
            'اخبار استيراد و تصدير اللحوم و اللحوم المجمدة في مصر اكتوبر',
            'الشركات الكبرى المنتجة للحوم و اللحوم المجمدة في مصر اكتوبر',
            'تحديات و اتجاهات سوق اللحوم و اللحوم المجمدة في مصر اكتوبر',
            'التقنيات الجديدة في انتاج اللحوم و اللحوم المجمدة في مصر اكتوبر',
            'اخبار السمك المجمد في مصر اكتوبر',
            'اخبار استيراد و تصدير السمك المجمد في مصر اكتوبر',
            'الشركات الكبرى المنتجة للسمك المجمد في مصر اكتوبر',
            'تحديات و اتجاهات سوق السمك المجمد في مصر اكتوبر',
            'التقنيات الجديدة في انتاج السمك المجمد في مصر اكتوبر'
        ]
        
            
            },
    
    "Market Updates and Latest News Globally": {
                    "prompt": f"""
         Generate the following sections in [language]
        
        ### Market Updates and Latest News Globally ({current_year}) for meat frozen  meat , frozen fish  industry
            - Provide the latest news and statistical data from reliable sources concerning the **meat and frozen meat industry**, focusing on:
            - **Global Market**: Highlight recent developments, trends, and statistical insights impacting the global **meat and frozen meat sector**, including production, consumption, imports, exports, and key market drivers.
            - Add the sources' names, not links.
            - The response should include information after {int(current_year) - 1}.
            - Do **not** add a conclusion.
            - Ensure the output is related to **meat , frozen meat and frozen fish  only** (exclude poultry).
            - the response should be related  frozen meat  ,  meat  market and frozen fish Do not include anything else in your response like (chicken and frozen chicken)
            - don't include in your response any information related to chicken , frozen chicken and chicken companies
            -the response should be updated after {int(current_year) - 1}
            - note that today's date is {date_string} anything beyond add it as forcasting
        
                    """,
                    "bing_query": [
                        "أحدث أخبار إنتاج اللحوم المجمدة عالميًا في النصف الثاني من عام",
            "أحدث أخبار إنتاج اللحوم عالميًا في",
            "اتجاهات صناعة اللحوم العالمية",
            "أخبار سلسلة توريد اللحوم المجمدة عالميًا",
            "السياسات التجارية العالمية فيما يخص اللحوم المجمدة",
            "تأثير الظروف الاقتصادية العالمية على أسعار اللحوم",
            "أكبر الدول المصدرة للحوم في العالم",
            "ممارسات الاستدامة في صناعة اللحوم عالميًا",
            "التكنولوجيا الجديدة في إنتاج اللحوم عالميًا",
            "أحدث أخبار إنتاج الأسماك المجمدة عالميًا في",
            "اتجاهات سوق الأسماك المجمدة عالميًا",
            "أخبار سلسلة توريد الأسماك المجمدة عالميًا"
                    ]
                },
    
    "Analyze the meat and fish industry in Egypt ": {
                    "prompt": f""" Generate the following sections in [language]
        Analyze the meat and fish industry in Egypt by focusing on the following aspects:
        
        ### Consumption:
        - What are the current trends in meat and fish consumption in Egypt?
        - How do factors like population growth, changing dietary habits, and economic conditions influence demand for meat and fish?
        
        ### Production:
        - What is the current state of meat and fish production in Egypt?
        - Identify major players in the market and their contributions to the national supply of meat and fish.
        - Discuss any government initiatives or regulations that affect production, such as subsidies, trade policies, or livestock development programs.
        
        ### Exports:
        - Examine the role of the meat and fish sectors in Egypt's export economy.
        - What types of meat products and fish are being exported, and to which countries?
        - Assess the impact of foreign investment in Egypt’s meat and fish production and export sectors.
        
        ### Imports:
        - Identify key imports related to the meat and fish industry, such as animal feed, livestock, or advanced processing technologies.
        - How do import trends affect the local market for meat and fish in Egypt?
        - Discuss any challenges or barriers related to imports in the industry, such as tariffs or supply chain disruptions.
        
        Instructions:
            - Add the sources' names, not links.
            - The answer should be in [language].
            - The response should be related to the meat and fish market.
            - Don't include in your response any information related to chicken, frozen meat, frozen fish, or chicken companies.
            - Generate a table that represents this part if applicable.
            - Include numbers that represent the current situation.
            - The response should be updated after {int(current_year) - 1}.
            - No need for data before {int(current_year) - 1}.
            - Don't include a conclusion in your response.
            - If you don't have enough info about any item, don't include it in the table.
            - note that today's date is {date_string} anything beyond add it as forcasting
                    """,
                    "bing_query": [
            "إحصائيات استهلاك اللحوم في مصر",
            "إحصائيات استهلاك السمك في مصر",
            "إحصائيات إنتاج اللحوم في مصر",
            "إحصائيات إنتاج السمك في مصر",
            "إحصائيات تصدير اللحوم في مصر",
            "إحصائيات تصدير السمك في مصر",
            "إحصائيات استيراد اللحوم في مصر",
            "إحصائيات استيراد السمك في مصر"
                    ]
                },
        
    "Competitive Landscape Analysis": {
                    "prompt": f""" Generate the following sections in [language]
        
        ### Competitive Landscape Analysis: Top Meat, Frozen Meat, and Frozen Fish Companies in Egypt
        
        Instructions:
        1. Title: "تحليل التنافسية للشركات الرائدة في قطاع اللحوم واللحوم المجمدة في مصر".
        2. Table Requirements:
            - Compare major companies operating in the meat, frozen meat, and frozen fish sectors.
            these companies should be related to meat dont inlude conpanies like إسماعيلية مصر للدواجن , كوكاكولا مصر
        
        
        3. Table Format: The table should be large and clear, suitable for inclusion in a formal document.
        4. Sources: Cite the data sources by name without including direct links.
        5. Language: The table and instructions should be in **[language]**.
        6. Timeframe: Focus on data post-{int(current_year) - 1} or as recent as possible. Avoid data from before {int(current_year) - 1}.
        7-the response should be related  frozen meat  ,  meat  market and frozen fish Do not include anything else in your response like (chicken and frozen chicken)
        8-don't include in your response any information related to chicken , frozen chicken and chicken companies
        9-don't add conclusion or introduction in your response
        - note that today's date is {date_string} anything beyond add it as forcasting
            """,
                    "bing_query": [
                    "مصنع الحلواني للحوم ",
                    
                    ]
                },
        
    "SWOT Analysis": {
                    "prompt": f"""
         Generate the following sections in [language], then format them according to the required structure in the [Instructions]:
        ### (SWOT) Analysis
            Strengths, Weaknesses, Opportunities, and Threats (SWOT) Analysis for meat  , frozen meat  and  frozen fish in Egypt:
            Generate and extract the strengths, weaknesses, opportunities, and threats concerning the meat and frozen meat market in Egypt from the given data.
            Ensure that there are no contradictions.
        
        [Instructions]:
        - Generate the response as a table.
        - Add a header for this section titled 'SWOT'.
        - Include population increase in this table.
        - Illustrate the reasons for the SWOT analysis from the data in context.
        - Make sure the data is relevant to our context in the meat and frozen meat industry in Egypt.
        - Be specific, detail-oriented, and include as many details as possible.
        - Include the citation source.
        - Do not include any conclusions.
        - the response should be [language]
        -the response should be related  frozen meat  ,  meat  market and frozen fish Do not include anything else in your response like (chicken and frozen chicken)
        -don't include in your response any information related to chicken , frozen chicken and chicken companies
        -don't add notes after your response
        - note that today's date is {date_string} anything beyond add it as forcasting
               """,
                    "bing_query": None
                },
        
    
    
    "Conclusion": {
                    "prompt": f"""
        
        Generate the following sections in [language], then format them according to the required structure in the [Instructions]:
        
        Conclusion:
        Highlight the key points concerning the   meat  and frozen meat  market in Egypt and worldwide.
        Include a constructive forecast for the meat , frozen meat and frozen fish   market  after {current_year} based on the information discussed earlier in the previous prompts.
        Illustrate the reasons behind your forecast.
        [Instructions]:
            -one paragraph.
            -Detailed and focused on the main highlights.
            -Include the latest projects mentioned earlier or any explorations.
            -Include the opportunities available in the frozen meat  ,  meat  market and frozen fish .
            -don’t include any recommendations in this section
            -the response should be related  frozen meat  ,  meat  market and frozen fish Do not include anything else in your response like (chicken and frozen chicken)
            -don't include in your response any information related to chicken , frozen chicken and chicken companies
            - note that today's date is {date_string} anything beyond add it as forcasting
        
                    """,
                    "bing_query": None
                }
}
dairy_cheese_prompts = {
    'Introduction':{
            "prompt" : f"""
            Generate the following sections in [language]: 
            
            # A comprehensive analysis of the dairies and cheeses industry
            
            ### Introduction and Importance:

            -Provide an overview of the dairy and cheese industry, emphasizing its role as a primary source of nutrition in the egypt and Arab world.
            -Highlight the essential components of dairy products, such as proteins, fats, sugars, minerals, and vitamins, that make them vital to daily diets.
            -Discuss how dairy products, especially cheese, are an affordable source of animal protein and a crucial livelihood for a large portion of small-scale producers in rural and urban areas.
            -Briefly mention the size of the market, with over 1,200 companies in Egypt, an annual milk production of 5.8 million tons, and traditional cheese manufacturing accounting for 50% of production.
            -Economic and Industrial Contribution: Explain the significance of the dairy and cheese industry in Egypt’s economy, including its role in GDP, employment, and industrial development. Mention the industry’s EGP 11 billion in investments and 80,000 workers.
            -Global Positioning: Highlight Egypt’s position as the fifth-largest producer of processed cheese globally, with exports reaching $256 million in 2020, including 18,000 tons of processed cheese valued at $80 million.
            -Interdependence with Other Industries: Describe how the dairy and cheese industry is interconnected with other sectors, such as agriculture (for feed supply), retail, and logistics, contributing to economic activity and stability.
            -Future Growth: Project future trends in demand for dairy products, driven by rising incomes and population growth, with an expected per capita consumption increase of 0.4% to 21.9 kg in high-income countries by 2031, and up to 1.5% annually in middle- and low-income countries."
            
        ### Dairies and cheeses Characteristics:
            -Analyze the characteristics of the dairy and cheese industry using the following table. Discuss each characteristic, its description, and associated risks:

            | خصائص الصناعة                      | المخاطر    | الوصف                                                                                                                                                                                                                                    |
            |------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
            | هيكل التكاليف                     | منخفضة     | تتسم صناعة الالبان ومنتجاتها بنسبة رافعة تشغيلية منخفضة، حيث تمثل التكاليف المتغيرة النسبة الأكبر من تكلفة المبيعات. الصناعة ذات رافعة تشغيلية منخفضة تعتبر أقل مخاطرة ولديها القدرة على الوصول إلى نقطة التعادل بشكل أسرع.                          |
            | مدي نضوج الصناعة                 | متوسطة     | يعتبر نشاط صناعة وتجارة منتجات الالبان من الصناعات الناضجة على المستوى المحلي والدولي، مما يشير إلى وجود استقرار في الصناعة.                                                                                                                                 |
            | مدي التأثر بالدورات الاقتصادية   | منخفضة     | يعتبر نشاط صناعة وتجارة منتجات الالبان من الصناعات التي لا تتأثر بالدورات الاقتصادية، حيث إنه مرتبط إلى حد كبير بالاحتياجات اليومية للمواطنين.                                                                                          |
            | الربحية                            | متوسطة     | نتيجة انخفاض نسبة الرافعة التشغيلية، تتمتع هذه الصناعة بمستوى ربحية مستقر إلى حد ما سواء في أوقات الركود أو الانتعاش الاقتصادي. بالإضافة إلى قدرة المنتجين على تمرير أي زيادة في أسعار الخامات إلى المستهلك النهائي.                               |
            | درجة الاعتماد على العملاء والموردين | متوسطة     | • **عرض Supply Dependence**: تعتمد صناعة منتجات الالبان على السوق المحلي والخارجي وتخضع لتقلبات سعرية بناءً على قوى العرض والطلب. <br> • **طلب Demand Dependence**: تعتمد الصناعة على تجارة الجملة والتجزئة، ويرتبط الطلب بالزيادة السكانية. |
            | مدي التأثر بالمنتجات البديلة     | متوسطة     | تعتبر مخاطر التأثر بالمنتجات البديلة متوسطة لعدم وجود بدائل لمنتجات الألبان، حيث تعتبر مصادر رئيسية للبروتين. البديل الوحيد هو اللحوم، والتي تتسم بارتفاع أسعارها.                                                                          |
            | التأثر باللوائح والقرارات الحكومية | متوسطة     | تشجع الدولة صناعة وتجارة الألبان لضمان توفير الاحتياجات اليومية للمواطنين، مع فرض اشتراطات صحية صارمة.                                                                                                                                         |

            -Elaborate on how these characteristics impact the overall dynamics and sustainability of the dairy and cheese industry.

        Formatting Notes:
        - Ensure the report is well-structured, with clear headings and subheadings for each section. Include data visualization (tables or charts) where necessary to support the analysis.
        - Ensure the report is comprehensive and provides statistical information of the current state and future prospects of the contracting, construction, and building industry in Egypt. Cite sources found under each section. Do not add a conclusion.
        - Avoid hallucinating information and ensure accuracy by relying on credible sources.
        - Cite sources if found under each section.
        - note that today's date is {date_string} anything beyond add it as forcasting
            """,
            "bing_query": None,
            
               },
    'production process and stages':{
        'prompt':f"""Generate the following sections in [language]: 
        ### Production Process for dairy and cheeses
            Describe in detail the entire production process for dairies and cheeses products in Egypt, Include the following:
                -Industry stages and types of dairies and cheeses manufactures in detail.
                -highlight in detail the manufacturing stages for dairies and cheeses.
                -The stages of dairy each product collection, processing, pasteurization, and packaging in deep.
                -The role of technology and quality control measures in ensuring product safety and compliance with Egyptian and international standards.
                -Key challenges in the production process, such as supply chain issues or regulatory compliance.
                -Instructions: Ensure the description is detailed and based on factual industry standards. Reference official Egyptian guidelines and global dairy processing practices. Avoid making unsupported claims about the efficiency of the processes without data.
            
                [Important Notes:]
                -Avoid conclusions or assumptions.
                -Do not fabricate details; rely on factual information.
                -Data Extraction from Graphs/Charts: Extract relevant data from graphs or charts and present them in table format, ensuring the numbers are clearly represented.  
                - note that today's date is {date_string} anything beyond add it as forcasting
        """,
            "bing_query": ["production process for dairies and cheeses products in Egypt",
                    "cheese and dairy stages of production",
                    "dairies and cheeses manufacturing stages in Egypt and Worldwide"],
            

                                    },
        "Market updates and news":{
                "prompt" : f"""
                Generate the following sections in [language]: 

                ### Market Updates and News (Locally in Egypt and Globally)
                -provide the latest market updates and news regarding the dairy, cheese and butter industry in Egypt. Focus on:
                    -discuss the Latest Updates And Industry Developments in detail.
                    -provide the Latest prices for dairies and cheeses products (such as milk, cheeses, yughart and butter) during {current_year} compared to {int(current_year) - 1}, visualize it in A table formate to be readable.
                    -Production volume and production capacity trends through {current_year}, compared to {int(current_year) - 1}, visualize it in A table formate to be readable.
                    -Any major investments, government initiatives, or industry developments in the local in egyption's dairy market.
                    
                [Instructions]:
                    -After you fetch all these data make it detailed, to the point, highlight the statistics, numbers, reasons for each number with the illustration.
                    -Write it very detailed and highlight all the required data and separate GLOBAL AND LOCAL news.
                    -Include citation from trusted industry reports or Egyptian business news sources. Avoid using assumptions about company performance or strategies unless supported by factual data.
                    -We are in {date_string}, so the news retrieved must be near that date by not more than 1 year.
                    -Don't include any special characters in the response.
                    -The response should be adaptable to Microsoft Word [language] fonts.
                    -Make it detailed as much as possible.
                    -Get some more details or more projects.
                    -Be specific, detailed oriented and include details as much as possible.
                    -Avoid contradictions.
                    -Include the citation source from Egyptian official sources and worldwide.
                    -News especially like wars and conflicts must be in detail as long as possible.
                    -Data Extraction from Graphs/Charts: Extract relevant data from graphs or charts and present them in table format, ensuring the numbers are clearly represented.  
                    - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": [
                            " اخر اسعار الخاصة بمنتجات الالبان في مصر",
                            "اسعار منتجات الاجبان في مصر",
                            "تأثير الصراعات الإقليمية علي أسعار الأجبان والألبان في مصر ",
                            "أحدث التحديثات والمشروعات الخاصة لصناعة منتجات الألبان والأجبان في مصر",
                ],  
                            },

        'Dairies sales in Egypt':{
                "prompt" : f"""
                Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:
                #### dairies sales in Egypt till {int(current_year) + 4}:
                - Present the information in the following table format:
                
                | Indicator                 | 2021       | 2022       | 2023      | 2024      | 2025       | 2026       | 2027       | 2028       |
                |---------------------------|------------|------------|------------|------------|------------|------------|------------|------------|
                | Dairy Sales (EGPmn)  | 373,176.0  | 395,031.6  | 477,856.3  | 554,152.7  | 610,239.3  | 657,439.9  | 700,755.7  | 747,731.6  |
                | % Growth (y-o-y)*    | 5.7%       | 5.9%       | 21.0%      | 16.0%      | 10.1%      | 7.7%       | 6.6%       | 6.7%       |
                
                [INSTRUCTION]
                -put the headers in bolds and centre alignment.
                -Don't include any conclusions.
                -Avoid contradictions.
                -Include the citation source.
                - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": None,
                
            },

        "consumption, production, import, exports the current year in Egypt":{ 
                "prompt" : f"""
                Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:
            ### Market updates in Egypt consumption, production, import, exports the current year:
                -Get in detail the consumption trends and key view of dairy and cheese industry in egypt through last 3 years.
                -Get in detail the latest exports and imports regarding the dairy and cheeses the current year.
                -Get in detail the latest production values regarding the dairy and cheeses the current year.
                -Each point from the list should be pointed out as a detailed subsection, for example latest news should be as subsection, latest prices should be subsection.
            
                [Instructions]:
                    -After you fetch all these data make it detailed, to the point, highlight the statistics, numbers, reasons for each number with the illustration.
                    -Write it very detailed and highlight all the required data.
                    -Data Extraction from Graphs/Charts: Extract relevant data from graphs or charts and present them in table format, ensuring the numbers are clearly represented.  
                    -Include citation from trusted industry reports or Egyptian business news sources. Avoid using assumptions about company performance or strategies unless supported by factual data.
                    -We are in {date_string}, so the news retrieved must be near that date by not more than ONE YEAR.
                    -Don't include any special characters in the response.
                    -The response should be adaptable to Microsoft Word [language] fonts.
                    -Make it detailed as much as possible.
                    -Get some more details or more projects.
                    -Be specific, detailed oriented and include details as much as possible.
                    -Avoid contradictions.
                    -Include the citation source from Egyptian official sources and worldwide.
                    -Prices are mandatory here and not optional.
                    -News especially like wars and conflicts must be in detail as long as possible.
                    - note that today's date is {date_string} anything beyond add it as forcasting
            """,
                "bing_query": ["الاخبار العالميه و الصراعات الاقليميه المتعلقه بالتاثير علي اسعار منتجات الالبان والاجبان ",
                            "واردات مصر لمنتجات الالبان والاجبان ",
                            "تصدير مصر لمنتجات الالبان والاجبان",
                            "استهلاك مصر من منتجات الالبان والاجبان "
                    ],
                
                                                                        },
        "Market updates in World wide":{
                "prompt" : f"""
                Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:
            ### Market updates in World wide the current year:
                Generate a comprehensive overview of worldwide market updates for the dairy industry the current year. Structure the response with detailed subsections as follows:

                1. Market Updates in {int(current_year) - 1}-{current_year}:
                - Provide a summary of the latest global market trends in the dairy industry for the years {int(current_year) - 1} and {current_year}.
                - Focus on milk, cheese, and yogurt production, consumption, and pricing.

                2. Dairy Industry News {current_year}:
                - Highlight the most important news regarding the dairy industry in {current_year}, including milk, cheese, and yogurt production, pricing, and consumption.
                - Discuss major events, announcements, or regulatory changes that affected the industry during {current_year}.

                3. Consumption Trends {current_year}:
                - Provide data and analysis on global consumption of dairy products in {current_year}.
                - Include statistics related to consumption increases or decreases by region and product type.

                4. Exports and Imports {current_year}:
                - Discuss the latest global export and import figures for dairy products, focusing on key countries or regions.
                - Include statistics on trade flows, major exporters, and importers, with comparisons to previous years.

                5. Production Values {current_year}:
                - Present the latest production data for the dairy industry in {current_year}, breaking down milk, cheese, yogurt, and other dairy products.
                - Highlight countries with the highest production growth.

                6. Global Conflicts and Their Impact {current_year}:
                - Analyze how global conflicts like the Israel-Gaza war, the Russian-Ukraine war, and Red Sea conflicts have impacted the dairy industry in terms of supply chains, production costs, and pricing in {current_year}.
                - Provide detailed discussion on how these conflicts influenced global demand and availability of dairy products.

                7. Projects and Initiatives {current_year}:
                - Discuss significant global dairy industry projects and initiatives launched in {current_year}.
                - Include investments, innovation in production technology, and sustainability efforts by countries or international organizations.

                [Instructions:]
                - Each section should be detailed and data-oriented.
                - Statistics should be provided in table format where necessary.
                - Avoid generalities and focus on specific data points, trends, and facts related to the dairy industry.
                - Ensure the response is adaptable to Microsoft Word's [language] fonts.
                - Avoid including any local news for Egypt or conclusions. Focus on global trends only.
                - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": ["اخر الاخبار العالميه و الصراعات الاقليميه المؤثرة علي صناعة منتجات الالبان والاجبان  "
                            "تصدير مصر لمنتجات الالبان والاجبان",
                            "استهلاك عالميا لمنتجات الالبان والاجبان ",
                            " اخر اسعار العالميه لمنتجات الالبان والاجبان عالميا",
                            "اخر التحديثات و المشاريع والمبادرات الخاصه لصناعة منتجات الالبان والاجبان فى العالم العربي والعالم"],
                
            },
        "Competitive Landscape":{
                "prompt" : f"""
                Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:
                ### Competitive Landscape
                - Mention the competitive landscape in the Egyptian market for key players such as dina farms, juhayna, beyti, almaraai, fargallah, oubour land, arab dairy-panda, lamaar, dumty).
                - Present an overview of the competitive landscape, detailing key companies, market positions,significant local and foreign investments and partnerships for the dairy and cheese industry.
                [Instructions]:
                - Present an overview of the competitive landscape, detailing key companies, market shares of the companies, and their market positions for the construction industry.
                -Data Extraction from Graphs/Charts: Extract relevant data from graphs or charts and present them in table format, ensuring the numbers are clearly represented.  
                - Ensure sources are cited at the end.
                - Present this information in a detailed table in [language].
                -Include all the market key players with their statistics.
                -Be specific , detailed oriented and include details as much as possible.
                -Include their market shares if present in a table as numbers not percentages.
                -If not sure skip the sections.
                -Don't include any conclusions.
                - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": ["اهم اللاعبين الرئيسين في صناعة منتجات الالبان والاجبان و نسب الاستحواذ فى السوق",
                            "المصرية تستثمر 500 مليون جنيه في 3 سنوات لزيادة الإنتاج | اقتصاد الشرق مع بلومبرغ",
                            "عبور لاند تدرس ضخ 350 مليون جنيه استثمارات جديدة وزيادة صادراتها خلال  - معلومات مباشر",
                            "شركات تسيطر على سوق صناعة الألبان فى مصر.. تعرف على التفاصيل ",
                            "https://almalnews.com/%d8%a2%d8%b1%d8%a7%d8%a8-%d8%af%d9%8a%d8%b1%d9%8a-%d8%a8%d8%a7%d9%86%d8%af%d8%a7-%d8%aa%d9%82%d8%b1%d8%b1-%d8%b4%d8%b1%d8%a7%d8%a1-10-%d9%85%d9%84%d8%a7%d9%8a%d9%8a%d9%86-%d8%b3%d9%87/",
                        ],
                
            },
                    
        "Bank internal Market Research":{
                    "prompt" : f"""
                    Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:
                    ### Bank internal Market Research Department Industry Report:
                    Generate a professional financial performance table for Dairy and Snacks companies under the headline:
                    #### Dairy companies are expected to report healthy earnings despite the recent drop in prices

                    | Company                             | EBITDA Margin (%) | NPM (%) | ROE (%) | ROA (%) | Current Ratio | Fin. Leverage (Debt/Equity) | OCF (EGP Mn) | FCF (EGP Mn) | FCF/OCF | Revenue (EGP Mn) | YoY Revenue (%) | Net Income (EGP Mn) | YoY Net Income (%) | Total Assets (EGP Mn) | Total Liabilities (EGP Mn) |
                    |-------------------------------------|------------------|---------|---------|---------|---------------|-----------------------------|--------------|--------------|---------|------------------|-----------------|---------------------|-------------------|------------------------|---------------------------|
                    | Arab Dairy Products Company         | 15.1             | 7.1     | 43.0    | 10.5    | 1.34          | 3.42                        | 168.5        | 93.89        | 0.91    | 917.4            | 95              | 64.83               | 193.37            | 1,827.8                | 1,293.1                   |
                    | Arabian Food Industries Company     | 11.6             | 6.7     | 33.4    | 11.5    | 1.28          | 3.01                        | 145.6        | -            | -       | 2,282.2          | 31              | 153.3               | 1.29              | 4,375.3                | 2,921.0                   |
                    | Obour Land for Food Industries      | 17.3             | 9.0     | 49.9    | 18.1    | 1.32          | 2.76                        | 124.3        | -            | -       | 1,750.0          | 19              | 157.0               | 36.35             | 3,287.4                | 2,004.6                   |
                    | Juhayna Food Industries             | 24.5             | 8.3     | 28.6    | 13.3    | 1.15          | 2.15                        | 49.1         | 112.4        | -       | 5,758.3          | 68              | 478.7               | 41.05             | 10,077                 | 5,708.0                   |
                    | **Dairy Average**                   | **17.1**         | **7.8** | **38.7**| **13.3**| **1.27**      | **2.83**                    | **121.9**    | **-**        | **-**   | **2,677.0**      | **53**          | **213.5**           | **68.01**          | **4,892**               | **2,981.7**               |

                    [Instructions]:
                    your role is a risk manager who works in credit approvals in banking sector , do the following:
                        -Generate the tables given in the response IN A GOOD manner alignment and format.
                        -set the headers in bold and centre alignment.
                        -Comment on the table in [language] and be spacefic .
                        -Make sure the indexes are in bold and centred allignment.
                        -Don't include any conclusions.
                        -Include the citation source here it's market research by Banque misr team.
                        - note that today's date is {date_string} anything beyond add it as forcasting
                        - generate the table columns as rows and rows as columns
                """,
                "bing_query":None,
                
                                        },
        
        "SWOT analysis":{
                "prompt" : f"""
                Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

        ### SWOT analysis:
                -Generate and Extract Strengths , weakness , opportuinties and threats concerning OF the dairies and cheeses Market in Egypt from the Given Data.
                -Make sure there's no contradictions.

                [Instructions]:
                    -Generate the response as a matrix table.
                    -Illustrate the reasons for the swot analysis from the data in context.
                    -Make sure the data is relevant to our context Dairies industry in Egypt.
                    -Be specific , detailed oriented and include details as much as possible.
                    -Don't include any conclusions.
                    -Include the citation source.
                    - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": None,
                
                        },
        "Industry Forecast":{
                "prompt" : f"""
                Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:
            Industry Forecast:
                -provide the Structural Trends of dairy and cheese Spending Outlook For {current_year} & {int(current_year) + 1}.
                -HIGHLIGHT  any statistical trends and key view of Structural Trends of dairy and cheese 
            ### Economic Conditions:
                -Detailed Discussion: Provide an in-depth discussion of Egypt's current economic conditions impacting the construction sector, including:
                    -Tax Regime and Incentives: Outline Egypt's tax policies, incentives, and regulations in the construction industry, highlighting any recent changes and their impact on the sector.
                    -Global Dependency and Egypt’s Economic Concerns: Discuss four key issues Egypt faces due to global dependencies:
                        -International market fluctuations
                        -Trade dependencies
                        -Currency exchange rate impacts
                        -Economic stability concerns
                        -POLITICAL concerns including wars...etc.
                -Source Citation: Cite all sources directly under each section.
                - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": None,
                
                            },
        "conclusion":{
                "prompt" : f"""
                Generate the following sections in [language] language then format them according to the required structure in the [Instructions]:

            ### Conclusion:
                    -Highligh the main highlights and statistical concerning of the dairy Market in Egypt and worldwide
                    -Include a constructive forecast regarding the dairies industrys after the current year based on the information you knew earlier from the previous prompts.
                    -Illustrate your forecasts reasons.

                    [Instructions]:
                        -2 paragraph.
                        -Detailed and focusing on the main highlights.
                        -Include latest projects mentioned earlier or explorations.
                        -Include the Oppourtuinties for it.
                        - note that today's date is {date_string} anything beyond add it as forcasting
                """,
                "bing_query": None,
                
                    },
}
textiles_prompts = {
    "Introduction":{
         "prompt" : f"""Generate the following in [language]:
        # Comperhensive analysis on the Spinning and weaving industry
        
        summarizre the following:
       
        ## Industry Overview:
        use the following to create introduction about the textiles industry:
             Textile and Garment Industry
            The textile and ready-made garment sector is the only vertically integrated industrial sector in Egypt in the Middle East, where the journey of final textile products begins with the cultivation of the finest Egyptian cotton known for its quality worldwide, through the production of yarn, dyeing, finishing, printing, then knitting, packaging and final packaging of the product with high quality that competes with global products, which has placed Egypt among the 60 largest exporting countries of textiles and clothing in the world. The sector includes a number of sub-sectors: spinning, fabrics, ready-made garments and home textiles. The ready-made garments sub-sector represents more than 70% of the entire sector in Egypt, and provides more than 20% of job opportunities in the Egyptian labor market. The textile industry is one of the important sectors in the Egyptian economy, employing approximately 20% of the industrial workforce in Egypt, and representing 16% of industrial exports.

            Spinning and weaving:
            The number of factories operating in the sector reached 11,000

            Ready-made garments:
            Ready-made garments represent 70% of the total sector, and provide 20% of the job opportunities provided by the textile sector. The number of factories operating in ready-made garments reached 3,169

            Home furnishings:
            The number of factories operating in the sector reached 853.

            #### First: Natural raw materials
                1. **Cotton**: It is used in many products such as clothing, upholstery fabrics, ropes, and knitting threads. It is characterized by its durability and resistance to tearing.
                2. **Wool**: The second natural raw material after cotton, and is characterized by its ability to maintain body heat. It includes types of wool such as merino wool, cross-bred, and carpet wool.
                3. **Linen**: It is characterized by its durability and is used in shoelaces, fishing nets, and bookbinding.
                
            #### Second: Synthetic raw materials
                - **Synthetic fibers**: They are manufactured chemically and are considered a modern innovation in the field of textiles. They include fibers such as polyester, polyacrylic, and polyamide. These fibers help meet the increasing demand for textile materials due to the increase in population.
                
            #### Technological processes in textile industries
                1. **Spinning processes**: include stages such as ginning, carding, carding, twisting, and spinning to convert fibers into yarns.
                2. **Weaving processes**: converting yarns into textiles through processes such as weaving and knitting.
                3. **Dyeing and finishing processes**: include stages such as lint firing, bleaching, dyeing, printing, and special finishing such as moth resistance or adding luster to the fabric.
                
            #### Dyeing and finishing:
                    Dyeing and finishing include many processes that aim to prepare fabrics or threads to obtain the desired color and improve the properties of the fabric. These processes include:
                    
                    1. **Pile burning**: Burning the hairs protruding on the surface of the fabric using a flame.
                    2. **De-brushing and washing**: Cleaning the raw threads using chemicals such as acids or hot water.
                    3. **Bleaching**: Bleaching natural fibers using materials such as hydrogen peroxide.
                    4. **Mercerization**: Improving the luster of cotton fabric and increasing its durability.
                    5. **Dyeing**: Giving the fabric a color using dye materials. This process is one of the main sources of pollution in the textile industry.
                    6. **Printing**: Printing colors and drawings on fabrics using dyes and adhesives.
                    7. **Carbonization**: Removal of cellulosic plant materials from wool fibers using sulfuric acid.
                    8. **Special equipment**: Imparting special properties to fabrics such as resistance to moths or water factors.
                    9. **Topping and shaving the surface of the fabric**: Mechanical preparation to change the appearance of the fabric and make it softer.
                    10. **Softening the fabric with a calender**: Passing the fabric between metal rollers to remove surface hairs and soften the texture of the fabric.
                    11. **Adding a shine to the fabric**: Passing the fabric between metal rollers to add a surface shine.
                    
            #### Stages of industrial processes:
                    1. **General inputs**: The process starts with multiple inputs such as raw materials.
                    2. **Traditional and reactive dyeing**: Fabrics go through traditional or reactive dyeing processes.
                    3. **Final finishing**: Preparing the fabrics to obtain the final shape.
                    4. **Printing and customization machines**: Fabrics are customized using special printing machines.
                    5. **Color Coordination**: Color coordination is done to ensure uniformity of color in the final product.
                    6. **Final Finishing and Quality Control**: These final stages include the quality control process to ensure that the fabrics meet the required specifications.
                    7. **Packaging**: After all the processes are completed, the finished fabrics are packaged.
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting           
            - if there are no information provided for an item in the section do not generate it
        """,
        "bing_query":None
    },  
    "Market Updates in Egypt":{
        "prompt" : f"""Generate the following in [language]:
        ### Market Updates and Latest News in Egypt related to textiles industry in {current_year} 
            - add paragraph for every unique news in the context
            - and add to the previous news these articles: (**With half a billion dollars.. Jiangsu Lianfa Textile Co. Ltd. seeks to establish a spinning complex in Egypt**),(**Industry: $2.4 billion in Egyptian ready-made garment exports in {int(current_year) - 1}**),(**12 facts about developing spinning and weaving factories at a cost of 50 billion pounds** "create this one as a paragraph not as points")
        ### Sources
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

        Instructions:
            - make sure you add all the news articles realated to the Spinning and weaving industry 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it""",
        "bing_query":["اخر اخبار صناعه المنسوجات في مصر","واردات مصر من المنسوجات",
        " صادرات مصر من المنسوجات",
        "واردات مصر من آلات الحلج والنسيج",
        "مصانع الغزل و النسيج في مصر",
        "استهلاك مصر من الغزل والنسيج",
        "اسعار الغزل و النسيج في مصر",
        "انتاج مصر من الغزل و النسيج",
        "احصائيات صناعة الغزل والنسيج في مصر",
        "https://cnnbusinessarabic.com/retail/74555/%D8%A8%D9%86%D8%B5%D9%81-%D9%85%D9%84%D9%8A%D8%A7%D8%B1-%D8%AF%D9%88%D9%84%D8%A7%D8%B1-%D8%B4%D8%B1%D9%83%D8%A9-%D8%B5%D9%8A%D9%86%D9%8A%D8%A9-%D8%AA%D8%A8%D8%AD%D8%AB-%D8%A5%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D8%AC%D9%85%D8%B9-%D9%84%D9%84%D8%BA%D8%B2%D9%84-%D9%81%D9%8A-%D9%85%D8%B5%D8%B1",
        "https://gate.ahram.org.eg/News/4696329.aspx#:~:text=%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-,%D8%A7%D9%84%D8%B5%D9%86%D8%A7%D8%B9%D8%A9:%202.4%20%D9%85%D9%84%D9%8A%D8%A7%D8%B1%20%D8%AF%D9%88%D9%84%D8%A7%D8%B1%20%D8%B5%D8%A7%D8%AF%D8%B1%D8%A7%D8%AA%20%D9%85%D8%B5%D8%B1,%D8%A7%D9%84%D9%85%D9%84%D8%A7%D8%A8%D8%B3%20%D8%A7%D9%84%D8%AC%D8%A7%D9%87%D8%B2%D8%A9%20%D8%AE%D9%84%D8%A7%D9%84%20{int(current_year) - 1}%20%7C%20%D9%81%D9%8A%D8%AF%D9%8A%D9%88&text=%D9%83%D8%B4%D9%81%20%D8%AA%D9%82%D8%B1%D9%8A%D8%B1%20%D8%B5%D8%AF%D8%B1%20%D8%B9%D9%86%20%D8%A7%D9%84%D9%87%D9%8A%D8%A6%D8%A9,2%20%D9%85%D9%84%D9%8A%D8%A7%D8%B1%20%D9%88433%20%D9%85%D9%84%D9%8A%D9%88%D9%86%20%D8%AF%D9%88%D9%84%D8%A7%D8%B1.",
        "https://www.youm7.com/story/2024/7/11/12-%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A9-%D8%AD%D9%88%D9%84-%D8%AA%D8%B7%D9%88%D9%8A%D8%B1-%D9%85%D8%B5%D8%A7%D9%86%D8%B9-%D8%A7%D9%84%D8%BA%D8%B2%D9%84-%D9%88%D8%A7%D9%84%D9%86%D8%B3%D9%8A%D8%AC-%D8%A8%D8%AA%D9%83%D9%84%D9%81%D8%A9-50-%D9%85%D9%84%D9%8A%D8%A7%D8%B1/6634787",
        "https://www.almasryalyoum.com/news/details/3235166"
        ]
    },
    "Market Updates Globally":{
        "prompt" : f"""Generate the following in [language]:
            ### Market Updates and Latest News Globally related to textiles industry in {current_year}

            
           use the provided context to talk about this in another paragraph 
                • Free Trade Agreements: In addition to the free trade agreements with the European Union, COMESA (Common Market for Eastern and Southern Africa) and the Arab world, the Qualified Industrial Zones (QIZ) agreement between Egypt, Israel and the United States of America gives local companies the right to enter the American markets without customs duties or quotas, provided that 35% of the goods are manufactured in the qualified industrial zones and that at least 10.5% of the production is from Israeli inputs.
                • Textile industrial clusters in Egypt: With the development of the free zone systems and the QIZ agreement, the textile industry began to cluster in the following three main areas:
                1- The Canal Zone: It includes the Suez Canal cities from Port Said to Ismailia. This area invests in jeans products and imports of thick cotton yarn. The Suez Canal facilitates the passage of exports to Europe via the Mediterranean Sea and to Asia via the Red Sea.
                2- Alexandria Area: A number of ready-made garment companies have opened their own outlets in Borg El Arab and El Ameria, including many Turkish companies, where their exports are carried out through the port of Alexandria.
                3- Greater Cairo: Many industrial centers were established in 6th of October City, Obour City, and 10th of October City.


        ### Sources
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].

        Instructions: 
            - make a paragraph for every country or region 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it""",
        "bing_query":["Latest news on the textile industry in Global",
         "اتفاقية الكويز بين مصر وإسرائيل والولايات المتحدة وتأثيرها على صناعة النسيج",
                    "اتفاقية الكوميسا وأثرها على صناعة النسيج في مصر",
                    "تطور صناعة النسيج في منطقة قناة السويس",
                    "اتفاقيات التجارة الحرة بين مصر والاتحاد الأوروبي والدول العربية",
                    "مصانع الملابس الجاهزة في الإسكندرية والتصدير إلى أوروبا",
                    "صناعة النسيج في مصر بمنطقة القاهرة الكبرى ومدينة السادس من أكتوبر",
                    "تأثير اتفاقية الكويز على صادرات الملابس المصرية",
                    "دور قناة السويس في صادرات النسيج والملابس المصرية",
                    "الشركات التركية في صناعة النسيج بالإسكندرية",
                    "المناطق الصناعية في مصر لصناعة النسيج والملابس"]
    },
    "Competitor Analysis":{
            "prompt" : f"""Generate the following in [language]:
            ### Main key players in the textiles market
                Create a table for the following
                    Oriental Weavers for Carpets or النساجون الشرقيون
                        1979	Oriental Weavers for Carpets is part of the Orientals Group (17 companies), a leading industrial conglomerate in Egypt.

                    Giza spinning and weaving S.A.E. or الجيزة للغزل والنسيج
                        1979	Producer of all kinds of casual dress. Exporter of garments to USA, Canada and Germany, Hometextile to Germany, France, Ireland and USA.

                    Lotus Garments Company
                        1994	Lotus Garment Group is a clothing manufacturer and exporter. Specialising in the production of denim, the group provides around 16 million jeans.

                    AlHesn Textiles
                        1898	Hesni Textiles was established over a century ago by Noaman Hesni. It processes over 8,000 tons of knitted fabrics and 1,300 tons of yarn annually.

                    Kazareen Textile Company
                        1991	Kazareen Textile Company, a member of Mimar Invest Group is a leading global textile , apparel & fashion services company

                    MAC Carpet Egypt
                        1980	Producer and exporter of printed and tufted rugs, mats and WTW.

                    Misr Spinning Weaving Co.
                        1927	Misr Spinning and Weaving Company also known as Misr Helwan or the El-Ghazl factory, is a publicly owned textile company in El-Mahalla El-Kubra.

                    Al Arafa for Investment and Consultancies
                        1907	Arafa group is one of the largest privately owned groups in the textiles and garments field in Egypt.

                    El Nasr Clothing & Textile Co Kabo
                        1940	Engaged in the manufacturing of underwear for men, women and children; owns factory that develops, produces finished garments.

                    Nile Linen Group
                        1996	Nile Linen Group is one of the fastest-growing global conglomerates in Egypt with business in home textile products
                    
                    Alexandria Spinning & Weaving Co.     
                        1947    About the Company The company - Alexandria Spinning and Weaving Company. Spinalex Company, an Egyptian joint stock company, was established in 1947. It became one of the largest commercial spinning companies in Egypt and was subject to abbreviated laws in 1961 and was affiliated with the Egyptian General Organization for Spinning and Weaving until it was proven to the company that it was affiliated with the Commercial Textiles Company (S.A.E.C.M.M) on December 26, 1992, with an additional part 203 of Resolution 1991 and its executive regulations. Within the framework of the government’s program to expand the ownership base of public business sector companies, the holding company sold its entire share in the capital.    
                    
                    Dice Sport & Casual Wear
                        1989   Dice Sports & Casual Wear PLC is a leading vertically integrated ready made garments Manufacturer. Based on a culture of speed and agility, Dice provides integrated solutions to global brands. Through 15 Manufacturing sites Dice is home to 13,000 workers and undertakes processes including Knitting, Dyeing, AOP, Accesories, Screen Printing & Embroidery, Washing, Cutting and Sewing. With a presence of 358 stores across Egypt, Dice has also diversified in to Retail through its home-grown brand, Dice Underwear.

                    Arab and polvara spinning and weaving
                        1981   The Arab and Volvara Spinning and Weaving Company was established in the Arab Republic of Egypt to provide for the provisions of the Companies Law immediately and clearly with shares and six limited importance issued by Law No. 159 Final 1981 and its executive regulations with the operation of Law 95 Final 1992 and its executive regulations. In light of the General Authority for Free Investment No. 3485 of 2001 to merge the Arab and United Company and Volvara Spinning, Weaving and Silks (Unirab) LLC with Unirab International Marketing LLC, a new company was decided under the name of the Arab and Volvara Spinning and Weaving LLC and the contract and articles of association approved by the wonderful companies that were established on 12/31/2001 as a basis for calculating the value of the assets and liabilities of the two merged companies. The company registered in the commercial register under No. 8185 dated 2/10/2002 Alexandria.

        Instructions: 
            - do not add conclutions   
            - note that today's date is {date_string} anything beyond add it as forcasting       
                    """,
            "bing_query":None
    },
    "Competitor Analysis 2":{
            "prompt" : f"""Generate the following in [language]:
           
        ### Key players news and updates in the textiles market {current_year}:
            create a table column for company name and column for the company news:
        ### Sources
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it
            
                    """,
            "bing_query":[
                "اخبار النساجون الشرقيون",
                "اخبار شركة الجيزة للغزل والنسيج",
                "اخبار شركة ملابس اللوتس",
                "اخبار شركة Hesni Textiles",
                "اخبار شركة كازارين للنسيج",
                "اخبار شركة ماك كاربت مصر",
                "اخبار شركة مصر للغزل والنسيج",
                "اخبار شركة العرفة للاستثمار والاستشارات",
                "اخبار شركة النصر للملابس والمنسوجات كابو",
                "اخبار مجموعة النيل للكتان",
                "اخبار شركات المنسوجات في مصر ",
                "اخبار العربية وبولفارا للغزل والنسيج",
                "اخبار دايس للملابس الرياضية والكاجوال",
                "اخبار الاسكندرية للغزل و النسيج",
                "اخبار شركات الغزل و النسيج"
            ]
    },
    "BM market research":{
        "prompt" : f"""Generate the following in [language]:
        ### The most important points mentioned in our bank’s market management report on the textiles industry, July {current_year}

        Create table in md format
        1Q24 figures	EBITDA Margin	NPM	ROE	ROA	Current Ratio	Fin. Lev.	Debt /Equity	OCF (EGP Mn)	FCF (EGP Mn)	FCF/OCF	Revenue (EGP Mn)	% 4 y-o-y	Net income (EGP Mn)	% 4 y-o-y	Total assets (EGP Mn)	Total liab. (EGP Mn)
        Arab and Polvara Spinning and Weaving	-17%	-11%	-4%	-10%	0.4	2.5	4%	0.5	0.3	70%	25	85%	-3	-9%	362	215
        Dice Sports and Casual Wear	22%	12%	19%	78%	1.1	4.5	256%	-458	-558	-120%	993	44%%	119	635%	3,776	2,932
        Alexandria Spinning & Weaving	-8%	18%	13%	17%	2.5	-	24%	-102	-96	90%	163	74%	29	-47%	1,095	324
        Average	-0.90%	6%	9%	28%	1.4	3.5	95%	-186	-218	13%	394	68%	49	310%	1,744	1,157

        ### Insights about the table
    
        - Add the source name: Banque misr market research for july {current_year}
        - note that today's date is {date_string} anything beyond add it as forcasting
        - generate the table columns as rows and rows as columns
        """,
        "bing_query":None
    },
    "Regulatory framework & Antidumping laws":{
        "prompt" : f"""Generate the following in [language]:
        ### Regulatory framework & Antidumping laws
            - Write the most important regulations in egypt regarding the textiles industry
        

        ### Sources
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
        Instructions: 
            - do not add conclutions
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it 
        """,
        "bing_query":["قوانين المنسوجات","قوانين مكافحة الإغراق"]   
    },
    "SWOT Analysis and conclution":{
        "prompt" : f"""Generate the following in [language]:
            ### SWOT Analysis on Textiles industry:
                - Create a table for SWOT analysis of the Textiles industry, identifying strengths, weaknesses, opportunities, and threats.
                    - the items in strengths and weaknesses should be internal parameters in egypt and items in opportunities and threats should be external parameters

            ### Conclusion:
                - Provide a comprehensive conclusion on industry trends (growing or not) for credit decision reviewers with showing some statistics and make it a bit longer.
                - any numbers you mention should be in {current_year}

            ### Sources
            - Add the sources as a domain name not the whole url like this [domain-name.top-level-domain].
            
            Instructions: 
            - note that today's date is {date_string} anything beyond add it as forcasting
            
            - if there are no information provided for an item in the section do not generate it 
        """,
        "bing_query":["قوانين المنسوجات ","قوانين مكافحة الإغراق","اخبار شركات المنسوجات في مصر","اخر اخبار صناعه المنسوجات في مصر","واردات مصر من المنسوجات","صادرات مصر من المنسوجات"]  
    }
}
