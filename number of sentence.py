import re
text = '''The apple doesn't fall. ...
All that glitters are not gold. ...
A picture is worth a thousand words. ...
Beggers can't be choosers. ...
A bird in the hand. ...
Better safe than sorry balaji...
An apple a day keeps doctor away. ...
Blood is thicker than water. ...
balaji sir 
'''
sentences = re.split(r'[.!?]\s*', text)
b_sentences = [sentence for sentence in sentences if sentence.strip().lower().startswith('b')]
num_b_sentences = len(b_sentences)
print(f"Number of sentences starting with 'B': {num_b_sentences}")