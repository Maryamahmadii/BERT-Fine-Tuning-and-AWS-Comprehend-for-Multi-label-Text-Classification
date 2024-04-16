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
I meticulously evaluated both the fine-tuned BERT model and the AWS Comprehend classifier. A heatmap was generated to visualize the classification metrics for each label (Accuracy, Precision, Recall, F1 Score), providing a clear comparison between the two approaches.

### AWS Comprehend
The results from AWS Comprehend include a JSON file containing a confusion matrix. This matrix was visualized using a heatmap to display detailed metrics for each class, providing insights into the model’s performance across different categories.

![Metrics Heatmap](https://github.com/Maryamahmadii/ML-Driven-E-commerce-Categorization-with-Web-Scraping/blob/main/Images/AWS_metrics_heatmap.png)

### BERT Lightning Model

![Metrics Heatmap](https://github.com/Maryamahmadii/ML-Driven-E-commerce-Categorization-with-Web-Scraping/blob/main/Images/BERT_metrics_heatmap.png)


## Inference Testing
To validate the real-world applicability of the BERT model, we conducted inference tests using actual product names from the Amazon website. The goal was to ascertain the model's capability to categorize products accurately outside the training dataset. Below is a sample Python script demonstrating this test:

\```python
product = "ACANII - For 2006-2014 Honda Ridgeline Headlights Headlamps Replacement 06-14 Driver + Passenger Side"

tags = predict(product, model)
if not tags[0]:
    print('This Product cannot be associated with any known category - Please review to see if a new category is required')
else:
    print(f'Following Tags are associated : \n {tags}')
# Expected Output
Following Tags are associated : 
 [('Exterior', 'Lighting')] \```
 
The model successfully identified the product as belonging to the categories 'Exterior' and 'Lighting'. This test provides a snapshot of how the fine-tuned BERT model performs in practical scenarios, ensuring its effectiveness for e-commerce platforms.

## Conclusion
This project demonstrates the effective use of web scraping and AWS machine learning tools to implement a multilabel classification system in e-commerce. Such systems can significantly enhance the accuracy of product categorization, improving both the end-user experience and backend management of product listings.
