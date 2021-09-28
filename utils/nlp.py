import spacy

def text_processing(text):

	nlp = spacy.load('it_core_news_sm')
	doc = nlp(text)

	sentence = []

	for token in doc:

		sentence.append(token.lemma_)

	for n, elem in enumerate(sentence):

		if elem == 'mi':

			sentence[n] = 'tu'
			sentence.insert(n + 1, 'io')

		elif elem == 'ti':

			sentence[n] = 'io'
			sentence.insert(n + 1, 'tu')

		elif elem == 'il' or elem == 'lo' or elem == 'la' or elem == 'i' or elem == 'gli' \
		or elem == 'le' or elem == 'a' or elem == 'uno' or elem == 'c\'':

			sentence.remove(elem)

		elif elem == 'per':

			if sentence[n + 1] == 'favore':

				sentence[n] = 'perfavore'
				sentence.remove(sentence[n + 1])

		elif elem == 'grazia':

			sentence[n] = 'grazie'

		elif elem == 'panare':

			sentence[n] = 'panino'

		elif elem == 'coca':

			if sentence[n + 1] == '-':
				if sentence[n + 2] == 'cola':

					sentence[n] = 'coca-cola'
					sentence.remove(sentence[n + 1])
				sentence.remove(sentence[n + 1])

		elif elem == 'gomma':

			if sentence[n + 1] == 'da':
				if sentence[n + 2] == 'masticare':

					sentence[n] = 'gomma da masticare'
					sentence.remove(sentence[n + 1])
				sentence.remove(sentence[n + 1])

	return sentence