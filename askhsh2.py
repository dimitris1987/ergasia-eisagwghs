import urllib.request
import json
import datetime

cur_date = datetime.datetime.now()

#Έλεγχος αριθμών από τον χρήστη
nums = []
arithmoi = []
for z in range(1,81):
    arithmoi.append(z)
for i in range(1,11):
    while True:
        x = int(input("Εισάγετε τον " + str(i) + "ο αριθμό  (1 εως 80)"))
        if x in arithmoi and x not in nums:
            break
    nums.append(x)


def compare_lists(l1, l2):
    s = 0
    for i in l1:
        if i in l2:
            s += 1
    return s


epityxies = []
dates = []
for i in range(31):
    cur_date = cur_date - datetime.timedelta(days=1)
    date_str = cur_date.strftime("%d-%m-%Y")
    url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json' % date_str
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req).read().decode('utf-8')
    data = json.loads(response)
    klhrwseis = data['draws']['draw']

    sum = 0
    for k in klhrwseis:
        tmp = k["results"]
        x = (compare_lists(nums, tmp))
        if x > 4:
            sum += 1

    epityxies.append(sum)
    dates.append(date_str)

hmera = dates[epityxies.index(max(epityxies))]
print("Την " + hmera +" ο χρήστης έχει τις περισσότερες επιτυχίες!")
