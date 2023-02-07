import json
from django.shortcuts import render
from django.http import JsonResponse
from diet.geraDieta.opt import gerarDieta


# Create your views here.
def index(request):
    return render(request, "index.html")


def criarDieta(request):
    body = json.loads(request.body.decode("utf-8"))

    obj = gerarDieta(
        float(body["minCaloria"]),
        float(body["maxCaloria"]),
        float(body["minColesterol"]),
        float(body["maxColesterol"]),
        float(body["minGordura"]),
        float(body["maxGordura"]),
        float(body["minSodio"]),
        float(body["maxSodio"]),
        float(body["minCarboidrato"]),
        float(body["maxCarboidrato"]),
        float(body["minFibras"]),
        float(body["maxFibras"]),
        float(body["minProteina"]),
        float(body["maxProteina"]),
        float(body["minVitA"]),
        float(body["maxVitA"]),
        float(body["minVitC"]),
        float(body["maxVitC"]),
        float(body["minCalcio"]),
        float(body["maxCalcio"]),
        float(body["minFerro"]),
        float(body["maxFerro"]),
    )
    response = JsonResponse(obj)
    return response
