import json
import re
stack = []
current = {}

def convert(fname_in, fname_out):
    fieldnames = ("name", "ru", "en", "synonims", "comments", "children")
 
    with open(fname_in, "r") as fin, open(fname_out, "w") as fout:
        
        fout.write("[\n")
                
        for line in fin:
            result = re.findall('\s', line)
            if len(result) == 1:
                line = fin.readline()
            elif len(result) >= 2:
                current["'name':'en'"] = line.strip()
                fout.write(json.dumps(current, ensure_ascii=False, indent=4))
                line = fin.readline()
                result = re.findall('\s', line)
                if len(result) == 1:
                    line = fin.readline()
                else:
                    current["'name':'ru'"] = line.strip()
                    fout.write(json.dumps(current, ensure_ascii=False, indent=4))


convert("Lung", "test1")
#{name: {ru: '', en: ''}, synonims: ['', ''...], comments: [''...], children: [{}, {}...]}
