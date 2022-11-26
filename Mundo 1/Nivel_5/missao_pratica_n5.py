from faker import Faker
import csv
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

l_pont=[': 5pts', ': 15pts', ': 22pts', ': 38pts',': 45pts',': 54pts',': 55pts',': 60pts',': 70pts',': 93pts',': 98pts',': 100pts']
l_nomes=['dois','quinze','vinte e dois','trinta','quarenta e quatro','cinquenta e um','sessenta e três','setenta e oito','oitenta e sete','noventa','noventa e oito','cem']
l_hist=['9', ' 10', ' 20', '35','40','56',' 67',' 80',' 84',' 93',' 98',' 100']

f = open('nomesepontuação.txt', 'w', newline='', encoding='utf-8')
fieldnames = ['first_name', 'last_name']

w = csv.writer(f)

fake = Faker('pt_BR')

for i in range(1,11):
    w.writerow([fake.name(), random.choice(l_pont)])
    print(fake.name(),random.choice(l_pont))
f.close()

plt.title('Histograma das Pontuações')
plt.xlabel('pontuação')
plt.ylabel('Probabilidade')
plt.hist(l_hist, 5, rwidth=0.9)
plt.show()

word_could_dict=Counter(l_nomes)
wordcloud = WordCloud(background_color='white', width = 1000, height = 600).generate_from_frequencies(word_could_dict)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

plt.close()