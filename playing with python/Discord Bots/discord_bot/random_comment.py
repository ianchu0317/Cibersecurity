from random import choice

aiyu = ["pay attention to the teacher :woozy_face:", "are you stupid ?", "wtf", "OF COURSE", ":poop:"]

troll = ["YES", "Shie SHie", "Thanks", "You're Welcome", "No gracias", "De nada", "JAJAJA"]

spanish = ["hahaha","Equis DHE","acaso eres estupido ?", "No mamess", "Feo", "callate", "No pedi tu opinion", "rata callejera", "no me subestimes", "LOL", "xD", "por ahi no", "Gaby gay"]

anime = ["senpaii", "omae wa mo shin deiru", "onii-chan", "chidori", "rasengan"]

lists = [aiyu, troll, spanish, anime]


def choice_response():
	l = choice(lists)
	return choice(l)
