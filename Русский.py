def reverse_translate(word: str) -> str:
	words = {"я": "I", "ты": "you", "он": "he", "она": "she", "оно": "it", "не": "not", "нет": "no", "знат": "know", "тот": "that", "этот": "this", "делат": "do", "кто": "who", "что": "what", "где": "where", "как": "as", "почему": "why", "вот": "here is", "ваш": "your", "твой": "your", "ден": "day", "чувство": "feeling", "о": "concerning", "у": "by / at", "на": "on / to", "с": "with / for", "из": "for / from", "к": "to", "его": "his", "её": "her", "их": "their", "мы": "we", "вы": "you", "они": "they", "обедать": "dine", "обеходь": "daily practice", "год": "year", "новый": "new", "сейчас": "now", "есть": "there is / there are", "кушат": "eat", "здес": "here", "ресторан": "restauraunt", "сегоден": "today", "меню": "menu", "за": "for", "нуждаться": "need", "компютаная": "computer", "знание": "knowledge" }
	all = []
	for ruword in words.keys():
		all.append(ruword.lower())
	if word in all:
		return words[word]


def Translate(sentence: str) -> str:
	L = sentence.strip().split(' ')
	print(L)
	sentence = ""
	count = 0
	for word in L:
		curr_word = reverse_translate(word)
		if curr_word == None:
			continue
		if count == 0:
			curr_word.capitalize()
		sentence += curr_word
		sentence += " "
		count += 1
	print(sentence)
		

Translate("она не знат")
Translate("нет я не знат")
Translate("что ваш чувство о её")
Translate("как её чувство о её ден")
Translate("что есть кушат здес на этот ресторан меню")
Translate("что вы делат сегоден")
#speech = str(input("Enter a line of Russian Language: "))
#Translate(speech.lower())

""" Charles Thomas Wallace Truscott """
""" Working on this while in the Tweed Mental Hospital """
