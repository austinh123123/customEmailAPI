import argparse
import requests as r
import json
import os
import policyUtils


def get_token(tenant: str, clientId: str, clientSecret: str, **kwargs):
    auth_data = {
        "client_id": clientId,
        "client_secret": clientSecret,
        "scope": ".default",
        "grant_type": "client_credentials"
    }
    resp = r.post(
        f'https://login.microsoft.com/{tenant}/oauth2/v2.0/token',
        data=auth_data
    )
    return resp.json()["access_token"]


def upload_endpoint(id):
    return f"https://graph.microsoft.com/beta/trustFramework/policies/{id}/$value"


def upload(policy_id: str, policy_text: str, token:str):
    endpoint = upload_endpoint(policy_id)
    headers = {
        "Content-Type": f"xml; charset=utf-8",
        "Authorization": f"Bearer {token}"
    }
    resp = r.put(
        endpoint,
        policy_text.encode('utf-8'),
        headers=headers,
    )
    return resp.text

def run_now_url(policyId: str):
    """This is hard-coded to use the grit dev tenant"""
    return f"https://gpdevb2c.b2clogin.com/gpdevb2c.onmicrosoft.com/oauth2/v2.0/authorize?p={policyId}&client_id=980626d3-2efc-402c-9335-f05c32d94ff8&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fjwt.ms&scope=openid&response_type=id_token&prompt=login"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="IEF Policy Deployment",
        description="Deploys IEF policies to B2C tenant"
    )
    parser.add_argument("tenant")
    parser.add_argument("policyFolder")
    args = parser.parse_args()
    with open(args.tenant, "r") as f: 
        token_info = json.loads(f.read())


    token = get_token(**token_info)
    for policy in policyUtils.get_policy_paths(args.policyFolder):
        with open(policy, "r") as f:
            try:  
                root = policyUtils.parse_policy(policy)
                id = policyUtils.getId(root)
                upload(id, f.read(), token)
                print(f"Uploaded policy {id} to {token_info['tenant']}")
                if policyUtils.is_RP_file(root):
                    print(f"Run now link: {run_now_url(id)}")
            except:
                print(f"Could not parse file: {policy}, skipping upload")