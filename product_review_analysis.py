#Task 1: Keyword Highlighter

#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
    #reviews = [
#        "This product is really good. I'm impressed with its quality.",
#        "The performance of this product is excellent. Highly recommended!",
#        "I had a bad experience with this product. It didn't meet my expectations.",
#        "Poor quality product. Wouldn't recommend it to anyone.",
#        "The product was average. Nothing extraordinary about it."
#    ]
#So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."
reviews = [
    "This product is really good. I'm impressed with its quality.", 
    "The performance of this product is excellent. Highly recommended!", 
    "I had a bad experience with this product. It didn't meet my expectations.", 
    "Poor quality product. Wouldn't recommend it to anyone.", 
    "The product was average. Nothing extraordinary about it."
    ]
#search and capitalize the keywords

for review in reviews:
    if "good" in review:
        uppercase_review = review.replace("good", "GOOD")
    elif "Good" in review:
        uppercase_review = review.replace("Good", "GOOD")
    elif "excellent" in review:
        uppercase_review = review.replace("excellent", "EXCELLENT")
    elif "Excellent" in review:
        uppercase_review = review.replace("Excellent", "EXCELLENT")
    elif "bad" in review:    
        uppercase_review = review.replace("bad", "BAD")
    elif "Bad" in review:   
        uppercase_review = review.replace("Bad", "BAD")
    elif "poor" in review:    
        uppercase_review = review.replace("poor", "POOR")
    elif "Poor" in review:    
        uppercase_review = review.replace("Poor", "POOR")
    elif "average" in review:    
        uppercase_review = review.replace("average", "AVERAGE")
    elif "Average" in review:    
        uppercase_review = review.replace("Average", "AVERAGE")
    else:
        uppercase_review = review
    print (uppercase_review)

#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.


def evaluate_reviews(reviews):
    lower_reviews = [review.lower() for review in reviews]
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    positive_count = 0
    negative_count = 0

    for review in lower_reviews:
        for positive_word in positive_words:
            positive_count = positive_count + review.count(positive_word)
        for negative_word in negative_words:
            negative_count = negative_count + review.count(negative_word)
    return print(f"Total Positive Words: {positive_count}\nTotal Negative Words: {negative_count}")
        
evaluate_reviews (reviews)


#Task 3: Review Summary

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
limit = 30

for review in reviews:
    summarized_review = review [:limit]
    for character in review [limit:]:
        if character != " ":
            summarized_review += character
        else:
            break
    print (summarized_review + "...")

#Example: "This product is really good. I'm...",