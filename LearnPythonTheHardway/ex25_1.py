from Projects import ex25
# -*- coding: utf-8 -*-

sentence = "All good things come to those who wait."#példamondat
words = ex25.break_words(sentence)                  #példamondat szavakra tagolása
print(words)

sorted_words = ex25.sort_words(words)               #tagolt szavak abc rendbe sorolása
print(sorted_words)

ex25.print_first_word(words)                        #első szó kiírása
ex25.print_last_word(words)                         #utolsó szó kiírása


ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
# print(sorted_words)

sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
