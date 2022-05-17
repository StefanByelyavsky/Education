import calc
import calc_provider

calc = calc.Calc()
task = input('введіть приклад:')

calc_provider = calc_provider.CalcProvider(calc)
result = calc_provider.fnExecute(task)

print(result)












for i in task:
    if not i.isdecimal():
        act = i
        parts = task.split(i)
if act == '/' and parts[-1] == '0':
    print("Неможна ділити на нуль")
else:
    match act:
        case '+':
            result = calc.fnSumm(int(parts[0]), int(parts[1]))
        case '-':
            result = calc.fnSubs(int(parts[0]), int(parts[1]))
        case '*':
            result = calc.fnMult(int(parts[0]), int(parts[1]))
        case  '/':
            result = calc.fnDiv(int(parts[0]), int(parts[1]))
        case _:
            print('некоректні дані')
    print(result)
