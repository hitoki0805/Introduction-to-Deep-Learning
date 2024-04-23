import re
import csv
import tkinter as tk
from tkinter import filedialog

def parse_log_file(log_file_path):
    # エポック情報とメトリクスを抽出するための正規表現パターン
    epoch_pattern = re.compile(r'Epoch (\d+)/\d+')
    accuracy_pattern = re.compile(r'- accuracy: ([0-9.]+)')
    loss_pattern = re.compile(r'- loss: ([0-9.]+)')
    val_acc_pattern = re.compile(r'- val_accuracy: ([0-9.]+)')
    val_loss_pattern = re.compile(r'- val_loss: ([0-9.]+)')
    
    results = []  # 結果を格納するリスト
    current_epoch = None
    metrics_data = {}
    
    with open(log_file_path, 'r') as file:
        for line in file:
            epoch_match = epoch_pattern.search(line)
            if epoch_match:
                # エポック情報が見つかった場合、前のエポックのデータを保存
                if current_epoch is not None:
                    results.append([
                        current_epoch,
                        metrics_data.get('accuracy', ''),
                        metrics_data.get('loss', ''),
                        metrics_data.get('val_accuracy', ''),
                        metrics_data.get('val_loss', '')
                    ])
                current_epoch = epoch_match.group(1)
                metrics_data = {}  # 新しいエポックのためにメトリクスデータをリセット
            else:
                # 各メトリクスの値を抽出して保存
                for pattern, key in [(accuracy_pattern, 'accuracy'), (loss_pattern, 'loss'), (val_acc_pattern, 'val_accuracy'), (val_loss_pattern, 'val_loss')]:
                    match = pattern.search(line)
                    if match:
                        metrics_data[key] = match.group(1)
        
        # 最後のエポックのデータを保存
        if current_epoch is not None:
            results.append([
                current_epoch,
                metrics_data.get('accuracy', ''),
                metrics_data.get('loss', ''),
                metrics_data.get('val_accuracy', ''),
                metrics_data.get('val_loss', '')
            ])
    
    return results

def save_to_csv(data, output_file_path):
    # CSVファイルに保存
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Epoch', 'Accuracy', 'Loss', 'Val_Accuracy', 'Val_Loss'])  # ヘッダー
        writer.writerows(data)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # GUIを表示しない
    log_file_path = filedialog.askopenfilename()  # ファイルダイアログを開く
    output_file_path = log_file_path.rsplit('.', 1)[0] + '.csv'  # 出力ファイルのパス
    
    # ログファイルを解析
    data = parse_log_file(log_file_path)
    
    # CSVに保存
    save_to_csv(data, output_file_path)
    print('CSVファイルに保存しました。')
