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
schema = "{http://schemas.microsoft.com/online/cpim/schemas/2013/06}"
def is_RP_file(policyRoot):
    return len(policyRoot.findall(f".//{schema}RelyingParty")) > 0

def getId(policyRoot):
    return policyRoot.attrib['PolicyId']

if __name__ == "__main__":
    print(
        is_RP_file(parse_policy("customEmail/basePolicy.xml"))
    )