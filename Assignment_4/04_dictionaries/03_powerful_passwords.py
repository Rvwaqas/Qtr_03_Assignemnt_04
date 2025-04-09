from hashlib import sha256



def login(username,stored_logins,password):
        if stored_logins[username]==hash_password(password):
            return True
        return False




def hash_password(password):
    return sha256(password.encode()).hexdigest()



def main():
    stored_logins={
        "rvwaqas602@gmail.com":"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

    }
    print(login("rvwaqas602@gmail.com",stored_logins,"password"))
    print(login("rvwaqas602@gmail.com",stored_logins,"word"))


if __name__=="__main__":
    main()