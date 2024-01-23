# Selenium Web Scraping for MakeMyTrip Railways

This Python script utilizes the Selenium library to automate the process of searching for train journeys on the MakeMyTrip Railways website. The script performs the following steps:

1. Navigates to the MakeMyTrip Railways website.
2. Handles the notification frame that may appear on the page.
3. Searches for train journeys from Delhi to Lucknow on a specific date and class.

## Prerequisites

Make sure you have the following installed:

- Python
- Selenium library
- Chrome WebDriver

You can install the required libraries using the following commands:

```bash
pip install selenium
```

Download the Chrome WebDriver from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) and ensure it's in your system's PATH.

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your_username/your_repository.git
```

2. Navigate to the project directory:

```bash
cd your_repository
```

3. Run the Python script:

```bash
python script_name.py
```

Make sure to replace `your_username/your_repository` with your actual GitHub username and repository name and `script_name.py` with the name of your Python script.

## Script Explanation

- The script uses Selenium with Chrome WebDriver to automate web interactions.
- It handles the notification frame using explicit waits to ensure the frame is loaded before interacting with it.
- It selects the cities, date, and class for the train journey.
- Finally, it initiates the search and fetches the relevant information.

Note: Please be mindful of web scraping policies and the terms of service of the website you are interacting with.

Feel free to customize the script according to your specific requirements.
