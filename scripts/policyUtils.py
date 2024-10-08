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

def get_basePolicy_id(policyRoot):
    base_policy_tag = policyRoot.findall(f".//{schema}PolicyId")
    assert len(base_policy_tag) <= 1, "More than one base policy tag found!"
    if len(base_policy_tag) == 1:
        return base_policy_tag[0].text
    return None

if __name__ == "__main__":
    print(
        is_RP_file(parse_policy("customEmail/basePolicy.xml"))
    )