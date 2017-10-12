# uniqueness-point-tools
python tools to help calculate words' phonemic uniqueness points


uniq.py takes a set of words (in words.txt) and summarizes phonological neighborhood and phonemic uniqueness point information (the speech sound at which a word is uniquely identifiable) in a text file (words_uniqinfo.txt) based on the CMU dictionary (cmudict.txt, more info at http://www.speech.cs.cmu.edu/cgi-bin/cmudict).

results should be taken as a starting point and manually checked, due to some weird words in the cmudict and depending on usage goals (e.g. cmudict contains singular and plural words as separate entries, resulting in a relatively late calculated uniqueness point for most nouns, which may not always be appropriate).
