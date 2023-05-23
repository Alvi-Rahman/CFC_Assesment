# CFC Assesment Documentation


This project is designed to scrape a website, extract externally loaded resources, identify the location of the "Privacy Policy" page, and perform a word frequency count on the privacy policy page's content.

## Project Structure

The project is organized into the following folders:

- `controllers`: Contains the controller files that handle the main skeleton and Encapsulated Logic of the project.
- `utilities`: Contains utility files that provide the necessary functions for scraping and data processing.
- `tests`: Contains the test files for each function in each class in the project.

## Requirements

The project has the following requirements, which can be installed using the provided `requirements.txt` file:

- Python 3.9.x
- BeautifulSoup4
- Requests
- PyTest

To install the requirements, run the following command:

```shell
pip install -r requirements.txt
```


## Functionality

The program performs the following tasks:

1. **Scrape the Index Webpage**: It scrapes the index webpage hosted at `cfcunderwriting.com` to gather information.
2. **Extract Externally Loaded Resources**: It identifies and extracts all externally loaded resources such as images, scripts, and fonts that are not hosted on `cfcunderwriting.com`. The extracted resources are written to the `external_resources.json` file.
3. **Identify Privacy Policy Page**: It enumerates the hyperlinks on the page and identifies the location of the "Privacy Policy" page.
4. **Scrape Privacy Policy Page**: Using the URL identified in the previous step, it scrapes the content of the privacy policy page. It performs a case-insensitive word frequency count on the visible text and writes the frequency count to the `privacy_policy_word_count.json` file.

## Running the Program

To run the program, execute the 

```shell
python3 main.py
``` 

It calls the necessary functions from the controllers to perform the scraping and data processing tasks. Make sure you have the required dependencies installed before running the program.


After the program execution, you will find two output files generated:

- `external_resources.json`: This file contains the list of all external resources found on the index page of `cfcunderwriting.com`.
- `privacy_policy_word_count.json`: This file contains the word frequency count for each word in the privacy policy page of `cfcunderwriting.com`.

## Running Tests

The project includes test files in the `tests` folder to ensure the correctness of each function. 
To run the tests and check the coverage, execute the following command:

```shell
pytest
```


The test files have full coverage, and all functions should pass successfully.

