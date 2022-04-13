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

        if row in clean_index:
          l[row] = list(map(lambda x : x.replace('\t',","),l[row]))
          text = ' '.join(l[row])
          text = text.split(",")
          text = list(map(lambda x : x.strip(),text))
          text = ' '.join(text)
          text = text.replace(' ',",")
          text = text.split(",")
          arr_len = len(text)
          for _ in range(32-arr_len):
            text.append("")
          l[row] = text
          # print(l[row])
  return l,l_length,columns_len


def Molding_new(clean_index,csv_file_name):
  おかしいリスト = []
  with open(csv_file_name) as f:
      reader = csv.reader(f)
      l = [row for row in reader]
      l_length = len(l)
      columns_len = len(l[0]) 
      
      for row in range(l_length):
        if row in clean_index:
          l[row] = list(map(lambda x : x.replace('\t',",").strip(),l[row]))
          text = ' '.join(l[row])
          text = text.replace(' ** ',"**,")
          text = text.replace(' ',",")
          text = text.replace('),,,,,',"),,,")
          text = text.replace('),,,,',"),,,")
          # print(text)
          text = text.split(",")
          l[row] = text
          
        if len(l[row]) > 32:
          del l[row][32:]

        if len(l[row]) < 32:
          for _ in range(32-len(l[row])):
            l[row].append("")
            # print(l[row][0], len(l[row]))
        # if row == 2867:
        #   print(l[row][24])

        try:
          if re.match("\D",l[row][27]) and l[row][26] == "" and l[row][25] == "" and l[row][29] == "":pass
          elif l[row][24] == "計不" :pass
          # re.正規表現使いたい
          elif l[row][24] == "464(+4)":pass
          elif l[row][24] == "462(+5)":pass
          elif l[row][24] == "436(-3)":pass
          elif l[row][24] == "414(+12)":pass
          elif l[row][24] == "397(-5)":pass
          elif l[row][24] == "454(-22)":pass
          elif l[row][24] == "499(+2)":pass
          elif l[row][24] == "459(-6)":pass
          elif l[row][24] == "435(-9)":pass
          elif l[row][24] == "484(-3)":pass
          elif l[row][24] == "562(-8)":pass
          elif l[row][24] == "542(+20)":pass
          
          elif row == 0:pass
          else: 
            おかしいリスト.append(f"{row + 1}-{l[row][0]}-{','.join(l[row])}")
            if l[row]=="ここー✨":pass
            else:l[row].insert(0, "ここー✨"),l[row].pop(-1)
        except :
          print(f"indexエラー: {row+ 1} - {len(l[row])}")
            
        # if len(l[row]) == columns_len:pass
        # else: 
          # print(f"{l[row][0]} : {row + 1}:{len(l[row])}")
          # for _ in range(columns_len-len(l[row])):
          #   l[row].append("")
          # print(f"{l[row][0]} : {row + 1}:{len(l[row])}")
            
          
  return l,l_length,columns_len,おかしいリスト