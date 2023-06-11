# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.
import re

def list_of_ten_dublicated_words(big_string):
    list_of_words = re.sub('[^А-Яа-я ]','',big_string .lower()).split(' ') # все символы сделали строчными, потом удалили все символы кроме букв
    # и рассплитили строку по пробелам. Врезультате получился список из букв и слов

    for el in list_of_words:
        if len(el) <= 1: list_of_words.remove(el)
    # удалили все буквы, в списке остались только словa

    max_count = 0
    max_word = ''
    list_of_max_count_words = []

    for _ in range(10): # список из 10 элементов
        for word in list_of_words: # перебираю все слова в списке
            if word in list_of_max_count_words: continue # если данное слово уже ести в результирующем списке то пропускаем итерацию
            if list_of_words.count(word) > max_count: # далее определяется наиболее повторяемое слово 
                max_count = list_of_words.count(word)
                max_word = word
        #if max_word not in list_of_max_count_words: 
        list_of_max_count_words.append(max_word) # добавляем новое "популярное" слово в результирующий список
        max_count = 0
        max_word = ''
    return list_of_max_count_words



big_string = '3. КАК НАДО ЗНАТЬ РАСПОРЯЖЕНИЯ НАЧАЛЬСТВА\
Кроме требований уставов, есть еще требования начальников. Эти требования ты должен знать так же, как уставы, и уметь всегда верно и хорошо исполнять.\
Если какое-нибудь приказание передано началь-ником тебе лично или через кого-нибудь, то поста-райся хорошенько понять, что тебе приказано: если не понял, переспроси, попроси объяснить, что тебе непонятно, и тогда ты можешь точно и хорошо его исполнить.\
Приказания начальника должны исполняться бы-стро, но толково; без толку не спеши, но и с толком не копайся; нужна толковая быстрота.\
Выучись быстро понимать начальника и быстро исполнять его приказания и распоряжения. Старайся запомнить эти распоряжения для того, чтобы началь-нику не пришлось повторять тебе их в другой раз.\
Приказания и распоряжения, которые надо испол-нять постоянно, лучше всего записывать у себя: гак ты и запомнишь лучше, а придется к случаю - есть где и справиться.\
4. КАК ПОСТУПАТЬ, ЕСЛИ ЧЕГО НЕ ЗНАЕШЬ \
Никогда ничего не делай наобум, не зная наверно, что так именно надо поступать. В таком случае всегда лучше спроси или своего товарища, или своего нспо- \
10. КАК НАДО ОТНОСИТЬСЯ К СВОИМ ПОДЧИНЕННЫМ\
Будь ласков с твоими  подчиненными, входи в их нужды, заботься об них. Увидишь кого в горе - не проходи мимо; утешь, помоги чем можешь: советом или ходатайством перед начальством. 11с гони, если кто-нибудь из твоих подчиненных придет спросить тебя о чем-нибудь, даже не касающемся службы, и не смейся, если даже он спросит глупость. Всегда обхо-дительно растолкуй и объясни бойцу, что он не пони-мает, или посоветуй, как надо сделать. Тогда все твои подчиненные будут видеть, что ты их действительно любишь, что их горе твое горе, их беда - твоя беда, и каждый с доверием будет к тебе обращаться во всякой своей нужде, зная, что ты им поможешь и научишь.\
Чаще разговаривай с подчиненными о службе. Не думай, что если ты отделал «направо» да «налево», да рассказал в положенный час. в чем состоит воинская дисциплина так и прав. Нет, ты в свободное время приди да поговори с бойцами; любовно и хорошо го-вори с ними, как отец с детьми, обо всем, что службы касается, что они увидели и узнали. «Хорошую речь хорошо и слушать». Говори с ними хорошо, занима-тельно, чтобы они тебя не по обязанности слушали, а чтобы это им было приятно, чтобы они сами хотели услыхать тебя и поговорить с тобой.'

print(list_of_ten_dublicated_words(big_string))