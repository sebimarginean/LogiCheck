import re
import itertools
import tkinter as tk

def equivalence(expression):
    
    atoms = set(re.findall(r'[A-Za-z]', expression))
    
    atoms_values = {}
    for var in atoms:
        atoms_values[var] = [0, 1]
    
    truth_table = list(itertools.product([0, 1], repeat = len(atoms)))
    #Replace the logical operators with python operators
    expression = expression.replace('<=>', '==')
    expression = expression.replace('=>', '<=')
    expression = expression.replace('&&', 'and').replace('||', 'or').replace('!', 'not ')
    
    #Evaluate the expression for each line in the truth table
    for line in truth_table:
        final_expression = expression
        for idx, atom in enumerate(atoms):
            final_expression = final_expression.replace(atom, str(line[idx]))
        
        if eval(final_expression) == False:
            return False
    return True

def verify_equivalence():
    input1 = input_field1.get()
    input2 = input_field2.get()
    output.configure(text="Expressions are logically equivalent" if equivalence("(" +input1 + ")<=>(" + input2 + ")") else "Expressions are not logically equivalent")

def verify_tautology():
    input3 = input_field3.get()
    result = equivalence("(" + input3 + ")<=>(1)")
    output.configure(text="Expression is tautology" if result == True else "Expression is not tautology")
    
def verify_contradiction():
    input4 = input_field4.get()
    result = equivalence("(" + input4 + ")<=>(0)")
    output.configure(text="Expression is contradiction" if result == True else "Expression is not contradiction")

root = tk.Tk()
root.geometry("800x500")
root.title("Logical equivalents")

input_field1 = tk.Entry(root, width=100)
input_field1.pack()

input_field2 = tk.Entry(root, width=100)
input_field2.pack()

button = tk.Button(root, text="Verify", command=verify_equivalence)
button.pack()


input_field3 = tk.Entry(root, width=100)
input_field3.pack()
button = tk.Button(root, text="Verify tautology", command=verify_tautology)
button.pack()


input_field4 = tk.Entry(root, width=100)
input_field4.pack()
button = tk.Button(root, text="Verify contradiction", command=verify_contradiction)
button.pack()

output = tk.Label(root, text="")
output.pack()

root.mainloop()