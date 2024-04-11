# ML-Driven E-commerce Categorization with Web Scraping and AWS Comprehend

## Overview
This project leverages web scraping to extract detailed product information from e-commerce websites, setting the stage for a sophisticated machine learning approach to categorization. By deploying AWS Comprehend for a multilabel text classification task, the project automatically tags products with multiple relevant categories based on their titles, enhancing product discoverability and user experience.

## Data Scraping
The initial phase involves scraping e-commerce websites to collect key product details such as titles, prices, and categories. This data serves as the groundwork for the subsequent machine learning processes.

## Data Preparation
Upon analyzing the scraped data, it was observed that products often fit into multiple categories (e.g., a glass cleanser could belong to both 'Automotive Tools' and 'Interior and Exterior' categories). To address this, the dataset was structured in a format suitable for AWS Comprehend: each row formatted as `CLASS|CLASS|CLASS, Product Name`. This format ensures clarity in training the model to recognize and assign multiple tags.

## Multilabel Classification with AWS Comprehend
With the data prepared, AWS Comprehend's custom multilabel text classification model was employed. The model was trained with 90% of the data, using the remaining 10% as a test set to evaluate performance. The model achieved an impressive accuracy of 0.91.

## Model Evaluation
The results from AWS Comprehend include a JSON file containing a confusion matrix. This matrix was visualized using a heatmap to display detailed metrics for each class, providing insights into the model’s performance across different categories.

![Metrics Heatmap](...)

The heatmap visualization helps in understanding the model's accuracy and precision across various classes, allowing for targeted improvements in category classification.

## Conclusion
This project demonstrates the effective use of web scraping and AWS machine learning tools to implement a multilabel classification system in e-commerce. Such systems can significantly enhance the accuracy of product categorization, improving both the end-user experience and backend management of product listings.
