from translate import Translator
print("Test de traducción simultanea")
translator=Translator(from_lang = "es",to_lang="en")
print(type(translator))
sentence=input(f"Traducir español a ingles \n")
# print(type(sentence))
translation=translator.translate(sentence)
# print(type(translation))
print(translation)