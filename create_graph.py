import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()  # GUIを表示しない
file_path = filedialog.askopenfilename()  # ファイルダイアログを開く

output_file_name = os.path.splitext(os.path.basename(file_path))[0]
output_file_path = f'images/{output_file_name}'

# CSVファイルを読み込む
data = pd.read_csv(file_path, encoding='utf-8-sig')

# グラフを描画
plt.figure()

# Accuracyのグラフ
plt.subplot(2, 2, 1)
plt.plot(data['Epoch'], data['Accuracy'], label='Accuracy')
plt.title('Accuracy per Epoch')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

# Lossのグラフ
plt.subplot(2, 2, 2)
plt.plot(data['Epoch'], data['Loss'], label='Loss', color='red')
plt.title('Loss per Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')

# Validation Accuracyのグラフ
plt.subplot(2, 2, 3)
plt.plot(data['Epoch'], data['Val_Accuracy'], label='Val_Accuracy', color='green')
plt.title('Validation Accuracy per Epoch')
plt.xlabel('Epoch')
plt.ylabel('Validation Accuracy')

# Validation Lossのグラフ
plt.subplot(2, 2, 4)
plt.plot(data['Epoch'], data['Val_Loss'], label='Val_Loss', color='purple')
plt.title('Validation Loss per Epoch')
plt.xlabel('Epoch')
plt.ylabel('Validation Loss')

# グラフのレイアウトを整える
plt.tight_layout()

plt.savefig(output_file_path)

# グラフを表示
plt.show()

