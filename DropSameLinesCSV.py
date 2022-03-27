import pandas as pd
sec_uk = pd.read_csv('all_shares.csv')
filed_date = pd.read_csv('filed_date.csv')
len_sec = len(sec_uk.values)
len_files = len(filed_date.values)
i = 0
j = 0
while i < len_sec:
  j = 0
  while j < len_files:
    if (sec_uk.values[i] == filed_date.values[j]).all():
      sec_uk = sec_uk.drop(sec_uk.index[[i]])
      filed_date = filed_date.drop(filed_date.index[[j]])
      len_sec -= 1
      len_files -= 1
    else:
      j += 1
  i += 1
# - сделать для n>2 файлов: 1) возможность удалить строку, если она есть во всех файлах 2) возможность удалить строку, если она есть хотя бы в 2 файлах 3) set уникальных
# строк из каждого файла
# - сделать приложение: выбираешь с компа 2 файла, загружаешь в него. Выходные данные: 1) set уникальных строк из первого + set уникальных строк из второго 2) индекс строки в первом 
# файле + индекс такой же строки во втором файле 3) индексы уникальных строк
# - возможность разного формата: xlsx, tsv, csv
