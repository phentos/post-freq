from piazza_api import Piazza
import time
import json

def getLogin(where='pwd.txt'):
    data = None
    login = dict()

    with open(where, "r") as f:
        data = f.read()
    # expect "e@mail.com,password"
    emailEnd = data.find(',')

    login['email'] = data[:emailEnd]
    login['password'] = data[emailEnd+1:]

    return login

def getClass(where='classtarget.txt'):
    target = ""

    with open(where, 'r') as f:
         target = f.read()
    
    return target

def cashMeOut(targetSighted):
    print("Time to get to work.")
    postDump = []
    totalCrawl = 0
    theJuice = targetSighted.iter_all_posts()
    for post in theJuice:
        totalCrawl += 1
        print("╪", end='', flush=True)
        if totalCrawl % 10 == 0:
            print(f"\n\tCrawl Total: {totalCrawl}")
            time.sleep(5)
        if 'student' in post['tags']:
            postDump.append(post)
        time.sleep(1)
    
    with open('postDump.json','w') as outFile:
        json.dump(postDump, outFile)


def main():
    begin = time.time()
    print("Clock started, get login info.")
    login_info = getLogin()
    target = getClass()

    p = Piazza()
    print(f"Logging in as: {login_info['email']}")
    p.user_login(login_info['email'], login_info['password'])
    print("We're in.")
    activeClass = p.network(target)


    cashMeOut(activeClass)
    print(f"\nDone. Total time: {(time.time()-begin)//60} minutes.\n")



main()