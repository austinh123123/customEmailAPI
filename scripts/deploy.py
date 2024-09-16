import argparse
import requests as r


def get_token(tenant: str, client_id: str, client_secret: str):
    auth_data = {
        "client_id": client_id,
        "client_secret": client_secret,
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


def upload(policy_id: str, policy_text: str):
    endpoint = upload_endpoint(policy_id)
    r.put(endpoint,)


if __name__ == "__main__":
    argparse.ArgumentParser(
        prog="IEF Policy Deployment",
        description="Deploys IEF policies to B2C tenant"
    )
