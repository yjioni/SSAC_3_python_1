from tkinter import filedialog, Tk
import pandas as pd


root = Tk()
root.filename = filedialog.askopenfilenames()
print(root.filename)

df_ranks = pd.DataFrame()

for name in root.filename:
    pd_data = pd.read_excel(name)
    df_ranks = df_ranks.append(pd_data)

df_ranks.info()

save_name = filedialog.asksaveasfilename(title='save as',
                                         initialdir='C:/Users/'
                                         )
df_ranks.to_excel(save_name, index=False)