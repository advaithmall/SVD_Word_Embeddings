import pprint
import json
import sys
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from tqdm import tqdm
import pickle
from scipy.linalg import svd
from sklearn.utils.extmath import randomized_svd

i = 0
corp_list = []
check_list = []
count = 0
print("Loading data...")
with open('corp.json') as f:
    for line in tqdm(f, total=4500000, desc="Reading"):
        i += 1
        if i%58==0:
            count+=1
            data = json.loads(line)
            txt = data['reviewText']
            txt = txt.lower()
            #replace . ! ? with <eos>
            txt = re.sub(r'\d+', ' numhere ', txt)
            txt = re.sub(r'[.!?]', ' eos ', txt)
            #replace all other punctuation with <sym>
            txt = re.sub(r'[^\w\s.!?]', ' <sym> ', txt)
            txt = txt.split()
            corp_list.extend(txt)
            # print(txt)
        if i>4500000:
            break
        else:
            continue
print("Saving...")
with open('corp_list.pickle', 'wb') as f:
    pickle.dump(corp_list, f)
print("Done")

print("got: ", count, "out of: ", i)

word_dict = {}
for word in tqdm(corp_list, total=len(corp_list), desc="Creating dictionary"):
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
fin_dict = {}
fin_dict["<unk>"] = 0
unk_list = []
wrd2idx = {}
k = 0
wrd2idx["<unk>"] = k
for item in word_dict.keys():
    if word_dict[item] > 2:
        k += 1
        wrd2idx[item] = k
        fin_dict[item] = word_dict[item]
    else:
        fin_dict["<unk>"] += word_dict[item]
        unk_list.append(item)
V = len(fin_dict.keys())+10
matrix = np.zeros((V, V))
window = 3
for i in tqdm(range(window, len(corp_list)-window), total=len(corp_list)-2*window, desc="Creating matrix"):
    for k in range(i-window, i):
        matrix[wrd2idx.get(corp_list[i], wrd2idx["<unk>"])
               ][wrd2idx.get(corp_list[k], wrd2idx["<unk>"])] += 1
    for k in range(i+1, i+window+1):
        matrix[wrd2idx.get(corp_list[i], wrd2idx["<unk>"])
               ][wrd2idx.get(corp_list[k], wrd2idx["<unk>"])] += 1

U, s, Vt = randomized_svd(matrix, n_components=1000)
#save word2idx in a pickle file
with open('word2idx.pickle', 'wb') as f:
    pickle.dump(wrd2idx, f)
#save U in a pickle file
with open('U.pickle', 'wb') as f:
    pickle.dump(U, f)
