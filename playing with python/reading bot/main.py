import reading

if __name__ == "__main__":
    texts = input("[+] Insert your document to read in mp3: ")

    #lang =
    #TEXT = Reading
    #TEXT
    test = reading.Languaje
    test.main_lang(test)
    test.select_languaje(test)

    name = input("[+] Choose a output name: ")

    read = reading.Reading(texts, test.lang_def, name)
    read.generate()
