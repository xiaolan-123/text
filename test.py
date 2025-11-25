# This is a test file
import tkinter as tk
from tkinter import ttk, messagebox


def sort_numbers():
    """
    从输入框获取数字，根据选择的排序方式进行排序，并显示结果
    """
    # 获取输入的数字字符串
    input_str = entry.get()

    # 验证输入是否为空
    if not input_str.strip():
        messagebox.showerror("错误", "请输入数字！")
        return

    # 分割数字字符串并转换为列表
    try:
        # 使用逗号或空格分割数字
        numbers = list(map(float, input_str.replace(',', ' ').split()))
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字，使用逗号或空格分隔！")
        return

    # 获取选择的排序方式
    sort_order = sort_var.get()

    # 进行排序
    if sort_order == "升序":
        sorted_numbers = sorted(numbers)
    else:
        sorted_numbers = sorted(numbers, reverse=True)

    # 显示结果
    result_text.config(state='normal')
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"原始数字: {numbers}\n")
    result_text.insert(tk.END, f"{sort_order}排序后: {sorted_numbers}\n\n")
    result_text.insert(tk.END, f"排序后的数字（空格分隔）: {' '.join(map(str, sorted_numbers))}")
    result_text.config(state='disabled')


def clear_input():
    """清空输入框和结果框"""
    entry.delete(0, tk.END)
    result_text.config(state='normal')
    result_text.delete('1.0', tk.END)
    result_text.config(state='disabled')


def paste_from_clipboard():
    """从剪贴板粘贴内容到输入框"""
    try:
        clipboard_content = root.clipboard_get()
        entry.insert(tk.END, clipboard_content)
    except tk.TclError:
        messagebox.showwarning("警告", "剪贴板为空或无法访问")


# 创建主窗口
root = tk.Tk()
root.title("数字排序工具")
root.geometry("500x400")
root.resizable(True, True)

# 设置样式
style = ttk.Style(root)
style.theme_use('clam')  # 可选: 'alt', 'default', 'clam', 'classic'

# 创建主框架
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# 创建输入框架
input_frame = ttk.LabelFrame(main_frame, text="输入数字", padding="10")
input_frame.pack(fill=tk.X, pady=5)

entry = ttk.Entry(input_frame, width=50)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
entry.focus()

# 创建按钮框架
button_frame = ttk.Frame(input_frame)
button_frame.pack(side=tk.RIGHT)

paste_button = ttk.Button(button_frame, text="粘贴", command=paste_from_clipboard)
paste_button.pack(pady=2)

clear_button = ttk.Button(button_frame, text="清空", command=clear_input)
clear_button.pack(pady=2)

# 创建排序选项框架
sort_frame = ttk.LabelFrame(main_frame, text="排序选项", padding="10")
sort_frame.pack(fill=tk.X, pady=5)

sort_var = tk.StringVar(value="升序")

asc_radio = ttk.Radiobutton(sort_frame, text="升序", variable=sort_var, value="升序")
asc_radio.pack(side=tk.LEFT, padx=10)

desc_radio = ttk.Radiobutton(sort_frame, text="降序", variable=sort_var, value="降序")
desc_radio.pack(side=tk.LEFT, padx=10)

sort_button = ttk.Button(sort_frame, text="开始排序", command=sort_numbers)
sort_button.pack(side=tk.RIGHT)

# 创建结果显示框架
result_frame = ttk.LabelFrame(main_frame, text="排序结果", padding="10")
result_frame.pack(fill=tk.BOTH, expand=True, pady=5)

result_text = tk.Text(result_frame, height=10, width=50, state='disabled',
                      wrap=tk.WORD, font=("Consolas", 10))
result_text.pack(fill=tk.BOTH, expand=True)

# 添加滚动条
scrollbar = ttk.Scrollbar(result_frame, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

# 添加快捷键
root.bind('<Return>', lambda event: sort_numbers())
root.bind('<Control-c>', lambda event: entry.event_generate('<<Copy>>'))
root.bind('<Control-v>', lambda event: paste_from_clipboard())
root.bind('<Control-x>', lambda event: entry.event_generate('<<Cut>>'))
root.bind('<Control-a>', lambda event: entry.select_range(0, tk.END))

# 添加状态栏
status_frame = ttk.Frame(main_frame)
status_frame.pack(fill=tk.X, pady=5)

status_label = ttk.Label(status_frame, text="提示: 输入数字时使用逗号或空格分隔", anchor=tk.W)
status_label.pack(fill=tk.X)

# 启动主循环
root.mainloop()