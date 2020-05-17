import re, json

def convert_txt_to_json(path):
    with open(path, "r") as f:
        text = f.read()

    # to remove references
    match = text.rfind("References")
    if match:
        text = text[:match]

    # to remove title and authors
    list_of_chunks = re.split("\n\s?\n+", text)
    list_of_chunks.pop(0)
    list_of_chunks.pop(0)

    # to remove headings
    for chunk in list_of_chunks:
        regexObj = re.compile("^[0-9]")
        result = regexObj.match(chunk)
        if result != None:
            list_of_chunks.remove(chunk)

    # to split chunks into first sentence and remainder
    final = {}
    for chunk in list_of_chunks:
        chunk = chunk.replace("\n", "")     # chunk is a str
        chunk = re.sub("\s+", " ", chunk)
        chunk = re.split("[.?!]\s+", chunk, maxsplit=1)
        if len(chunk) == 2 and "" not in chunk:
            first_sentence, rmd_block = chunk[0], chunk[1]
            final[first_sentence] = rmd_block

    # to convert dictionary into json format
    with open(path+".json", "w") as f:
        json.dump(final, f)


convert_txt_to_json("1209.1318.pdf.txt")