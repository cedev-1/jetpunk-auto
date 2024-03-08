# Automated Quiz Script for JetPunk

This Python script utilizes Selenium to automate a quiz on JetPunk.com, specifically focusing on European countries. It automatically fills in the answers to the quiz questions by entering the names of European countries into the text field.

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver

## Installing Dependencies

1. Install Python by following the instructions on [python.org](https://www.python.org/).
2. Install Selenium by running `pip install selenium`.
3. Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your system PATH.

## Usage

1. Ensure you have correctly configured the path to the Chrome WebDriver in the script.
2. Execute the script by running the following command in your terminal:

    ```
    python jetpunk-UE-country.py
    ```

## How it Works

The script launches a Chrome browser and navigates to the "Pays d'Europe en une minute" quiz page on JetPunk. It waits for a few seconds to allow the page to fully load, then clicks the quiz start button.

Afterward, the script automatically enters the names of European countries into the quiz text field one by one, based on the provided list. It then waits for a brief period between each entry.

Finally, the script closes the browser after 20 seconds.

Feel free to customize the list of countries or adjust any other parameters as needed for your specific use case.
