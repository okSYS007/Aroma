import tkinter as tk

def calculate_profit():
    cost_price = float(cost_price_entry.get())
    additional_costs = float(additional_costs_entry.get())
    total_cost_price = cost_price + additional_costs
    markup = float(markup_entry.get())
    
    result = "Цена и прибыль для каждого типа флакона:\n"
    
    for bottle_type, (bottle_count, bottle_capacity) in bottle_info.items():
        total_bottle_capacity = bottle_count * bottle_capacity
        total_cost_per_bottle = total_cost_price * bottle_capacity / total_bottle_capacity
        selling_price_per_bottle = total_cost_per_bottle * (1 + markup / 100)
        total_selling_price = selling_price_per_bottle * bottle_count
        total_profit = total_selling_price - total_cost_price
        
        result += f"{bottle_type} ({bottle_capacity} мл) - Цена за 1 флакон: {selling_price_per_bottle:.2f} USD, Прибыль: {total_profit:.2f} USD\n"

    result_label.config(text=result)

bottle_info = {
    "10 флаконов по 10 мл": (10, 10),
    "20 флаконов по 5 мл": (20, 5),
    "33 флакона по 3 мл": (33, 3)
}

def add_bottle_info():
    bottle_type = bottle_type_entry.get()
    bottle_count = int(bottle_count_entry.get())
    bottle_capacity = int(bottle_capacity_entry.get())
    bottle_info[bottle_type] = (bottle_count, bottle_capacity)

    result_label.config(text="Информация о флаконах добавлена.")

# Создаем графический интерфейс
app = tk.Tk()
app.title("Подсчет прибыли товара")

# Ввод себестоимости и дополнительных расходов
cost_price_label = tk.Label(app, text="Себестоимость товара ($):")
cost_price_label.pack()

cost_price_entry = tk.Entry(app)
cost_price_entry.pack()

additional_costs_label = tk.Label(app, text="Дополнительные расходы ($):")
additional_costs_label.pack()

additional_costs_entry = tk.Entry(app)
additional_costs_entry.insert(0, "0")
additional_costs_entry.pack()

markup_label = tk.Label(app, text="Наценка по умолчанию (%):")
markup_label.pack()

markup_entry = tk.Entry(app)
markup_entry.insert(0, "0")  # Устанавливаем наценку по умолчанию в 30%
markup_entry.pack()

calculate_button = tk.Button(app, text="Подсчитать прибыль", command=calculate_profit)
calculate_button.pack()

# Ввод информации о флаконах
bottle_info_label = tk.Label(app, text="Информация о флаконах:")
bottle_info_label.pack()

bottle_type_label = tk.Label(app, text="Тип флакона:")
bottle_type_label.pack()

bottle_type_entry = tk.Entry(app)
bottle_type_entry.pack()

bottle_count_label = tk.Label(app, text="Количество флаконов:")
bottle_count_label.pack()

bottle_count_entry = tk.Entry(app)
bottle_count_entry.pack()

bottle_capacity_label = tk.Label(app, text="Литраж флаконов (мл):")
bottle_capacity_label.pack()

bottle_capacity_entry = tk.Entry(app)
bottle_capacity_entry.pack()

add_bottle_button = tk.Button(app, text="Добавить информацию о флаконах", command=add_bottle_info)
add_bottle_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
