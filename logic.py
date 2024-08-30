#Authors    Kevin Jaimes    - 1152245
#           Evelin Bermudez - 1152278

current_operation = None
last_number = None

# click screen buttons
def button_click(text, entry, result):
    global current_operation, last_number
    current_text = entry.get()
    
    if text == "AC":
        clear_all(entry, result)
    elif text == "C":
        entry.delete(len(current_text) - 1)
    elif text == "=":
        calculate_result(current_text, result)
    else:
        insert_text(text, current_text, entry)

def clear_all(entry, result):
    global current_operation, last_number
    entry.delete(0, "end")
    result.config(state="normal")
    result.delete(0, "end")
    result.config(state="readonly")
    current_operation = None
    last_number = None

def calculate_result(expression, result):
    try:
        expression = expression.replace("x", "*").replace("/", "/")
        result_value = eval(expression)
        result.config(state="normal")
        result.delete(0, "end")
        result.insert(0, result_value)
        result.config(state="readonly")
    except Exception:
        result.config(state="normal")
        result.delete(0, "end")
        result.insert(0, "Error")
        result.config(state="readonly")

# insert, not leading zeros
def insert_text(text, current_text, entry):
    if text.isdigit():
        if current_text == "0":
            entry.delete(0, "end")
            entry.insert("end", text)
        else:
            entry.insert("end", text)
    else:
        entry.insert("end", text)

#validate numb or symbols
def validate_numb(char):
    return char.isdigit() or char in "*+-/%"
