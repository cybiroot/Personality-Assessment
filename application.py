import pandas as pd
from tkinter import *
from tkinter import ttk

df = pd.read_csv('MBTI 500.csv', delimiter = ',')
df = df.drop_duplicates()

def solution(word):
  counts = df['posts'].str.count(word)

  wo_INTJ = wo_INTP = wo_ISFJ = wo_ISFP = wo_ISTJ = wo_ISTP = wo_ENFJ = wo_ENFP = wo_ENTJ = wo_ENTP = wo_ESFJ = wo_ESFP = wo_ESTJ = wo_ESTP = wo_INFJ = wo_INFP = 0
  
  isUseless = True
  for i in range(106067):
    if counts[i] != 0:
      isUseless = False

    if i <= 22427:
      wo_INTJ += counts.iloc[i]
    elif i > 22427 and i <= 47388:
      wo_INTP += counts.iloc[i]
    elif i > 47388 and i <= 48038:
      wo_ISFJ += counts.iloc[i]
    elif i > 48038 and i <= 48913:
      wo_ISFP += counts.iloc[i]
    elif i > 48913 and i <= 50156:
      wo_ISTJ += counts.iloc[i]
    elif i > 50156 and i <= 53580:
      wo_ISTP += counts.iloc[i]
    elif i > 53580 and i <= 55114:
      wo_ENFJ += counts.iloc[i]
    elif i > 55114 and i <= 61281:
      wo_ENFP += counts.iloc[i]
    elif i > 61281 and i <= 64236:
      wo_ENTJ += counts.iloc[i]
    elif i > 64236 and i <= 75961:
      wo_ENTP += counts.iloc[i]
    elif i > 75961 and i <= 76142:
      wo_ESFJ += counts.iloc[i]
    elif i > 76142 and i <= 76502:
      wo_ESFP += counts.iloc[i]
    elif i > 76502 and i <= 76984:
      wo_ESTJ += counts.iloc[i]
    elif i > 76984 and i <= 78970:
      wo_ESTP += counts.iloc[i]
    elif i > 78970 and i <= 93933:
      wo_INFJ += counts.iloc[i]
    elif i > 93933 and i <= 106067:
      wo_INFP += counts.iloc[i]

  if isUseless:
    return None

  rslt_df1 = pd.DataFrame([ ["INTJ", wo_INTJ],
                         ["INTP", wo_INTP],
                         ["ISFJ", wo_ISFJ],
                         ["ISFP", wo_ISFP],
                         ["ISTJ", wo_ISTJ],
                         ["ISTP", wo_ISTP],
                         ["ENFJ", wo_ENFJ],
                         ["ENFP", wo_ENFP],
                         ["ENTJ", wo_ENTJ],
                         ["ENTP", wo_ENTP],
                         ["ESFJ", wo_ESFJ],
                         ["ESFP", wo_ESFP],
                         ["ESTJ", wo_ESTJ],
                         ["ESTP", wo_ESTP],
                         ["INFJ", wo_INFJ],
                         ["INFP", wo_INFP] ],
  columns = ['Type', 'NormalizedScore'])

  oc_minimum = rslt_df1['NormalizedScore'].min()
  oc_maximum = rslt_df1['NormalizedScore'].max()

  ptcg_INTJ = (float(wo_INTJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_INTP = (float(wo_INTP - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ISFJ = (float(wo_ISFJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ISFP = (float(wo_ISFP - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ISTJ = (float(wo_ISTJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ISTP = (float(wo_ISTP - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ENFJ = (float(wo_ENFJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ENFP = (float(wo_ENFP - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ENTJ = (float(wo_ENTJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ENTP = (float(wo_ENTP - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ESFJ = (float(wo_ESFJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ESFP = (float(wo_ESFP - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ESTJ = (float(wo_ESTJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_ESTP = (float(wo_ESTP - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_INFJ = (float(wo_INFJ - oc_minimum))/(oc_maximum-oc_minimum)
  ptcg_INFP = (float(wo_INFP - oc_minimum))/(oc_maximum-oc_minimum)

  rslt_df = pd.DataFrame([ ["INTJ", ptcg_INTJ],
                         ["INTP", ptcg_INTP],
                         ["ISFJ", ptcg_ISFJ],
                         ["ISFP", ptcg_ISFP],
                         ["ISTJ", ptcg_ISTJ],
                         ["ISTP", ptcg_ISTP],
                         ["ENFJ", ptcg_ENFJ],
                         ["ENFP", ptcg_ENFP],
                         ["ENTJ", ptcg_ENTJ],
                         ["ENTP", ptcg_ENTP],
                         ["ESFJ", ptcg_ESFJ],
                         ["ESFP", ptcg_ESFP],
                         ["ESTJ", ptcg_ESTJ],
                         ["ESTP", ptcg_ESTP],
                         ["INFJ", ptcg_INFJ],
                         ["INFP", ptcg_INFP] ],
  columns = ['Type', 'NormalizedScore'])

  rslt_df = rslt_df.sort_values(by=['NormalizedScore'], ascending = False)

  rslt_df = rslt_df.reset_index(drop=True)
  rslt_df.index = rslt_df.index + 1
  return rslt_df.head(5)

root = Tk()
root.geometry("760x450")

lbl = Label(root, text = "Enter the word")
lbl.pack()

textBox=Text(root, height=2, width=10)
textBox.pack()

submitButton=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: handleClick())
#command=lambda: retrieve_input() >>> just means do this when i press the button
submitButton.pack()


tree1 = ttk.Treeview(root)
tree1.pack()

def yeet_children():
  for item in tree1.get_children():
    tree1.delete(item)

def handleClick():
  target = textBox.get("1.0","end-1c")

  rslt_df = solution(target)

  print(rslt_df)
  print('____________________________________________________________________')
  print(rslt_df == None)

  yeet_children()
  tree1['columns'] = rslt_df.columns.values.tolist()

  for i in rslt_df.columns.values.tolist():
    tree1.heading(i, text=i)
    tree1.column('#0', width = 80, anchor="w")
    tree1.column('#1', width = 80, anchor="w")
    tree1.column('#2', width = 160, anchor="w")
  for index, row in rslt_df.iterrows():
    tree1.insert("", 'end', text=index, values=list(row))
    
root.mainloop()