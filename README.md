# Facebook Groups Parser and Processor

This project provides tools to parse and process Facebook group information from an HTML file. It extracts group details, merges duplicate entries, filters out low-activity groups, and outputs the processed data in JSON or CSV format.

## Features

- Parse Facebook group information from an HTML file
- Merge duplicate group entries
- Filter out low-activity groups
- Output processed data in JSON or CSV format

## Requirements

- Python 3.6+
- BeautifulSoup4

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/facebook-groups-parser-processor.git
   cd facebook-groups-parser-processor
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Obtaining the Input HTML File

Before running the script, you need to obtain an HTML file containing Facebook group information:

1. Go to Facebook and perform a search for groups you're interested in.
2. After the initial search, click on the "Groups" tab to filter the results.
3. Save the entire webpage:
   - In Firefox: Choose "Web Page, complete" when saving.
   - In Chrome, Edge, and other browsers: Look for similar options to save the complete webpage.
4. Name the file "fb.html" for simplicity. You can save it in your /tmp folder or on your desktop.

## Usage

1. Ensure your virtual environment is activated (see step 3 in the Installation section).

2. Run the main script, passing the path to your HTML file as an argument:
   ```
   python main.py /path/to/your/fb.html
   ```

   For example:
   ```
   python main.py /tmp/fb.html
   ```
   or
   ```
   python main.py ~/Desktop/fb.html
   ```

3. Choose the output format (JSON or CSV) when prompted.

4. The processed data will be saved to a file named `facebook_groups_processed.json` or `facebook_groups_processed.csv`, depending on your choice.

5. When you're done, you can deactivate the virtual environment:
   ```
   deactivate
   ```

## Output Data Structure

The processed data in both JSON and CSV formats will contain the following fields for each Facebook group:

- `GroupName` (string): The name of the Facebook group.
- `GroupID` (string): The unique identifier of the group, extracted from the URL.
- `Members` (string): The number of members in the group, possibly including 'K' or 'M' for thousands or millions.
- `Privacy` (string): The privacy setting of the group, either "Public" or "Private".
- `PostFrequency` (string): The frequency of posts in the group, e.g., "5 posts a day" or "2 posts per month".
- `URL` (string): The full URL of the Facebook group.

Example JSON structure:
```json
[
  {
    "GroupName": "Example Group",
    "GroupID": "123456789",
    "Members": "10K",
    "Privacy": "Public",
    "PostFrequency": "5 posts a day",
    "URL": "https://www.facebook.com/groups/123456789"
  },
  ...
]
```

The CSV file will have these fields as columns, with each row representing a single Facebook group.

## File Structure

- `main.py`: The main script that orchestrates the parsing and processing of Facebook group data.
- `facebook_groups_parser.py`: Contains the `FacebookGroupsParser` class for parsing HTML and extracting group information.
- `facebook_groups_processor.py`: Contains the `FacebookGroupsProcessor` class for merging and filtering group data.
- `requirements.txt`: Lists the project dependencies.

## License

MIT License

Copyright (c) 2024 Tatsu Ikeda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.