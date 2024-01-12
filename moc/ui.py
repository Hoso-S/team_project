import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def show_detail(name):
    # ここで名前の詳細画面を表示する処理を追加
    window_detail = tk.Toplevel(window_list)
    window_detail.title(f"{name}の詳細画面")

    # ダミーデータ（4月から3月までの教科ごとの点数）
    subjects = ["国語", "数学", "英語", "化学", "物理", "生物"]
    scores = np.random.randint(0, 101, size=(6, 12))

    # グラフ描画
    fig, ax = plt.subplots(figsize=(8, 6))
    for i, subject in enumerate(subjects):
        ax.plot(range(1, 13), scores[i, :], label=subject)

    ax.set_title("月別教科ごとの点数")
    ax.set_xlabel("月")
    ax.set_ylabel("点数")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=window_detail)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=20, pady=20)

    # 表描画
    table_frame = ttk.Frame(window_detail)
    table_frame.pack(padx=20, pady=(0, 20))

    # ヘッダー
    header_labels = ["月"] + subjects
    for j, header_label in enumerate(header_labels):
        ttk.Label(table_frame, text=header_label, font=("Arial", 10, "bold")).grid(row=0, column=j, padx=5, pady=5, sticky="nsew")

    # データ
    for i in range(12):
        ttk.Label(table_frame, text=f"{i+1}月", font=("Arial", 10, "normal")).grid(row=i + 1, column=0, padx=5, pady=5, sticky="nsew")
        for j in range(6):
            ttk.Label(table_frame, text=str(scores[j, i]), font=("Arial", 10, "normal")).grid(row=i + 1, column=j + 1, padx=5, pady=5, sticky="nsew")

    # 閉じるボタン
    close_button = ttk.Button(window_detail, text="閉じる", command=window_detail.destroy)
    close_button.pack(pady=10)

def on_double_click(event):
    item = tree.selection()[0]
    name = tree.item(item, "values")[0]
    show_detail(name)

def list_data():
    # 仮のデータ
    data = [
        ("Alice", "20", "大学生", "英語"),
        ("Bob", "25", "社会人", "数学"),
        ("Charlie", "18", "高校生", "化学"),
        # 他のデータを追加
    ]
    return data

def update_list():
    for row in tree.get_children():
        tree.delete(row)

    for item in list_data():
        tree.insert("", "end", values=item)

def list():
    # リスト表示画面を作成
    global window_list
    window_list = tk.Toplevel(window_search)
    window_list.title("リスト表示画面")
    window_list.geometry("700x450")

    global tree
    tree = ttk.Treeview(window_list, columns=("Name", "Age", "Grade", "Subject"), show="headings")

    tree.heading("Name", text="名前")
    tree.heading("Age", text="年齢")
    tree.heading("Grade", text="学年")
    tree.heading("Subject", text="教科")

    tree.pack(fill="both", expand=True)
    update_list()

    tree.bind("<Double-1>", on_double_click)

def search():
    
    # 検索画面の作成
    global window_search
    window_search = tk.Tk()
    window_search.title("検索画面")
    window_search.configure(bg="white")  # 背景色を白に設定
    window_search.geometry("700x450")

    # フリーワード入力ボックス
    label_free_word = tk.Label(window_search, text="フリーワード:")
    label_free_word.pack(pady=(20, 0))

    entry_free_word = tk.Entry(window_search)
    entry_free_word.pack(pady=10)

    # 年齢のフィルタ
    label_age = tk.Label(window_search, text="年齢:")
    label_age.pack()

    ages = ["全て"] + [str(i) for i in range(15, 23)]  # 15から22までの選択肢
    age_var = tk.StringVar(value=ages[0])

    age_menu = ttk.Combobox(window_search, textvariable=age_var, values=ages)
    age_menu.pack(pady=10)

    # 学年のフィルタ
    label_grade = tk.Label(window_search, text="学年:")
    label_grade.pack()

    grades = ["全て"] + [str(i) for i in range(1, 7)]  # 1から6までの選択肢
    grade_var = tk.StringVar(value=grades[0])

    grade_menu = ttk.Combobox(window_search, textvariable=grade_var, values=grades)
    grade_menu.pack(pady=10)

    # 教科のフィルタ
    label_subject = tk.Label(window_search, text="教科:")
    label_subject.pack()

    subjects = ["全て", "国語", "数学", "英語", "化学", "物理", "生物"]
    subject_var = tk.StringVar(value=subjects[0])

    subject_menu = ttk.Combobox(window_search, textvariable=subject_var, values=subjects)
    subject_menu.pack(pady=10)

    # 検索ボタン
    search_button = tk.Button(window_search, text="検索", command=list)
    search_button.pack()

    # ウィンドウを表示
#    window_search.mainloop()


def login():
    # ここで実際のログイン処理を行うと仮定
    # 今は単純にログイン成功として扱う
    username = entry_username.get()
    password = entry_password.get()

    if username == "user" and password == "pass":
        # ログイン成功時の処理
        # ログインウィンドウを破棄し、検索画面を表示
        window_login.destroy()

        # 新しいウィンドウ（検索画面）の作成
#        window_search = tk.Tk()
#        window_search.title("検索画面")
#        window_search.configure(bg="white")  # 背景色を白に設定

#        label_search = tk.Label(window_search, text="検索画面が表示されました。")
#        label_search.pack(padx=20, pady=20)

        search()
#        login_button = tk.Button(window_search, text="検索", command=search)
#        login_button.pack()

    else:
        # ログイン失敗時の処理（例: エラーメッセージを表示）
        label_error.config(text="ログインに失敗しました。")

def main():
    # ログインウィンドウの作成
    global window_login
    window_login = tk.Tk()
    window_login.title("Login Window")
    window_login.configure(bg="white")  # 背景色を白に設定
    window_login.geometry("700x450")

    # ユーザー名のラベルとエントリーボックス
    label_username = tk.Label(window_login, text="ユーザー名:")
    label_username.pack(pady=(20, 0))

    global entry_username
    entry_username = tk.Entry(window_login)
    entry_username.pack(pady=10)

    # パスワードのラベルとエントリーボックス
    label_password = tk.Label(window_login, text="パスワード:")
    label_password.pack()

    global entry_password
    entry_password = tk.Entry(window_login, show="*")  # パスワードは*で表示
    entry_password.pack(pady=10)

    # ログインエラーメッセージ
    global label_error
    label_error = tk.Label(window_login, text="", fg="red", bg="white")
    label_error.pack()

    # ログインボタン
    login_button = tk.Button(window_login, text="ログイン", command=login)
    login_button.pack()

    # ウィンドウを表示
    window_login.mainloop()

if __name__ == "__main__":
    main()
