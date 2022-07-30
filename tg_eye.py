from tabnanny import check
from telethon.sync import TelegramClient
import time
import os


class Eye():
    def __init__(self, api_hash, api_id, namefilelog, array_phones, delay_sec):
        self.ErrorFindUser = "UserNotFound"
        self.api_hash = api_hash #'e4fa500de7caf508c7fd24c340b813fe'
        self.api_id = api_id #'908250'
        self.namefile = namefilelog #"file.log"
        self.array_users = array_phones #["Настя", "+79156099431", "Полина Кренделёк"]
        self.delay_sec = delay_sec
        self.symsplit = "&"
        self.client = TelegramClient("newSessionEye", api_id, api_hash)
        self.client.start()
        for dialog in self.client.iter_dialogs():
            break
        self.check_file()

    def check_file(self):
        if os.path.isfile(self.namefile) == False:
            with open(self.namefile, "w") as file:
                pass

    def get_status(self, user_name):
        try:
            acc = self.client.get_entity(user_name)
            res = f"{acc.status}".split("(")[0]+":"+user_name
        except ValueError:
            return self.ErrorFindUser + ":" + user_name
        return res   
    
    def write_file_line(self, ar_status):
        line = ""
        for status in ar_status:
            line += " " + status
        with open(self.namefile, "a") as file:
            file.write(time.asctime() + self.symsplit + line + "\n")

    def read_file_line(self):
        with open(self.namefile, "r") as file:
            data = file.read()
        if data == "":
            return []
        if data.index("\n") != -1:
            data_last = data.split("\n")[-2]
        else:
            data_last = data
        data_last = data_last.split(self.symsplit)[1]
        data_last = data_last.strip(" ").split(" ")
        dt = []
        for status in data_last:
            dt.append(status.split("\n")[0])
        return dt

    def check_not_eq_status(self, ar1, ar2):
        """
        ['UserStatusOnline','UserStatusOnline']
        ['UserStatusOnline','UserStatusOffline']
        return false
        """
        if len(ar1)!=len(ar2):
            return True
        for ind in range(len(ar1)):
            if ar1[ind] != ar2[ind]:
                return True
        return False

    #run loop write mode omline users 
    def run(self, flag_bool_out=True):
        self.check_file()
        while True:
            if self.delay_sec > 0:
                time.sleep(self.delay_sec)
            array_status = []
            for user in self.array_users:
                array_status.append(self.get_status(user))
            file_status = self.read_file_line()
            if len(file_status) == 0:
                file_status = list("nil" for i in self.array_users)
            not_equil_status = self.check_not_eq_status(file_status, array_status)
            if not_equil_status :
                self.write_file_line(array_status)
                if flag_bool_out:
                    print(f"[{time.asctime()}] write in {self.namefile}: {array_status}")

# Example
# 
# api_hash = 'scs0dc0siv7d76d8v9ecsd9ka9'
# api_id = '999999'
# namefile = "file.log"
# array_users = ["Иван Иванов", "Alex", "+79009009090"]
# 
# delay_sec = 0
# eye = Eye(api_hash, api_id, namefile, array_users, delay_sec)
# eye.run()
