from piazza_api import Piazza

def getLogin(where):
    data = None
    login = {'email':"", 'password':''}

    with (where, "r") as f:
        data = f.read()
    # expect "e@mail.com,password\n"
    emailEnd = data.find(',')

    login['email'] = data[:emailEnd]
    login['password'] = data[emailEnd+1:-1]

def main():
    login_info = getLogin()


if "__name__" == "__main__":
	main()
