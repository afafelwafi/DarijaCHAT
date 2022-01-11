from gensim.corpora import WikiCorpus

def make_corpus(in_f, out_f):

  """Convert Wikipedia xml dump file to text corpus"""

  output = open(out_f, 'w')
  wiki = WikiCorpus(in_f)

  for i, text in enumerate(wiki.get_texts()):
    output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')

    if (i % 1000 == 0):
      print('Processed ' + str(i) + ' articles')
  print('Processing complete!')  
  output.close()
  

