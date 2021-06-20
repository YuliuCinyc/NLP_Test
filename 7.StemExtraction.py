from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
stemmer = PorterStemmer()
print(stemmer.stem('working'))
print(stemmer.stem('worked'))
print("——————————————————————————————————————————————")
print(SnowballStemmer.languages)
french_stemmer = SnowballStemmer('french')
print(french_stemmer.stem("French word"))