import json

def convert(fname_in, fname_out):
    fieldnames = ("name", "ru", "en", "synonims", "comments", "children")
 
    with open(fname_in, "rt", encoding="utf-8") as fin, \
            open(fname_out, "wt", encoding="utf-8") as fout:
 
        fout.write("[\n")
        data = fin.readlines()  
        print(data[0])
        
        for obj in data:
            if obj == " ":
                continue
            elif obj[0] == " ":
                continue
            elif obj[1] == " ":
                fout.write(json.dumps({synonims:obj}, ensure_ascii=False, indent=4) + "\n")                
            else:
                fout.write(json.dumps({"name":obj[:-1]}, ensure_ascii=False, indent=4) + "\n")
        

                fout.write("]")
convert("Lung", "test1")
#{name: {ru: '', en: ''}, synonims: ['', ''...], comments: [''...], children: [{}, {}...]}
