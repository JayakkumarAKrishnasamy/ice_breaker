import os
from urllib.parse import urlparse
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Function to scrape linkedin profile given an URL"""
    profile_url = urlparse(linkedin_profile_url)
    return requests.get(profile_url.geturl()).json()

def scrape_linkedin_profiles(linkedin_profile_urls: list):
    """Function to scrape linkedin profiles given a list of URLs"""
    profiles = []
    for profile_url in linkedin_profile_urls:
        profiles.append(scrape_linkedin_profile(profile_url))
    return profiles

if __name__ == "__main__":
    linkedin_profile_urls = [
        "https://www.linkedin.com/in/joseph-m-garcia/",]
    profiles = scrape_linkedin_profiles(linkedin_profile_urls)
    print(profiles)
    print(type(profiles))
    print(type(profiles[0]))
    print(type(profiles[0]["publicProfileUrl"]))



