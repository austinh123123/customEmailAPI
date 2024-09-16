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
    print(headers)
    resp = r.put(
        endpoint,
        policy_text.encode('utf-8'),
        headers=headers,
    )
    return resp.text


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
            id = policyUtils.getId(policyUtils.parse_policy(policy))
            print(upload(id, f.read(), token))