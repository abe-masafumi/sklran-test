import csv
import re


def Molding(clean_index,csv_file_name):

  with open(csv_file_name) as f:
  # or
  # with open('1.2.test2.csv') as f:
      reader = csv.reader(f)
      l = [row for row in reader]
      l_length = len(l)
      columns_len = len(l[0])
      # print(columns_len)
      # print(len(l[338]))
      # print(l_length)
      
      for row in range(l_length):
        if len(l[row]) != columns_len:
          print(row)
        if row in clean_index:
          l[row] = list(map(lambda x : x.replace('\t',","),l[row]))
          text = ' '.join(l[row])
          text = text.split(",")
          text = list(map(lambda x : x.strip(),text))
          text = ' '.join(text)
          text = text.replace(' ',",")
          text = text.split(",")
          arr_len = len(text)
          for _ in range(columns_len-arr_len):
            text.append("")
          l[row] = text
          # print(l[row])
  return l,l_length,columns_len


def Molding_new(clean_index,csv_file_name):
  おかしいリスト = []

  with open(csv_file_name) as f:
  # or
  # with open('1.2.test2.csv') as f:
      reader = csv.reader(f)
      l = [row for row in reader]
      l_length = len(l)
      columns_len = len(l[0]) 
      # print(columns_len)
      # print(len(l[338]))
      # print(l_length)
      
      for row in range(l_length):
        try:
          if re.match("\D",l[row][27]) or l[row][24] == "計不":pass
          else: おかしいリスト.append(f"{row + 1},{l[row]}")
            
        except IndexError:
          print("rea-")
          おかしいリスト.append(f"{row + 1},{l[row]}")
          
        if row in clean_index:
          l[row] = list(map(lambda x : x.replace('\t',","),l[row]))
          text = ' '.join(l[row])
          text = text.split(",")
          text = list(map(lambda x : x.strip(),text))
          text = ' '.join(text)
          text = text.replace(' ',",")
          text = text.split(",")
          arr_len = len(text)
          for _ in range(columns_len-arr_len):
            text.append("")
          l[row] = text
          # print(l[row])
  return l,l_length,columns_len,おかしいリスト