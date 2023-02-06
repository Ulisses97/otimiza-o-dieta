import pandas as pd
from pulp import *

df = pd.read_excel("diet-diet.xls", nrows=17)
# df = pd.read_excel("diet - big.xls",nrows=18)
# df = pd.read_excel("diet.xls",nrows=64)

# df

# Crie a variável 'prob' para conter os dados do problema
prob = LpProblem("Problema de dieta simples", LpMinimize)


# Cria uma lista dos Ingredientes
food_items = list(df["Foods"])

print("Itens alimentares a se considerar, são\n" + "-" * 100)
for f in food_items:
    print(f, end=", ")
print("\n\n")
# Criando dicionário das propriedades a se considerar
costs = dict(zip(food_items, df["Price/Serving"]))
calories = dict(zip(food_items, df["Calories"]))
cholesterol = dict(zip(food_items, df["Cholesterol (mg)"]))
fat = dict(zip(food_items, df["Total_Fat (g)"]))
sodium = dict(zip(food_items, df["Sodium (mg)"]))
carbs = dict(zip(food_items, df["Carbohydrates (g)"]))
fiber = dict(zip(food_items, df["Dietary_Fiber (g)"]))
protein = dict(zip(food_items, df["Protein (g)"]))
vit_A = dict(zip(food_items, df["Vit_A (IU)"]))
vit_C = dict(zip(food_items, df["Vit_C (IU)"]))
calcium = dict(zip(food_items, df["Calcium (mg)"]))
iron = dict(zip(food_items, df["Iron (mg)"]))

# Um dicionário chamado 'food_vars' é criado para conter as variáveis referenciadas
food_vars = LpVariable.dicts("Food", food_items, 0, cat="Contínuo")
# food_vars

# A função objetivo é adicionada a 'prob' primeiro
prob += lpSum([costs[i] * food_vars[i] for i in food_items]), "Custo Total da dieta balanceada"

# Restrições

# Calorias
prob += lpSum([calories[f] * food_vars[f] for f in food_items]) >= 800.0, "CaloriasMinimas"
prob += lpSum([calories[f] * food_vars[f] for f in food_items]) <= 1300.0, "CaloriasMaximas"

# Colesterol
prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) >= 30.0, "ColesterolMínimo"
prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) <= 240.0, "ColesterolMáximo"

# Gordura
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= 40.0, "GorduraMínima"
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) <= 100.0, "GorduraMáxima"

# Sódio
prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) >= 500.0, "SódioMínimo"
prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) <= 2000.0, "SódioMáximo"

# Carboidrato
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= 130.0, "CarboidratoMínimo"
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) <= 450.0, "CarboiddratoMáximo"

# Fibra
prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) >= 125.0, "FibraMínima"
prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) <= 250.0, "FibraMáxima"

# Proteina
prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= 60.0, "ProteinaMínima"
prob += lpSum([protein[f] * food_vars[f] for f in food_items]) <= 100.0, "ProteinaMáxima"

# Vitamina A
prob += lpSum([vit_A[f] * food_vars[f] for f in food_items]) >= 1000.0, "VitaminaAMínima"
prob += lpSum([vit_A[f] * food_vars[f] for f in food_items]) <= 10000.0, "VitaminaAMáximo"

# Vitamina C
prob += lpSum([vit_C[f] * food_vars[f] for f in food_items]) >= 400.0, "VitaminaCMínima"
prob += lpSum([vit_C[f] * food_vars[f] for f in food_items]) <= 5000.0, "VitaminaCMáximo"

# Cálcio
prob += lpSum([calcium[f] * food_vars[f] for f in food_items]) >= 300.0, "CálcioMínimo"
prob += lpSum([calcium[f] * food_vars[f] for f in food_items]) <= 1500.0, "CálcioMáximo"

# Ferro
prob += lpSum([iron[f] * food_vars[f] for f in food_items]) >= 10.0, "FerroMínimo"
prob += lpSum([iron[f] * food_vars[f] for f in food_items]) <= 40.0, "FerroMáximo"

# Os dados do problema são gravados em um arquivo .lp
# prob.writeLP("ProblemaDeDieta.lp")

# O problema é resolvido usando a escolha do Solver do PuLP
prob.solve()

# O status da solução é impresso na tela
print("Status:", LpStatus[prob.status])

print("Portanto, a dieta balanceada ideal (de menor custo) consiste em\n" + "-" * 110)
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)

print("O custo total dessa dieta balanceada é: R${}".format(round(value(prob.objective), 2)))
