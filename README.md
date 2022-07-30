# tg_eye
Узнать и получить в файл активность пользователей из вашей телефоной книги вашего аккаунта

установка: 
git clone https://github.com/YuranIgnatenko/tg_eye

получение api_hash, api_id:
https://my.telegram.org/auth

<h2>Example:</h2>

import tg_eye as eye \
api_hash = 'scs0dc0siv7d76d8v9ecsd9ka9' \
api_id = '999999' \
namefile = "file.log" \
array_users = ["Иван Иванов", "Alex", "+79009009090", "U7"] \
delay_sec = 0 \
eye = eye.Eye(api_hash, api_id, namefile, array_users, delay_sec) \
eye.run() 

---------------------------------------------------------- \
console output: 
[Sat Jul 30 16:58:15 2022] write in file.log: ['UserStatusOffline:Иван Иванов', 'UserStatusOnline:Alex', 'UserStatusRecently:+79009009090', 'UserNotFound:U7'] \
---------------------------------------------------------- \
file output: 
Sat Jul 30 16:58:15 2022& UserStatusOffline:Иван Иванов, UserStatusOnline:Alex, UserStatusRecently:+79009009090, UserNotFound:U7
 
</h2>
Статусы активности:
<ul>
<li>UserStatusOnline (в сети) </li>
<li>UserStatusOffline (не в сети - доступно время последнего посещения)</li>
<li>UserStatusRecently (не в сети - не доступно время последнего посещения)</li>
<li>UserNotFound (пользователь отсутствует в телефонной книге вашего аккаунта - добавьте в мессенджере)</li>
</ul>
 </h3>
