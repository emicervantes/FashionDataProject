# Fitted and Predicted (VenusHacks 2023)

### Developed by Emi Cervantes, Christina Orengo, Nathan Samarasena

As many women-identifying people know, it can often be difficult to find and purchase the proper clothing that fits to our unique body shapes and specifications. In fact, it often feels like every product can just end up completely different than another, even if it's in the same style! So, what if there were a program designed to remedy these problems? What if there were a program that could streamline my shopping experience using _my_ dimensions? Introducing... '**Fitted and Predicted**'!

This program was designed to showcase how seemingly complicated and nuanced tasks as quality prediction and recommendation of something as subjective as clothing and fashion can be optimized for the consumer, especially with the use of machine learning and model training.

**Data Preparation**

With this problem in mind, the Clothing Fit Dataset by Rishabh Misra was the perfect starting point. Starting with a dataset of over 5500 clothing products in various categories including their clothing type (top, bottom, outerwear, dress), ratings and reviews, fit of clothing feedback, and customer/product measurements. 

To be able to more effectively analyse the data, Emi commanded the review and feedback normalization, taking written out responses by customers and using keyword search to provide us with a numerical rating. After that point, we adjusted all analytically viable columns to numeric values to prepare our data frames for training. Next, we took the quality and review/rating scores to generate a new aggregated score for each unique review.

**Machine Learning using KNN Linear Regression**

Now that our data was prepped and ready for training, we moved forward with KNN Linear Regression model to help us analyze our information. For each clothing category we compiled a list of important measurements that are relevant to each type. For example, for tops and dresses we included bra size and cup size to help train our data along with waist, hip, and fit data. From there, we wanted to train our model against the quality pieces based on the average score that would then help us provide us with the best quality recommendation for consumers. Our test and training models were checked for accuracy by the use of mean square error algorithms and we determined that our error between test and training was sufficiently low when our nearest neighbor count was set to 15.

**Applying Our Model to Front End Web Development**



**Citation**
1. Misra, Rishabh, Mengting Wan, and Julian McAuley. "Decomposing fit semantics for product size recommendation in metric spaces." In Proceedings of the 12th ACM Conference on Recommender Systems, pp. 422-426. 2018.
2. Misra, Rishabh and Jigyasa Grover. "Sculpting Data for ML: The first act of Machine Learning." ISBN 9798585463570 (2021).

* https://www.kaggle.com/datasets/rmisra/clothing-fit-dataset-for-size-recommendation
* https://rishabhmisra.github.io/publications/
