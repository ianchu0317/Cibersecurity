import socket

addr = input("[+] Insert your ip: ")
port = 22
wordlist = input("[+] Insert your worldlist: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This line of code doesn´t work for me, so i will do another bellow
#with open(wordlist, "r") as word_list:
#    for word in word_list:
#        word = word_list.readline()
#        print(word)
#sock.connect()


word_list = open(wordlist, "r")

print (word_list.readline())
#for word in word_list:
#    x = word_list.readline()
#    print(word)


