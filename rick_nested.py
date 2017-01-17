import yaml

over = yaml.load(open('customerFullStatusMoreOverTime.yaml','r'))

purchase = yaml.load(open('customerMoreQuarterProductDictOverTime.yaml','r'))

customerProductAnalysis = {}

for mar_code in over.keys():
    for age_bracket in over[mar_code].keys():
        for resident in over[mar_code][age_bracket].keys():
            for keys in over[mar_code][age_bracket][resident].keys():
                for house_id in over[mar_code][age_bracket][resident][keys].keys():
                    if len(over[mar_code][age_bracket][resident][keys][house_id])>=2:
                        for _id in over[mar_code][age_bracket][resident][keys][house_id]:
                           customerProductAnalysis[_id] = purchase[_id]
                           
file_object = open('customerProductAnalysis.yaml','w+')
file_object.write(yaml.dump(customerProductAnalysis,default_flow_style=False))
                           
            
