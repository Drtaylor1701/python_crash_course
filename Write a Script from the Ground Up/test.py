def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    string_no_punctuation = ""
    for character in file_contents:
        if character not in punctuations:
            #print(character)
            string_no_punctuation = string_no_punctuation + character
            #print(string_no_punctuation)

    list_of_words = string_no_punctuation.split()
    #print(list_of_words)

    list_of_interesting_words = []
    for word in list_of_words:
        if word not in uninteresting_words:
            list_of_interesting_words.append(word)
        #print(list_of_interesting_words)

    frequency_dict = {}
    for word in list_of_interesting_words:
        if word in frequency_dict:
            print("yes")
            value = frequency_dict.get(word)
            print(value)
            frequency_dict.update({word: value + 1})
        else:
            print("no")
            frequency_dict.update({word: 1})
    print(frequency_dict)
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies()
    return cloud.to_array()

text = "At oh eight hundred hours, station time, the Romulan Empire formally declared war against the Dominion. They have already struck fifteen bases along the Cardassian border. So, this is a huge victory for the good guys! This may even be the turning point of the entire war. There's even a 'Welcome to the Fight' party tonight in the wardroom. So I lied, I cheated, I bribed men to cover the crimes of other men. I am an accessory to murder. But most the damning thing of all, I think I can live with it. And if I had to do it all over again, I would. Garak was right about one thing. A guilty conscience is a small price to pay for the safety of the Alpha Quadrant, so I will learn to live with it. Because I can live with it. I can live with it. Computer, erase that entire personal log."
calculate_frequencies(text)