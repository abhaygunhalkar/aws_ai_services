import boto3

def detect_sentiment(text, language_code):
    """
    Detects the sentiment of the given text using Amazon Comprehend.

    Args:
        text (str): The text to analyze.
        language_code (str): The language code of the text (e.g., 'en' for English).

    Returns:
        dict: The sentiment analysis result, or None on error.
    """
    try:
        client = boto3.client('comprehend')
        response = client.detect_sentiment(Text=text, LanguageCode=language_code)
        return response
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return None
    
def detect_entities(text, language_code):
    """
    Detects entities in the given text using Amazon Comprehend.

    Args:
        text (str): The text to analyze.
        language_code (str): The language code of the text (e.g., 'en' for English).

    Returns:
        dict: The entity detection result, or None on error.
    """
    try:
        client = boto3.client('comprehend')
        response = client.detect_entities(Text=text, LanguageCode=language_code)
        return response
    except Exception as e:
        print(f"Error during entity detection: {e}")
        return None
    
def detect_pii_entities(text, language_code):
    """
    Detects personally identifiable information (PII) in the given text
    using Amazon Comprehend.

    Args:
        text (str): The text to analyze.
        language_code (str): The language code of the text (e.g., 'en').

    Returns:
        dict: The PII entity detection result, or None on error.
    """
    try:
        client = boto3.client('comprehend')
        response = client.detect_pii_entities(Text=text, LanguageCode=language_code)
        return response
    except Exception as e:
        print(f"Error during PII entity detection: {e}")
        return None

def main():
    """
    Main function to demonstrate sentiment analysis.
    """
    text_to_analyze = "Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-0000-1111-0008 has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. Customer feedback for Sunshine Spa, 123 Main St, Anywhere. Send comments to Alice at sunspa@mail.com. I enjoyed visiting the spa. It was very comfortable but it was also very expensive. The amenities were ok but the service made the spa a great experience."
    language_code = 'en'

    sentiment_result = detect_sentiment(text_to_analyze, language_code)
    
    entity_result = detect_entities(text_to_analyze, language_code)
    
    pii_result = detect_pii_entities(text_to_analyze, language_code)

    if sentiment_result:
        print(f"Text: {text_to_analyze}\n")
        print(f"Sentiment: {sentiment_result['Sentiment']}\n")
        print(f"Sentiment Scores: {sentiment_result['SentimentScore']}\n")
    else:
        print("Sentiment analysis failed.")
    print('--------------------------------------------------------------------------')       
    if entity_result:
        print("Detected Entities:")
        for entity in entity_result['Entities']:
            print(f"Type: {entity['Type']}, Text: {entity['Text']}")
    else:
        print("Entity analysis failed.")
    
    print('--------------------------------------------------------------------------')  
   
    #The API response doesn't directly include the full text of the PII, but rather its type, location (BeginOffset, EndOffset), and confidence score.
    # Extract the actual text of the PII entities from the input text using the BeginOffset and EndOffset values provided in the API response
    if pii_result:
        print("Detected PII Entities:")
        print(pii_result['Entities'])
        for entity in pii_result['Entities']:
            if 'Text' in entity:  # Check if 'Text' key exists
                print(f"Type: {entity['Type']}, Start: {entity['BeginOffset']}, End: {entity['EndOffset']}")
                # Get the actual text from the input
                pii_text = text_to_analyze[entity['BeginOffset']:entity['EndOffset']]
                print(f"  Text: {pii_text}")
            else:
                print(f"Type: {entity['Type']}, Text: N/A")
    else:
        print("PII Entity analysis failed.")
        
if __name__ == "__main__":
    main()