# import requests
import validators
import re
import os
import json
from dotenv import load_dotenv
from .pishing_domain import fetch_phishing_domains_from_otx, save_domains_to_file

# Load the API key from the environment variable
load_dotenv("/Users/shawn47/Documents/Python_Projects/.env")
API_KEY = os.getenv("my_apikey_OTX")

# Fetch phishing domains and save to file
phishing_domains = fetch_phishing_domains_from_otx(API_KEY)
if phishing_domains:
    save_domains_to_file(phishing_domains)
else:
    print("No phishing domains found.")

# Load phishing domains from file
with open("alienvault_phishing_domains.json", "r") as f:
    phishing_domains = json.load(f)

def is_url_valid(link):
    return validators.url(link)

def is_ip_in_url(link):
    ip_pattern = re.compile(r'http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
    return bool(ip_pattern.search(link))

def is_url_length_suspicious(link):
    return len(link) > 75

def has_suspicious_characters(link):
    suspicious_chars = ['@', '-', '_', '%', '?', '&', '=']
    return any(char in link for char in suspicious_chars)

def is_known_phishing_domain(link):
    domain = re.findall(r'http[s]?://([^/]+)', link)
    if domain:
        domain = domain[0]
        return domain in phishing_domains
    return False


# List of known disposable email providers
disposable_email_providers = [
    "mailinator.com", "10minutemail.com", "guerrillamail.com", "maildrop.cc", "tempmail.com"
]

def is_email_valid(email):
    return validators.email(email)

def email_has_suspicious_characters(email):
    suspicious_chars = ['@', '-', '_', '%', '?', '&', '=']
    return any(char in email for char in suspicious_chars)

def is_disposable_email(email):
    domain = email.split('@')[-1]
    return domain in disposable_email_providers

def is_known_phishing_domain_email(email):
    domain = email.split('@')[-1]
    return domain in phishing_domains

def analyze_email(email):
    if not is_email_valid(email):
        return f"{email} is invalid."

    if has_suspicious_characters(email):
        return f"email: {email}  'status' Suspicious (Suspicious characters)"

    if is_disposable_email(email):
        return f"email: {email}  'status' Suspicious (Disposable email provider)"

    if is_known_phishing_domain(email):
        return f"email: {email}  'status' Suspicious (Known phishing domain)"

    return f"email: {email}  'status' Safe"

def analyze_url(message):
    if not is_url_valid(message):
        return f"{message} is invalid."

    if is_ip_in_url(message):
        return f"url: {message}  'status' Suspicious (IP address in URL)"

    if is_url_length_suspicious(message):
        return f"url: {message}  'status' Suspicious (URL length)"

    if has_suspicious_characters(message):
        return f"url: {message}  'status' Suspicious (Suspicious characters)"

    if is_known_phishing_domain(message):
        return f"url: {message}  'status' Suspicious (Known phishing domain)"

    if 'login' in message or 'secure' in message:
        return f"url: {message}  'status' Suspicious (Contains 'login' or 'secure')"

    return f"url: {message}  'status' Safe"

# Example usage
if __name__ == "__main__":
    test_urls = [
        "http://example.com",
        "http://192.168.0.1",
        "http://phishing-site.com",
        "http://very-long-url-example.com/" + "a" * 76,
        "http://suspicious-url.com?param=value&other=param",
        "http://secure-login.com",
        "http://google.com"
    ]

    for url in test_urls:
        print(analyze_url(url))