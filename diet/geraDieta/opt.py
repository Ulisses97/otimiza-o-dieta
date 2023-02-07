import pandas as pd
from pulp import *


def gerarDieta(
    calMin=800.0,
    calMax=1300.0,
    colMin=30.0,
    colMax=240.0,
    gordMin=40.0,
    gordMax=100.0,
    sodMin=500.0,
    sodMax=2000.0,
    carbMin=130.0,
    carbMax=450.0,
    fibraMin=125.0,
    fibraMax=205.0,
    protMin=60.0,
    protMax=100.0,
    vitAMin=1000.0,
    vitAMax=10000.0,
    vitCMin=400.0,
    vitCMax=5000.0,
    calcMin=300.0,
    calcMax=1500.0,
    ferroMin=10.0,
    ferroMax=40.0,
):
    df = pd.read_excel(os.path.join(os.path.dirname(__file__), "diet.xls"), nrows=64)
    # df = pd.read_excel("diet - big.xls",nrows=18)
    # df = pd.read_excel("diet.xls",nrows=64)

    # df

    # Crie a variável 'prob' para conter os dados do problema
    prob = LpProblem("Problema de dieta simples", LpMinimize)

    # Cria uma lista dos Ingredientes
    food_items = list(df["Foods"])

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
    prob += lpSum([calories[f] * food_vars[f] for f in food_items]) >= calMin, "CaloriasMinimas"
    prob += lpSum([calories[f] * food_vars[f] for f in food_items]) <= calMax, "CaloriasMaximas"

    # Colesterol
    prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) >= colMin, "ColesterolMínimo"
    prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) <= colMax, "ColesterolMáximo"

    # Gordura
    prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= gordMin, "GorduraMínima"
    prob += lpSum([fat[f] * food_vars[f] for f in food_items]) <= gordMax, "GorduraMáxima"

    # Sódio
    prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) >= sodMin, "SódioMínimo"
    prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) <= sodMax, "SódioMáximo"

    # Carboidrato
    prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= carbMin, "CarboidratoMínimo"
    prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) <= carbMax, "CarboiddratoMáximo"

    # Fibra
    prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) >= fibraMin, "FibraMínima"
    prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) <= fibraMax, "FibraMáxima"

    # Proteina
    prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= protMin, "ProteinaMínima"
    prob += lpSum([protein[f] * food_vars[f] for f in food_items]) <= protMax, "ProteinaMáxima"

    # Vitamina A
    prob += lpSum([vit_A[f] * food_vars[f] for f in food_items]) >= vitAMin, "VitaminaAMínima"
    prob += lpSum([vit_A[f] * food_vars[f] for f in food_items]) <= vitAMax, "VitaminaAMáximo"

    # Vitamina C
    prob += lpSum([vit_C[f] * food_vars[f] for f in food_items]) >= vitCMin, "VitaminaCMínima"
    prob += lpSum([vit_C[f] * food_vars[f] for f in food_items]) <= vitCMax, "VitaminaCMáximo"

    # Cálcio
    prob += lpSum([calcium[f] * food_vars[f] for f in food_items]) >= calcMin, "CálcioMínimo"
    prob += lpSum([calcium[f] * food_vars[f] for f in food_items]) <= calcMax, "CálcioMáximo"

    # Ferro
    prob += lpSum([iron[f] * food_vars[f] for f in food_items]) >= ferroMin, "FerroMínimo"
    prob += lpSum([iron[f] * food_vars[f] for f in food_items]) <= ferroMax, "FerroMáximo"

    # Os dados do problema são gravados em um arquivo .lp
    # prob.writeLP("ProblemaDeDieta.lp")

    # O problema é resolvido usando a escolha do Solver do PuLP
    prob.solve()

    resultado = {"custo": "R${}".format(round(value(prob.objective), 2))}

    # O status da solução é impresso na tela

    for v in prob.variables():
        if v.varValue > 0:
            resultado[v.name] = v.varValue

    return resultado
