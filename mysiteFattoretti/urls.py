"""mysiteFattoretti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

'''
Alla funzione path() vengono passati quattro argomenti, due richiesti: routee,viewe e due facoltativi: kwargse,name.


Route:
route è una stringa che contiene un pattern URL.
 Quando elabora una richiesta, Django inizia dal primo modello in entrata urlpatternse 
 si sposta in fondo all'elenco, confrontando l'URL richiesto con ogni modello fino a quando 
 non trova quello corrispondente.

 View:
 Quando Django trova un modello corrispondente, chiama la funzione 
 di vista specificata con un HttpRequestoggetto come primo argomento e tutti i valori 
 "catturati" dalla rotta come argomenti di parole chiave. 

Kwargs:
Gli argomenti di parole chiave arbitrarie possono essere passati in un dizionario alla vista di destinazione.

Name:
Assegnare un nome al tuo URL ti consente di farvi riferimento in modo inequivocabile 
da qualsiasi altra parte di Django, in particolare dai modelli. 
Questa potente funzionalità ti consente di apportare modifiche globali ai pattern URL 
del tuo progetto mentre tocchi solo un singolo file.'''


'''Con il comando makemigrations stiamo dicenso a django che abbiamo apportato modifiche al models e che le vogliamo 
salvare come migrate.
Il comando sqlmigrate  accetta i nomi di migrazione e restituisce il loro SQL'''

'''abbiamo rimosso gli hardcoded url perchè se si cambiasse il nome dell'url si dovrebbe modificare in tutta l'app 
invece mettendo in nome dell'argomento nella funzione path() si possono rimuovere i colegamenti diretti agli url.

con i namaspacing urls name django sa quale view dell'app creare per un url quando si usa il tag templates
'''

'''request.POSTè un oggetto simile a un dizionario che consente di accedere ai 
dati inviati in base al nome della chiave. In questo caso, request.
POST['choice']restituisce l'ID della scelta selezionata, come una stringa.

la funzione reverse() evita di dover codificare un URL nella funzione di visualizzazione. 
Ci viene dato il nome della vista a cui vogliamo 
passare il controllo e la parte variabile del pattern URL che punta a quella vista.'''

