# reviewsense
E-commerce Sentiment Analysis and Review Processing

## Overview

This project focuses on sentiment analysis and processing of product reviews within an e-commerce dataset. The goal is to extract valuable insights from customer feedback by analyzing sentiments, generating summary reports, and performing data queries. The project utilizes Python, pandas/nltk libraries for data manipulation and SQL for database interaction.

## Features

- **Data Loading and Preprocessing**: Use `module1.py` to load the dataset, preprocess the reviews, and handle duplicates.

- **Sentiment Analysis and Tokenization**: Utilize `module2.py` for sentiment analysis, tokenization, and normalization of review text using functions from `settings.py`.

- **Summary Reports**: Generate summary reports using SQL queries stored in `queries.sql`.

- **MySQL Integration**: Modify `db.py` with your MySQL database connection details for seamless integration.

- **Custom Text Processing**: Fine-tune text processing steps in `settings.py` for tailored normalization.

## Getting Started
**Data**: Place the 'ecommerce.csv' dataset in the project directory.
**Execution**: Run `module1.py` for data preprocessing and `module2.py` for sentiment analysis and tokenization.
**Database**: If using MySQL, update `db.py` with database connection details and execute SQL queries from `queries.sql`.

## Usage

- Run `module1.py` to load, preprocess, check, and remove duplicates.

- Execute `module2.py` to perform sentiment analysis, tokenization, and normalization.

- Generate summary reports by executing SQL queries from `queries.sql`.

- For MySQL integration, modify `db.py` with database connection details and execute SQL queries from `queries.sql`.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
