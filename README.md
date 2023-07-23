# LinkedIn Profiles Scrapper

This project utilizes Selenium 4.9.0 and EdgeDriver for web scraping LinkedIn profiles with an auto-login feature.

## Table of Contents
- [Introduction](#introduction)
- [Instructions](#instructions)
  - [1. Change the LinkedIn Search Query](#1-change-the-linkedin-search-query)
  - [2. Running the Web Scraping Process](#2-running-the-web-scraping-process)
  - [3. Data Collection to PostgreSQL DB](#3-data-collection-to-postgresql-db)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Warning](#warning)
- [Author](#author)

## Introduction
This project is designed to scrape LinkedIn profiles using Selenium 4.9.0 and EdgeDriver. It includes an auto-login feature, which makes it easier to gather data from LinkedIn profiles efficiently.

## Instructions

### 1. Change the LinkedIn Search Query
Before running the web scraping process, you should modify the LinkedIn search query according to your requirements. Locate the `vars.py` file and update the `SEARCH_QUERY` variable to match your target criteria.

### 2. Running the Web Scraping Process
To start the web scraping process, simply run the `main.py` script. This will initiate the scraping of LinkedIn profiles based on the search query you provided.

### 3. Data Collection to PostgreSQL DB
The scraped data will be collected to a PostgreSQL database. The connection URL for the database is set to `'postgresql://postgres:adminpass123@localhost/gino'`. Ensure that you have PostgreSQL installed and running on your local machine to store the data properly.

## Requirements
- Selenium 4.9.0

## Installation
1. Clone the repository:
git clone https://github.com/2tieatie/test_task.git

2. Install the required Python packages:
pip install -r requirements.txt

## Usage
Run the web scraping process using the following command:
python main.py


## Customization
If you encounter any issues during web scraping, you can customize the EdgeDriver options in the `vars.py` file. These options can help improve page loading and simplify HTML structure for easier scraping.

## Warning
Keep in mind that LinkedIn may have algorithms in place to prevent extensive web scraping. A single query in this project retrieves only the first 100 pages of data to avoid potential issues with LinkedIn policies.

## Author
Made by Misha Tumanov with 🐍❤️

