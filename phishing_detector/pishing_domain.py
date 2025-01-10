import requests
import json

# Fetch phishing domains from AlienVault OTX.
def fetch_phishing_domains_from_otx(api_key, indicator="domain"):
    """
    Fetch phishing domains from AlienVault OTX.
    Args:
        api_key (str): Your AlienVault OTX API key.
        indicator (str): The type of indicator to query (e.g., 'domain').
    Returns:
        list: List of domains flagged as phishing or malicious.
    """
    url = f"https://otx.alienvault.com/api/v1/pulses/subscribed"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            domains = []
            for pulse in data.get('results', []):
                for ind in pulse.get('indicators', []):
                    if ind.get('type') == indicator:
                        domains.append(ind.get('indicator'))
            return domains
        else:
            print(f"Error fetching data: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_domains_to_file(domains, filename="alienvault_phishing_domains.json"):
    """
    Save phishing domains to a local JSON file.
    Args:
        domains (list): List of domains to save.
        filename (str): File path to save the data.
    """
    with open(filename, "w") as f:
        json.dump(domains, f)
        print(f"Saved {len(domains)} domains to {filename}")