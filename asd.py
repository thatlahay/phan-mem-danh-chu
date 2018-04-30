import sys
database = {'some','pop','mario',}
tudung = 0
#Chương trình sẽ chạy cho đến khi người dùng nhập sai
while True:
 for word in database:
   #Cho người chơi xem từ cần nhập
   print("[*] "+word)
   #Yêu cầu người chơi nhập từ
   player_input = input('[+] Hãy nhập từ: ')
   if player_input == word:
     tudung = tudung + 1
   else:
     print('Wrong')
     print('Bạn đúng được %s từ' % tudung)
     sys.exit()