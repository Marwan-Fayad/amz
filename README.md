## Amazon Sales Dataset

## Overview
This dataset contains detailed information about Amazon products, sales, and customer reviews. It is structured to support a variety of data analysis and machine learning tasks, including price optimization, sentiment analysis, and recommendation systems.

## Dataset Features
The dataset includes the following columns:

### Product Information
- **product_id**: A unique identifier assigned to each product.
- **product_name**: The name of the product.
- **category**: The category or type of product.
- **discounted_price**: The price of the product after applying discounts.
- **actual_price**: The original price of the product before any discounts.
- **discount_percentage**: The percentage of discount applied to the product.
- **rating**: The average rating given to the product by users.
- **rating_count**: The number of ratings received by the product.
- **about_product**: A brief description or key features of the product.

### User Information
- **user_id**: A unique identifier for each user.
- **user_name**: The name of the user who submitted a review.

### Review Information
- **review_id**: A unique identifier for each review.
- **review_title**: The title or headline of the review.
- **review_content**: The detailed content of the review.

### Links
- **img_link**: A URL to the product image.
- **product_link**: A URL to the product page on Amazon.

## Applications
- **Price Analysis**: Study how discounts impact product sales.
- **Sentiment Analysis**: Analyze customer reviews to understand user sentiments.
- **Recommendation Systems**: Develop personalized recommendations using user reviews and ratings.
- **Category Insights**: Explore trends and patterns within specific product categories.
- **Customer Behavior Analysis**: Identify trends such as:
  - Categories and sub-categories with the most products.
  - The cheapest products available after discounts.
  - Relationships between discounted prices and customer ratings.
  - Relationships between actual prices and discounted prices.

## Usage Instructions
1. **Data Loading**: Use tools like pandas to load the dataset:
   ```python
   import pandas as pd
   data = pd.read_csv('amazon_sales_dataset.csv')
   print(data.head())
   ```
2. **Preprocessing**: Handle missing values, normalize data, and prepare it for analysis.
3. **Exploration**: Perform exploratory data analysis to uncover insights.
4. **Modeling**: Use the data to train machine learning models for tasks such as classification, regression, or clustering.

## File Format
The dataset is provided in CSV format. Ensure to handle encoding or delimiter issues appropriately while loading.

## Contributions
Contributions to improve the dataset or documentation are welcome. Submit pull requests or open issues for suggestions and improvements.

## License
Specify the license under which the dataset is shared (e.g., MIT, CC BY 4.0).

## Disclaimer
This dataset is intended for educational and research purposes only. Ensure compliance with Amazon's terms and conditions when using the data for any purpose.

