import re

class FacebookGroupsProcessor:
    def __init__(self, groups):
        self.groups = groups

    def merge_and_filter_groups(self):
        merged_groups = {}
        for group in self.groups:
            url = group['URL']
            if url not in merged_groups:
                merged_groups[url] = group
            else:
                for key, value in group.items():
                    if value and value != 'N/A':
                        merged_groups[url][key] = value

        filtered_groups = []
        for group in merged_groups.values():
            if (group['GroupName'] and group['Members'] != 'N/A' and
                group['Privacy'] != 'N/A' and not self.is_low_activity_group(group['PostFrequency'])):
                filtered_groups.append(group)

        return filtered_groups

    def is_low_activity_group(self, post_frequency, threshold=1):
        if post_frequency == 'N/A':
            return False
        match = re.search(r'(\d+(?:\.\d+)?)\s+posts?\s+(?:a|per)\s+(day|month)', post_frequency)
        if match:
            number = float(match.group(1))
            period = match.group(2)
            if period == 'month' and number <= threshold:
                return True
            elif period == 'day' and number * 30 <= threshold:
                return True
        return False

    def process(self):
        return self.merge_and_filter_groups()