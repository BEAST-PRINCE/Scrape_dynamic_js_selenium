# Web Data Scraper

This Python script scrapes project data from the HP RERA Public Dashboard and saves the data to a CSV file.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Google Chrome browser
- Chromedriver corresponding to your Chrome version

### Python Libraries

Install the required Python libraries using `pip`:

- selenium
- csv
- venv (In case if you are creating a virtual environment for running this script)


pip install selenium csv

OR 

pip install -r requirements.txt



Usage

    Run the Script:

    Execute the script using Python:

    bash

    python scraper.py

    Output:

    The scraped data will be saved to output.csv in the same directory.


# Script Overview

Libraries Used

    selenium: For automating the web browser interaction.
    csv: For saving the data in CSV format.


Workflow

    Open the HP RERA Public Dashboard.
    Wait until the page is fully loaded.
    Locate the first 6 project blocks.
    For each project:
        Click on the project link to open the modal with project details.
        Extract the Name, Permanent Address, PAN No., and GSTIN No..
        Append the extracted data to a list.
        Close the modal or navigate back.
    Save the scraped data to output.csv.
    Quit the browser.

Notes

    The script runs the browser in headless mode.
    Adjust the number of projects to scrape by modifying the [:6] slice.
    Ensure your network connection is stable as the script waits for elements to load on the webpage.
