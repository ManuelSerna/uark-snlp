#************************************************
'''
    Natural Language Processing Homework #1
    Part 2: Chi-squared approach
    Manuel Serna-Aguilera
'''
#************************************************
import collections
import json
import string

#------------------------------------------------
# Get chi-square values.
# Take in key-value pair and bigrams dict.
#------------------------------------------------
def get_chi_square(key, value, bigrams):
    # Get individual words from bigram to access their counts
    bigram = key.split() # always two elements
    n = bigrams['total']
    
    '''
    Get w11, w12, w21, w22 values for 2 x 2 table.
        - w11: bigrams where first second words DO appear
        - w12: bigrams where first word DOES NOT appear, but the second DOES
        - w21: bigrams where first word DOES appear, but the second DOES NOT
        - w22: bigrams where neither first now second appear (subtract total token count n from three previous calculations)
    '''
    w11 = value
    w12 = bigrams['tokens'][bigram[0]]-value
    w21 = bigrams['tokens'][bigram[1]]-value    
    w22 = n-w11-w12-w21
    
    # Calculate chi-square
    top = n*((w11*w22)-(w12*w21))*((w11*w22)-(w12*w21))
    bottom = (w11+w12)*(w11+w21)*(w12+w22)*(w21+w22)
    chi_squared = top/bottom
    
    return chi_squared



'''
Extract json object as a dict.
'''
file_name = "data.json"
text = open(file_name, 'r')
text_str = text.read()
bigrams_json = json.loads(text_str)

'''
For each bigram, get the chi-squared value for bigrams that appear more than x times.
'''
chi_square_vals = {}
threshold = 1
for key, value in bigrams_json['bigrams'].items():
    if value > threshold:
        chi_square_vals[key] = get_chi_square(key, value, bigrams_json)

'''
Sort the chi-square dict by nonincreasing chi-square values.
'''
chi_square_vals = sorted(chi_square_vals.items(), key=lambda kv: kv[1], reverse=True)
chi_square_vals = collections.OrderedDict(chi_square_vals)

'''
Write the top 100 collocations (according to frequency) to a file.
'''
with open("collocations.text", 'w') as file:
    # Iterate through top 100 words
    file.write('-----------------------------')
    file.write('\n')
    file.write('Top 100 bigrams.')
    file.write('\n')
    file.write('-----------------------------')
    file.write('\n')
    for i in list(chi_square_vals)[0:100]:
        file.write(i)
        file.write('\n')
    
    # Iterate through bottom 5
    file.write('-----------------------------')
    file.write('\n')
    file.write('5 lowest weighted bigrams.')
    file.write('\n')
    file.write('-----------------------------')
    file.write('\n')
    for i in list(chi_square_vals)[len(chi_square_vals)-5:len(chi_square_vals)]:
        file.write(i)
        file.write('\n')

'''
Display the top 25 collocations to the terminal.
'''
j = 1
print('========================')
print('Top 25 collocations (based on chi-square values)')
print('------------------------')
for i in list(chi_square_vals)[0:25]:
    print('{}) {}'.format(j, i))
    j += 1
print('========================')
