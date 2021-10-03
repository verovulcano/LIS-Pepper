import spacy

def text_processing(text):

	nlp = spacy.load('it_core_news_sm')
	doc = nlp(text)

	sentence = []

	for token in doc:

		if not(token.pos_ == 'DET' or token.pos_ == 'ADP'):
			
			sentence.append(token.lemma_)

	for n, elem in enumerate(sentence):

		if elem == 'mi':

			sentence[n] = 'tu'
			sentence.insert(n + 1, 'io')

		elif elem == 'ti':

			sentence[n] = 'io'
			sentence.insert(n + 1, 'tu')

		elif elem == 'favore':
			sentence[n] = 'per favore'
		
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

			if sentence[n + 1] == 'masticare':

				sentence[n] = 'gomma da masticare'
				sentence.remove(sentence[n + 1])

		elif elem == "c'":

			sentence.remove(sentence[n])

	return sentence