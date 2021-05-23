from gensim.test.utils import common_texts,datapath
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import math

fig = plt.figure()
common_dictionary = Dictionary(common_texts)
common_curpus = [common_dictionary.doc2bow(text) for text in common_texts]

print("common_texts: {}".format(common_texts))
print("common_dictionary: {}".format(common_dictionary))
print("common_curpus: {}".format(common_curpus))

# train the model on curpus
lda = LdaModel(common_curpus, num_topics=3)

### Save model to disk
# temp_file = datapath("model")
# lda.save(temp_file)
###

### Create a new corpus, made of Previously  unseen documents

#sample_texts = [
#     ['computer','time','graph'],
#     ['survey','response','eps'],
#     ['human','system','computer']
# ]
#other_corpus = [common_dictionary.doc2bow(text) for text in other_texts]
#
#unseen_doc = other_corpus[0]
#vector = lda[unseen_doc]

###
nb_topics=3
nb_words=10
# def plot_top_words(lda, nb_topics, nb_words):
top_words = [[word for word,_ in lda.show_topic(topic_id, topn=50)] for topic_id in range(lda.num_topics)]
top_betas = [[beta for _,beta in lda.show_topic(topic_id, topn=50)] for topic_id in range(lda.num_topics)]
gs = GridSpec(round(math.sqrt(nb_topics))+1,round(math.sqrt(nb_topics))+1)
gs.update(wspace=0.5, hspace=0.5)
plt.figure(figsize=(20,15))
for i in range(nb_topics):
    ax = plt.subplot(gs[i])
    plt.barh(range(nb_words), top_betas[i][:nb_words], align='center', color='blue', ecolor='black')
    ax.invert_yaxis()
    ax.set_yticks(range(nb_words))
    ax.set_yticklabels(top_words[i][:nb_words])
    plt.title("Topic "+str(i))

    fig.savefig("lda_test.jpg")
print(top_words[1])
# plot_top_words(lda,3,10)