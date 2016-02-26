import json

def convert(fname_in, fname_out):
    fieldnames = ("name", "ru", "en", "synonims", "comments", "children")
 
    with open(fname_in, "r") as fin, open(fname_out, "w") as fout:
 
        fout.write("[\n")
                
        for line in fin:
            count = 0
            if line == " ":
                count = 0
                line = fin.readline()
            elif line == "\n":
                count = 0
                line = fin.readline()
            elif line[1:2] == " ":
                if line == "\n":
                    count = 0
                    line = fin.readline()
                elif line[3:4] == " ":
                    if count == 1:
                        fout.write(json.dumps({"children":line[3:-1]}, ensure_ascii=False, indent=4) + "\n")
                        count = 0
                        line = fin.readline()
                else:
                    fout.write(json.dumps({"synonims":line[1:-1]}, ensure_ascii=False, indent=4) + "\n")
                    line = fin.readline()
            
            else:
                fout.write(json.dumps({"name":line[:-1]}, ensure_ascii=False, indent=4) + "\n")
                line = fin.readline()
        fout.write("]")
            
        


convert("Lung", "test1")
#{name: {ru: '', en: ''}, synonims: ['', ''...], comments: [''...], children: [{}, {}...]}
