class AI:
    def __init__(self):

        self.greeting = ["Hi anashex", "Hola", "Hi", "Que tal", "How are you ?", "Como estás ?", "como estas ?", "Todo bien ?" ]
        self.name = ["Name", "Whats your name ?", "Cuál es tu nombre", "How are you ?"]
        self.question = [""]
        self.creator = ["Quién te creó ?", "Quien te creó ?", "Who created you ?", "who created you ?", "quien te creó ?", "who is your creator ?"]
        self.whois = []
        self.nashee = ["xD", "XD", "jajajaja", "JAJAJA", "aaa", "bruh", "Bruh", "jajaja", "Who is Ian ?", "kk", "KK"]
        self.bye = ["Chau", "chau", "Bye", "bye", "Goodbye", "see you", "See ya", "see ya"]


    def check_msg(self, msg):
        if msg in self.greeting:
            return 'Hi how are you ?'
        elif msg in self.name:
            return 'My name is ANASHEX, nice to meet you'
        elif msg in self.creator:
            return 'I was created by Ian, he is a pro'
        elif msg in self.nashee:
            return 'XD :woozy_face: :poop: '
        elif msg in self.bye:
            return 'Bye, see you next time :)'
