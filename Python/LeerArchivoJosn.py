# Importamos JSON 
import json
 
with open('BD_GEPP.json', 'r') as f:
    array = json.load(f)
 
    # Le cambio a comillas dobles 
    formatearjson = json.dumps(array)
 
print (array)