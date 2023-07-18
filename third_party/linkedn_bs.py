import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Function to scrape LinkedIn profile given a URL"""
    response = requests.get(linkedin_profile_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_data = {}
        profile_data['name'] = soup.select_one('.pv-top-card--list .text-heading-xlarge').get_text(strip=True)
        profile_data['headline'] = soup.select_one('.pv-top-card--list .text-body-medium').get_text(strip=True)
        # Add more data extraction logic as per your requirements
        return profile_data
    else:
        return print("Error scraping LinkedIn profile.")

def scrape_linkedin_profiles(linkedin_profile_urls: list):
    """Function to scrape LinkedIn profiles given a list of URLs"""
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
    else:
        print("Error scraping profiles.")