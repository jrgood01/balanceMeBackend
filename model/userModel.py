class user():
    def __init__(self, id=-1, first_name='', last_name='', account_type=0,password='',email='', points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_type = account_type
        self.password = password
        self.email = email
        self.id = id
        self.points = points
    def sync(self):
        add_user = ("INSERT INTO users "
               "(first_name, last_name, account_type,password,email,points)"
               "VALUES ('%s', '%s', %d, '%s', '%s', %d)" % (self.first_name, self.last_name, self.account_type, self.password, self.email, 0))
        cursor.execute(add_user)
        return 

    def updateEmail(self, newEmail):
        self.email = newEmail
        update_qeury = ("UPDATE users "
                    "SET `email` = '%s' "
                    "WHERE `id` = %d" % (self.email, self.id)
        )
        print(update_qeury)
        cursor.execute(update_qeury)
        return
        
    def updateFirstName(self, newFirstName):
        self.first_name = newFirstName
        update_qeury = ("UPDATE users "
                    "SET `first_name` = '%s' "
                    "WHERE `id` = %d" % (self.first_name, self.id)
        )
        print(update_qeury)
        cursor.execute(update_qeury)
        return

    def updateLastName(self, newLastName):
        self.last_name = newLastName
        update_qeury = ("UPDATE users "
                    "SET `last_name` = '%s' "
                    "WHERE `id` = %d" % (self.last_name, self.id)
        )
        print(update_qeury)
        cursor.execute(update_qeury)
        return

    def updatePoints(self, newPoints):
        self.points = newPoints
        update_qeury = ("UPDATE users "
                    "SET `points` = '%s' "
                    "WHERE `id` = %d" % (self.points, self.id)
        )
        print(update_qeury)
        cursor.execute(update_qeury)
        return

    @staticmethod
    def getAll():
        get_user = "SELECT * FROM users"
        cursor.execute(get_user)
        results = cursor.fetchall()
        usr_str = "{"
        for userData in results:
            usr_str += str(user(userData[0], userData[1], userData[2],
             userData[3], userData[4], userData[5], userData[6]).dict()) + ","
        return usr_str[:-1] + "}"
    def dict(self):
        return {"first_name": self.first_name, "last_name": self.last_name,
        "account_type": self.account_type, "password": self.password, "email": self.email, "id": self.id, "points": self.points}
