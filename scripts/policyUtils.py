import os
import xml.etree.ElementTree as ET

def get_policy_paths(folder: str):
    result = []
    for path in os.listdir(folder):
        if path.endswith(".xml"):
            result.append(os.path.join(folder, path))
    return result

def parse_policy(policy_path: str):
    tree = ET.parse(policy_path)
    root = tree.getroot()
    return root

def getId(policyRoot):
    return policyRoot.attrib['PolicyId']

if __name__ == "__main__":
    print(
        getId(parse_policy("customEmail/basePolicy.xml"))
    )