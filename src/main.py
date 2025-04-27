import yaml 
 
with open("config/config.yml", "r") as f: 
    config = yaml.safe_load(f) 


print(config["data"]["raw_path"]) 
