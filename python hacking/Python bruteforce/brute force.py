import hashlib, time

hash = input("Introduce your hash: ")
wordlist = input("Introduce your wordlist: ")


#try:
with open(wordlist, "r") as word_list:
	for word in word_list:
		word = word_list.readline()
		word_hash = hashlib.md5(word.encode("utf-8")).hexdigest()
		print(f"{hash} == {word}")
		if word_hash == hash:
			print(f"The password is {word}")
			break


#except KeyboardInterrupt:
#	print("The command has been anuled")
#	time.sleep(5)
#	quit()

#except:
#	print("There is an error ocurred")
#	quit()
