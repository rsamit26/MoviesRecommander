import math
import json
f = open("input.json","r")
s= f.read()
movies = json.loads(s)
print(t)

# Keywords genrator

st= open("SmartStoplist.txt","r")
smt = st.read()
s= f.read()
SmartStoplist = []
smts = smt.split('\n')
for word in smts:
    SmartStoplist.append(word)

def Keywords(string):
    counts = dict()
    comp_list  = []
    ss = string.replace(',', '');
    pp = ss.replace('.','')
    tt = pp.replace(':','')
    words = tt.split()
    for word in words:
        lword = word.lower()
        if lword in SmartStoplist:
            continue
        else:
            counts[lword] = counts.get(lword, 0) + 1

    lst = list()
    for k,v in counts.items():
        lst.append((v, k))
    lst.sort()

    for v, k in lst:
      comp_list.append(k)


    return comp_list



def compare_storyline(list1,list2):
    count =0
    nlst = list()
    countlist = list()
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] in list2[j]:
                count = count + 1
                nlst.append(list1[i])
            else:continue

    for word in nlst:
        if word not in countlist:
            countlist.append(word)
        else:
            continue
    return (countlist)

    # end of keyword genrator




# get genre


def get_genre(dict, title):
    genre_list = []
    for i in range(len(movies)):
        if title in movies[i]['title']:
            genre_list = (movies[i]['genre'])
        else:continue
    return genre_list
# get Stars


def get_stars(dict, title):
    stars_list = []
    for i in range(len(movies)):
        if title in movies[i]['title']:
            stars_list = (movies[i]['stars'])
        else:continue

    return stars_list


for i in range(len(movies)):
    if movies[i]['metascore'] == '':
        movies[i]['metascore'] = '50'
    else:
        continue

shorted_movies  = dict()
nlist = list()
lst =list()
for j in range(3):
    a = Keywords(movies[j]['storyline'])
    genres = get_genre(movies,movies[j]['title'])
    stars = get_stars(movies,movies[j]['title'])
    r_j = float(movies[j]['rating'])
    m_j = float(movies[j]['metascore'])
    mean_j = r_j/10.0
    for i in range(len(movies)):
        b = Keywords(movies[i]['storyline'])
        r = float(movies[i]['rating'])
        m = float(movies[i]['metascore'])
        mean_i = r / 10.0
        cos_i = math.acos(mean_i)
        cos_j = math.acos(mean_j)
        sim = math.cos(cos_i - cos_j)
        for gen in range(len(genres)):
            if genres[gen] in movies[i]['genre']:
                sim = sim +.07
            else:continue
        if movies[j]['director'] in movies[i]['director']:
            sim = sim + .1

        for st in range(len(stars)):
            if stars[st] in movies[i]['stars']:
                sim = sim + .08
            else:continue
        count = len(compare_storyline(a,b))
        if count > 2:
            sim  = sim + .1




        shorted_movies[movies[i]['title']] = shorted_movies.get(movies[i]['title'], sim)
    for k,v in shorted_movies.items():
        lst.append((v,k))
    lst.sort(reverse=True)
    #print(lst[:11])
    print("\n")
    for k,v in lst:
        nlist.append(v)
    print(movies[j]['title'], nlist[1:11])
    nlist.clear()
    lst.clear()
    shorted_movies.clear()


