import re
from bs4 import BeautifulSoup
import json
import csv
import urllib.parse

class FacebookGroupsParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.groups = []

    def parse_html(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        group_links = soup.find_all('a', href=re.compile(r'https://www\.facebook\.com/groups/'))

        for link in group_links:
            group_name = link.text.strip()
            group_url = link.get('href')
            group_id = urllib.parse.urlparse(group_url).path.split('/')[-1]

            info_element = link.find_next('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6')
            if info_element:
                info_text = info_element.text.strip()
                members_match = re.search(r'(\d+\.?\d*[KM]?) members', info_text)
                privacy_match = re.search(r'(Public|Private)', info_text)
                posts_match = re.search(r'(\d+(?:\.\d+)?) posts? (?:a|per) (?:day|month)', info_text)

                members = members_match.group(1) if members_match else 'N/A'
                privacy = privacy_match.group(1) if privacy_match else 'N/A'
                posts = posts_match.group(0) if posts_match else 'N/A'

                self.groups.append({
                    'GroupName': group_name,
                    'GroupID': group_id,
                    'Members': members,
                    'Privacy': privacy,
                    'PostFrequency': posts,
                    'URL': group_url
                })

        return self.groups

    def save_as_json(self, output_file, groups=None):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(groups or self.groups, f, indent=2, ensure_ascii=False)

    def save_as_csv(self, output_file, groups=None):
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['GroupName', 'GroupID', 'Members', 'Privacy', 'PostFrequency', 'URL'])
            writer.writeheader()
            writer.writerows(groups or self.groups)