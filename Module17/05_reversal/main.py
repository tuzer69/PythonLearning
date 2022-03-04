text = 'ddnnsdhПриветhsdsdlkd'

result = text[:text.index('h') + 1] \
		 + text[text.rindex('h') - 1:text.index('h'): -1] \
		 + text[text.rindex('h'):]

print("Разворот: ", result)