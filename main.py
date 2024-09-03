import sys
import os
from facebook_groups_parser import FacebookGroupsParser
from facebook_groups_processor import FacebookGroupsProcessor

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Please enter the path to the HTML file: ")

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    parser = FacebookGroupsParser(file_path)
    groups = parser.parse_html()

    processor = FacebookGroupsProcessor(groups)
    processed_groups = processor.process()

    output_format = input("Choose output format (json/csv): ").lower()
    while output_format not in ['json', 'csv']:
        output_format = input("Invalid choice. Please enter 'json' or 'csv': ").lower()

    output_file = f"facebook_groups_processed.{output_format}"
    if output_format == 'json':
        parser.save_as_json(output_file, processed_groups)
    else:
        parser.save_as_csv(output_file, processed_groups)

    print(f"Processed data has been saved to {output_file}")
    print(f"Original group count: {len(groups)}")
    print(f"Processed group count: {len(processed_groups)}")

if __name__ == "__main__":
    main()