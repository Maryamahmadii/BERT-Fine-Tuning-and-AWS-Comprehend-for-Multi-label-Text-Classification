# ML-Driven E-commerce Categorization with Web Scraping, BERT Fine-tuning and AWS Comprehend

## Overview
This project leverages web scraping to extract detailed product information from e-commerce websites, setting the stage for a sophisticated machine learning approach to categorization. 
The project capitalizes on the advanced capabilities of language representation models and cloud-based machine learning services to streamline product categorization on e-commerce platforms. By integrating web scraping, BERT model fine-tuning, and AWS Comprehend, I create a powerful multilabel text classification system that accurately tags products based on their names, thereby facilitating better searchability and user navigation.

## Data Scraping
Web scraping techniques are used to harvest product details such as names, prices, and predefined categories from an online retail site. This rich dataset forms the foundation for the machine learning models training, validation and test.

## Data Preparation
Products often transcend a single category. For instance, a product may be suitable for 'Automotive Tools' as well as 'Lighting.' To accommodate this, I organized the dataset for the BERT model and AWS Comprehend in a multilabel format. This involved structuring each entry as CLASS|CLASS|CLASS, Product Name to ensure the models could learn to assign multiple relevant categories to each product.

## Model Development

### Multilabel Classification with AWS Comprehend
With the data prepared, AWS Comprehend's custom multilabel text classification model was employed. The model was trained with 90% of the data, using the remaining 10% as a test set to evaluate performance.
**AWS Services Utilized:**
- AWS Comprehend Custom Classification
- IAM (Identity and Access Management)
- Amazon S3 (Simple Storage Service)
- AWS Endpoint
- Amazon SageMaker

### BERT Model and Fine-tuning
I utilized a BERT model, a leading language representation model, and fine-tuned it with our specific dataset. The fine-tuning process involved training the BERT model with 80% of the dataset, with the remaining 20% reserved for evaluation. Additionally, we tested the model's inference capabilities with randomly selected product names from Amazon to simulate real-world performance.

## Model Evaluation
I meticulously evaluated both the fine-tuned BERT model and the AWS Comprehend classifier. A heatmap was generated to visualize the classification metrics for each label (Accuracy, Precision, Recall, F1 Score), providing a clear comparison between the two approaches.

### AWS Comprehend
The results from AWS Comprehend include a JSON file containing a confusion matrix. This matrix was visualized using a heatmap to display detailed metrics for each class, providing insights into the model’s performance across different categories.

![Metrics Heatmap](https://github.com/Maryamahmadii/ML-Driven-E-commerce-Categorization-with-Web-Scraping/blob/main/Images/AWS_metrics_heatmap.png)

### BERT Lightning Model

![Metrics Heatmap](https://github.com/Maryamahmadii/ML-Driven-E-commerce-Categorization-with-Web-Scraping/blob/main/Images/BERT_metrics_heatmap.png)


## Inference Testing

### AWS Comprehend
To streamline deployment and demonstrate the adaptability of our model, I created an endpoint on AWS Comprehend. Inference tests were conducted on the endpoint using the same product name from the BERT model testing. Here's a Python code snippet highlighting this process:

```python
import boto3

comprehend_client = boto3.client(service_name='comprehend') 
endpointarn = 'Your_Endpoint_Arn'
product = 'ACANII - For 2006-2014 Honda Ridgeline Headlights Headlamps Replacement 06-14 Driver + Passenger Side'

result = comprehend_client.classify_document(Text=product, EndpointArn=endpointarn)

classes = result['Labels']

for n in classes:
    print(n['Name'], n['Score'])
    
Lighting 0.9998512268066406
Body Parts 0.9984129667282104
Exterior 0.9973132014274597
```
The AWS Comprehend classifier provided a list of categories with confidence scores. It identified 'Lighting' with the highest confidence, followed by 'Body Parts' and 'Exterior'. These results indicate that AWS Comprehend can effectively recognize multiple categories with high confidence, which is beneficial for products that fit into more than one category.

### BERT Lightning Model
To validate the real-world applicability of the BERT model, we conducted inference tests using actual product names from the Amazon website. The goal was to ascertain the model's capability to categorize products accurately outside the training dataset. Below is a sample Python script demonstrating this test:

```python
product = 'ACANII - For 2006-2014 Honda Ridgeline Headlights Headlamps Replacement 06-14 Driver + Passenger Side'

tags = predict(product, model)
if not tags[0]:
    print('This Product cannot be associated with any known category - Please review to see if a new category is required')
else:
    print(f'Following Tags are associated : \n {tags}')

Following Tags are associated : 
 [('Exterior', 'Lighting')]
```

The model successfully identified the product as belonging to the categories 'Exterior' and 'Lighting'. This test provides a snapshot of how the fine-tuned BERT model performs in practical scenarios, ensuring its effectiveness for e-commerce platforms.

## Comparative Analysis
- **Training Efficiency**: AWS Comprehend was trained in 55 minutes for $8, while BERT required 3 hours on a personal laptop, indicating AWS's solution is more time and cost-efficient.
- **Category Precision**: The BERT model seems to focus on fewer but more relevant categories, which might be preferable for simplicity and accuracy.
- **Deployment Considerations**: AWS Comprehend offers ease of deployment and scalability as a managed service, while BERT would require more infrastructure and management if deployed at scale.
- **Integration and Deployment**: AWS services provided an integrated environment that may simplify deployment and management, especially with the use of Comprehend, IAM, S3, and SageMaker.

## Conclusion
Both models have their strengths and are suitable for different scenarios. AWS Comprehend offers quick training times, low cost, and seamless integration with AWS services, making it a great choice for those already invested in the AWS ecosystem. The BERT model, while requiring more time and resources to fine-tune, showcases impressive precision and accuracy, which could be ideal for applications where these metrics are paramount.