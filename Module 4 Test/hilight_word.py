def highlight_word(sentence, word):
    replace_word = word.upper()
    output_sentence = sentence.replace(word, replace_word)
    return(output_sentence)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))