import yaml
import os

def load_config(env='dev'):
    with open(f"../config/{env}.yaml", 'r') as file:
        return yaml.safe_load(file)
        