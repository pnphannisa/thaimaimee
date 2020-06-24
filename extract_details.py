from tika import parser
import glob
from tqdm import tqdm
from multiprocessing import Pool
import json

def get_texts(fname):
    return parser.from_file(fname)

fnames = glob.glob("data/pdf_details/3.2-1/*/*.pdf")
print(len(fnames))

#how many pdfs
get_texts(fnames[0])

#loop to get texts
results = []
bs = 100
for i in range(len(fnames)//bs+1):
    with Pool(4) as p: results+=p.map(get_texts, fnames[i*bs:(i+1)*bs])

#how many texts
print(len(results))
json.dump(results, open('data/results32.json','r')

