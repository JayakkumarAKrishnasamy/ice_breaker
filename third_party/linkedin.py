import os
from urllib.parse import urlparse
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Function to scrape linkedin profile given an URL"""
    profile_url = urlparse(linkedin_profile_url)
    response = requests.get(profile_url.geturl())
    if response.status_code == 200:
        return response.json()
    else:
        return None

def scrape_linkedin_profiles(linkedin_profile_urls: list):
    """Function to scrape linkedin profiles given a list of URLs"""
    profiles = []
    for profile_url in linkedin_profile_urls:
        profile = scrape_linkedin_profile(profile_url)
        if profile:
            profiles.append(profile)
    return profiles

if __name__ == "__main__":
    linkedin_profile_urls = [
        "https://www.linkedin.com/in/joseph-m-garcia/"
    ]
    profiles = scrape_linkedin_profiles(linkedin_profile_urls)
    if profiles:
        print(profiles)
        print(type(profiles))
        print(type(profiles[0]))
        print(type(profiles[0]["publicProfileUrl"]))
    else:
        print("Error scraping profiles.")
