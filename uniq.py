import string

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
script for computing phonological neighborhood information and
uniqueness points for a set of words (python 2.7)
mbrown@alum.mit.edu

inputs:
>> words.txt (a list of words of interest: one word per line)
>> cmudict.txt: CMU pronouncing dictionary
   (http://www.speech.cs.cmu.edu/cgi-bin/cmudict) -- each line
   contains 1 word followed by its phonemes

outputs:
>> words_uniqinfo.txt: a text file containing the following
   info for each word:
    -- its phonemes
    -- at each phoneme, how many CMUdict competitors the word
       has, and if less than 20, what they are
    -- the word's uniqueness point (if the word is not unique,
       then len(phonemes)+1
    -- NOTE: uniqueness point should be manually checked
       (CMUdict contains some weird nonwords, and depending on
       your goals, you may not want to count variations on the
       same word, such as singular/plural, as competitors)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# home directory
homeDir = 'C:/Users/meredith/Downloads/cmudict_tools/'
if homeDir[-1]!='/':
    homeDir=homeDir+'/'

# file imports
cmudictFile = open(homeDir + 'cmudict.txt','r')
inFile = open(homeDir + 'words.txt','r')
outFile = open(homeDir + 'words_uniqinfo.txt','w')

# process cmudict: entries of form [word [phons]]
cmudict=[]
for line in cmudictFile:
    line = string.split(line,sep='  ')
    if ';;;' not in line[0]:
        line[1] = line[1].strip('\n')
        line[1] = string.split(line[1],sep=' ')
        cmudict.append(line)

# create words list
words=[string.split(line,sep='\n')[0].strip('\xef\xbb\xbf') for line in inFile]

# aggregate cmudict entries
wordsPron = []
for word in words:
    for entry in cmudict:
        if entry[0].lower() == word.lower(): # case insensitive
            wordsPron.append(entry)
            break

# for each entry: format information & write to outfile
for word in wordsPron:
    # print header for entry
    outFile.write(string.join([word[0],' (', str(len(word[1])), ': ', \
                    string.join(word[1],' '),')\n']))
					
	# default uniqueness point: after word offset
    uniq = len(word[1])+1 
    			
    # iterate over cmudict entries
	# could be further optimized by sorting input words (perhaps later)
    searchspace = cmudict
    for phon in range(len(word[1])):
        matchNum=0
        matches=[]
        newsearchspace=[]
		
		# identify cmudict entries whose initial chars match target word's, add to newsearchspace
        for entry in searchspace:
            if len(entry[1]) >= phon:
                if word[1][0:phon+1] == entry[1][0:phon+1] and \
                   word[0].lower() != entry[0].lower():
                    matchNum+=1
                    matches.append(entry[0])
                    newsearchspace.append(entry)
        searchspace = newsearchspace
		
		# process matches 
        if matchNum > 20:
            matches = ['more than 20']
        elif matchNum == 0:
            uniq = phon+1
			
		# format output
        outFile.write(string.join(['\t',str(phon+1),": ", str(matchNum), \
                                  "competitors (", string.join(matches, sep=', '),\
                                  ")\n"]))
        
		# stop if done
        if matchNum == 0:
            break
			
    outFile.write(string.join(['\tuniqueness point: ',str(uniq),'\n\n']))
        
outFile.close()
print('File generated.')

