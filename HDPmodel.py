!pip install tomotopy
import tomotopy as tp

# Train NMF model.

mdl = tp.HDPModel(min_cf=0, min_df=0, rm_top=0, initial_k=30, alpha=1, eta=0.01, gamma=1)
for line in open('bigrammed.txt'):
    mdl.add_doc(line.strip().split())

for i in range(0, 1000, 100):
    mdl.train(100)
    print('Iteration: {}\tLog-likelihood: {}'.format(i, mdl.ll_per_word))

for k in range(mdl.k):
    print('Top 10 words of topic #{}'.format(k))
    print(mdl.get_topic_words(k, top_n=10))

mdl.summary()

