mongodb-pythonpuro-casadocodigo
=================================

  MongoDB + Python puro
-------------------------

* Database.....: *test*
* Collection...: *seriados*

* Carga 

```
 mongo < db/seriados.js

```


* Exemplo de documento

```
db.seriados.findOne()
 
{
    "_id" : "1",
    "nome" : "Breaking Bad",
    "personagens" : [ 
        "Walter White", 
        "Skyler White", 
        "Jesse Pinkman", 
        "Hank Schrader", 
        "Marie Schrader ", 
        "Saul Goodman"
    ]
}
```

# Rodando


```
 python seriados.py

```
