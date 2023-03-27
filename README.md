# SVD_Word_Embeddings
Word Embeddings built by doing singular value decomposition on Co-Occurrence matrix

### Directory Structory

```
.
├── eval.py
├── main.py
├── svd_images
│   ├── an.png
│   ├── awesome.png
│   ├── crucial.png
│   ├── father.png
│   ├── study.png
│   ├── thinking.png
│   └── titanic.png
├── U.pickle
└── word2idx.pickle

1 directory, 11 files

```


### In svd folder, download: U.pickle, word2idx.pickle

### U.pickle: https://iiitaphyd-my.sharepoint.com/:u:/g/personal/advaith_malladi_research_iiit_ac_in/EeodNM2ac01GtYlOHOBUhm8BjJdBykLE_w5_FKaQjAGe9Q?e=XS5xwI

### word2idx.pickle: https://iiitaphyd-my.sharepoint.com/:u:/g/personal/advaith_malladi_research_iiit_ac_in/EULP5H3uqXlPlJfrrZe8zNQBFVKDoyIzuDmPp349Mi7j0w?e=hpwbeV



## To run code related to SVD, first:
```
cd svd

```

### to look at plot images presented in report:

```
cd svd_images

```

### To create embeddings, run:

```

python3 -W ignore main.py

```

### To get the 10 closest words to a given word and to plot them, run:

```

python3 -W ignore eval.py

enter word upon prompt

```

