import re

def sentence_splitter(input_str):
    sentences = re.sub(r'\n', '', input_str)

    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)

    sentences = re.sub(r'!\s', '!\n', sentences)

    sentences = re.sub(r'\?\s', '?\n', sentences)

    print sentences


sentence = "Mr. Smith bought cheapsite.com for 1.5 million dollars, \
i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. \
In any case, this isn't true... Well, with a probability of .9 it isn't."

if __name__ == "__main__":
    sentence_splitter(sentence)
