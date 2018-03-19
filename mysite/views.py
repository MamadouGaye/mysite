from django.shortcuts import render
def accueil(requete):
	return render(requete,'index.html')