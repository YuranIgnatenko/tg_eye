# tg_eye
Узнать и получить в файл активность пользователей из вашей телефоной книги вашего аккаунта

git clone https://github.com/YuranIgnatenko/tg_eye

<h1>
Example:
import tg_eye as eye
 
api_hash = 'scs0dc0siv7d76d8v9ecsd9ka9'
api_id = '999999'
namefile = "file.log"
array_users = ["Иван Иванов", "Alex", "+79009009090"]
 
delay_sec = 0
eye = eye.Eye(api_hash, api_id, namefile, array_users, delay_sec)
eye.run()
</h1>
