#7.8
surpirse=['Groucho','Chico','Harpo']
#7.9
surpirse_last_word=[*surpirse[:2],surpirse[2].lower()]
surpirse_first_word=[surpirse[-1].upper(),*surpirse[-2::-1]]
print(surpirse_last_word,surpirse_first_word)