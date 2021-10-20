from urllib.request import install_opener, urlopen

test_url  ="http://olympus.realpython.org/profiles/aphrodite"
def readtostring(url):
    page = urlopen(url)
    page_bytes=page.read()
    page_html= page_bytes.decode("utf-8")
    return page_html

def find_sentence(text,word):
    text =text.split(".")
    for sentence in text:
        if word in sentence:
            yield sentence
    # while text.count(".")!=0:
    #     stop_pos= text.index(".")
    #     if word_pos>stop_pos:
    #         text=text[stop_pos:]
    #         print(text)
    #     else:
    #         if text.count(".")>0:
    #             text=text[:text.index(".")]
    # while text.count("\n")!=0:
    #     stop_pos= text.index("\n")
    #     if word_pos>stop_pos:
    #         text=text[stop_pos:]
    #     else:
    #         if text.count("\n")>0:
    #             text=text[:text.index("\n")





def check_for_string(url,*strings):
    counts=[]
    sentences=[]
    for string in strings:
        page=readtostring(url)
        num=page.count(string)
        if num==0:
            sentences.append(f"{string} does not appear")
            continue
        counts.append(num)
        print(num)
        a=0
        index=0 -len(string)
        while a<num:
            a+=1
            index= page[index+len(string):].index(string)
            
            for instance in find_sentence(page,string):
                if instance not in sentences:
                    sentences.append(instance)
    sentences=clean_links(clean_links(clean_links(sentences)))        
    cleanup(sentences)

def spalpha(k):
    k=k.replace(' ','')
    if k.isalpha():
        return True
def clean_links(strings):
    for i in range(len(strings)):
        sentence=strings[i]
        if sentence.count("<a ")==0:
            continue
        sentence=sentence.replace("</a>",' ')
        semi_list= sentence.split("<a ")
        for i in range(len(semi_list)):
            if not "href" in semi_list[i]:
                continue
            else:
                if semi_list[i].count(">")==0:
                    semi_list.pop(i)
                    continue
                else:
                    start=semi_list[i].index(">") +1
                    semi_list[i]=semi_list[i][start:]
                    strings[i]= ' '.join(semi_list)
    return strings
    











def cleanup(things):
    for i in range(len(things)):
        while True:
            if not spalpha(things[i][:3]):
                things[i]=things[i][1:]
            else:
                break
        print(things[i])
        print()
                    
                    







g11= "https://www.reddit.com/r/girlsfrontline/comments/q8lrnj/mama_g11/"
bo= "https://en.wikipedia.org/wiki/Balloon_(2018_film)"

print(check_for_string(g11,"g11"))
