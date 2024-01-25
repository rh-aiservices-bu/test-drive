import yaml

def namespace_specific_yaml(username):
    with open("7_raytest_template.yaml", "r") as stream:
        try:
            yaml_info = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            
    yaml_info["metadata"]["namespace"]=username
    yaml_info["spec"]["resources"]["GenericItems"][0]["generictemplate"]["metadata"]["namespace"]=username
    yaml_info["spec"]["resources"]["GenericItems"][1]["generictemplate"]["metadata"]["namespace"]=username
    yaml_info["spec"]["resources"]["GenericItems"][1]["generictemplate"]["spec"]["rules"][0]["host"]=f'raytest-head-svc.{username}.svc.cluster.local'
    
    print(yaml_info)
    
    with open('raytest.yaml', 'w') as outfile:
        yaml.dump(yaml_info, outfile, default_flow_style=False)