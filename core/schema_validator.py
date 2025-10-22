import jsonschema
import json



class SchemaValidator:
    @staticmethod
    def schema_validator(response_json, schema_path):
        with open(schema_path, 'r') as file:
            schema = json.load(file)
        
        jsonschema.validate(instance= response_json, schema = schema)
