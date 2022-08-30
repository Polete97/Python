# VARIABLES DINS EL TEXT
 #### Pots fer càlculs dins les claus, però millor fer-los abans,de manera que es pugui llegir bé el conjunt de la frase.
 
```python
print(f"M'he menjat {quants} cocodrils.")
print(f"En {qui} s'ha menjat {quants} cocodrils.")
 ```

# NO HAVER D’ESCAPAR LA BARRA \

```python
print("si no vols haver d'escapar \\ les barres")
print(r"pots fer servir \ raw strings")
print(rf"...i funcionen també \ formatant {coses}")
```

# AJUNTAR TEXT SENSE +
```python
print("Hola bon dia," " com esteu tots?" ' Jo molt bé.')
```

# COMBINAR TEXTOS
```python
llista = ["joaquim", "rinoceronts", "ermesenda"]
print("".join(llista)) # >>> "joaquimrinocerontsermesenda"
print(", ".join(llista)) # >>> "joaquim, rinoceronts, ermesenda"
```
# TOTES LES COSES SÓN CERTES O FALSES
 ```python
 num = 0
 if num != 0:
    print("no cal comparar: tot el que no és zero (o buit) és cert")
 if num:
    print("Tinc un número que no és zero.")
 if not num:
    print("No hi ha número (tinc un zero).")
 llista = []
 if not llista:
    print("La llista és buida.")
 text = ""
 if not text:
    print("No hi ha text entre les cometes.")
 ```
# AND I OR RETORNEN LA COSA
 #### and / or retornen el primer element que decideix el resultat
 print(f"{qui or 'Ningú'} vindrà a dinar")
 #### 0 or 2 -> 2  | 0 and 2 -> 0
 ####  1 or 2 -> 1 | 2 and 0 -> 0
 #### 2 and 1 -> 1 | 1 and 2 -> 2
...I NO MIRA EL SEGON SI EL PRIMER FALLA
# només executarà la segona part si la primera és bona
if llista and llista[0] == 5: # (mai farà index error)
 print("oita quin 5 més bonic")
PUC FER IF / ELSE EN UNA LÍNIA
 print(f"Dinarem {quants}" if quants else "No dinarem.")
 # també serveix per executar coses segons condicions
 fes_el_dinar(quants) if quants else None
 # Compte amb les assignacions (X if Y else Z va junt SEMPRE)
 a = 5 if quants else None # vol dir “a = (X if Y else Z)”
 # NO pas: “assigna tal” if Y, else “deixa-ho com estava”

MAJÚSCULES I COSES VÀRIES
 print(text.upper()) # BON DIA A TOTS
 print(text.lower()) # bon dia a tots
 print(text.title()) # Bon Dia A Tots
COMPARACIÓ TERNÀRIA
 if 0 < x < 5:
 print("el num està entre 0 i 5")
EL BUCLE FÀCIL
 for element in llista:
 print(element)
...SI ET CAL L’ÍNDEX
 for i, element in enumerate(llista):
 print(i, element)
DETECTAR BREAK
def primer_num_superior_a_tal(llista, tal):
 for num in llista:
 if num > tal:
 print(num)
 break
 else: # i.e. "el for no ha fet cap break"
 print("No n'he trobat cap.")
FER EL BUCLE AL REVÉS
def bucle_invertit(llista):
 for element in reversed(llista):
 print(element)
FER EL BUCLE ORDENAT
def bucle_ordenat(llista):
 for num in sorted(llista):
 print(num)
...O UN RETURN SI NO HA RETURNAT
def primer_num_superior_a_qual(llista, qual):
 for num in llista:
 if num > qual:
 return num
 return "No n'he trobat cap." # si el troba no arriba aquí :)
DEIXAR COSES PENDENTS DE PROGRAMAR
 def func_que_em_fa_mandra_escriure():
 ... # així guardo el “pass” per quan no ha de fer res
ELEMENT DINS LLISTA
 if 2 in llista:
 print("tinc com a mínim un 2")
 if "a" in text:
 print("aaaaaaaaaaaaaa")
 # [CÀLCUL for ELEMENT in LLISTA] -> llista de calculats
 llista = [x ** 2 for x in range(5)] # [0, 1, 4, 9, 16]
 llista = [3 * x + i for i, x in enumerate(llista)] # més variables
 matriu = [[1, 3], [4, 5], [3, 4]] # des d’una matriu
 multis = [x*y for x, y in matriu] # [3, 20, 12]

 # [CÀLCUL for ELEMENT in LLISTA if CONDICIÓ]
 llista = [5 * x for x in llista if x % 2] # filtro només imparells
 llista = [x for x in llista if x] # filtro no nuls
GENERAR I FILTRAR LLISTES (LIST COMPREHENSIONS)
 permesos = [1, 3, 8]
 llista = [n for n in demanats if n in permesos] or [1, 3, 8]
 # short-circuit: si queda buit serà fals, i em quedaré [1, 3, 8]
TRIAR VALOR PER SI LA LLISTA QUEDÉS BUIDA
COSES GUAIS DEL MÒDUL RANDOM
 import random
 x = random.randint(3, 8) # enter entre 3 i 8 (inclosos)
 y = random.choice(llista) # tria un element de la llista a l'atzar

 # random.choices(llista, proporcions)
 z = random.choices([0, 2], [1, 5]) # El 2 sortirà 5x més sovint que el 0
 a, b = random.choices([0, 2], [1, 5], k=2) # treu-me’n dos de cop
 random.shuffle(llista) # barreja la llista a l’atzar
 random.sample(llista, 2) # agafa de la llista dos elements a l'atzar
...I UN PARELL DE TRUCS
 if not random.randint(0, 5): # una de cada 6 vegades (quan triï el 0)
 print("quina sort, nen")

 def moneda(): # així faig “if moneda:” quan vull fer cara o creu
 return bool(random.getrandbits(1))
DESACTIVAR CODI CONVERTINT-LO EN TEXT
 for x in llista:
 print("estic fent coses que es faran")

 """
 for x in llista:
 print("aquesta part està desactivada")
 """
 def fes_una_suma_molt_xula(a, b):
 return a+b

 s = fes_una_suma_molt_xula # sense parèntesis vol dir la funció en sí
 s(1, 3)
NOM ALTERNATIU PER LA FUNCIÓ
EXPLICAR QUÈ FA LA FUNCIÓ
 def funcio(num, llista):
 """Fa coses amb la llista i els nums i tal (aquestes explicacions
 els IDE les veuen i les fan servir per explicar-te què fan les
 funcions sense que hagis d’anar a veure el codi tu mateix)

 :param num: explicació del num
 :param llista: explicació de la llista
 :return: explicació del resultat
 """
 return coses_que_ha_calculat
VALOR PER SI NO TROBO LA CLAU D’UN DICCIONARI
LLISTES QUE NO OCUPEN MEMÒRIA (GENERADORS)
 key = "pernils"
 dict = {"hola": "Com estàs", "barcelona": "no m'enamora"}
 valor = dict.get(key, "No hi era") # si no troba, retorna “No hi era”
 # crea la llista abans de començar (ocupant molta memòria)
 for x in [num for num in range(100000)]:
 print(x)
 # calcula cada num just quan li cal (i l’oblida just després)
 for x in (num for num in range(100000)):
 print(x)
VARIABLE QUE NO FARÉ SERVIR
IF TOTS SÓN CERT / IF ALGUN ÉS CERT
FUNCIÓ QUE INVENTA LLISTES QUE NO OCUPEN (YIELD)
 for _ in range(5): # s’hi val, i així marco que no afecta en res
 print("Hola")
 # la funció no fa el que té escrit a dins, sinó que li encarrega
 # de fer-ho a algú altre (perquè té yield en lloc de return).
 # i.e. quan la crido, el que fa és retornar una còpia de la recepta.
 def diu_si_3_cops_i_despres_forever_no():
 for _ in range(3):
 yield "Sí!" # yield és com return però només pausa (no tanca)
 while True:
 yield "No!"
 # li entrego una còpia de la recepta a la variable "respostes"
 respostes = diu_si_3_cops_i_despres_forever_no()
 # ...ara "respostes" sap què ha de fer (però de moment no ho fa)
 # Cada cop que demani "next", "respostes" seguirà la recepta fins que
 # arribi a un yield. Llavors em retornarà el que trobi al yield,
 # i s'esperarà allà fins que jo n’hi demani un altre.
 for _ in range(25):
 print(next(respostes))

 # Com que la recepta és infinita (while True), jo podria anar-li
 # dient "next()" per sempre (i ella m’aniria dient “No!”).
 # Per contra, si la fes finita, podria fer "for _ in respostes".
 # Ah, i podria entregar més d'una còpia de la recepta
 # (a diferents variables), i cadascuna recorreria les instruccions
 # al seu ritme, a mesura que li demanessin “next” a ella.
 noms = ["Joaquima", "Ermessenda", "Zalutacions"]
 if all("a" in nom.lower() for nom in noms):
 print("Tots els noms tenen la lletra 'a'.")
 # all(True, True, True) -> True
 if any("z" in nom.lower() for nom in noms):
 print("Hi ha algun nom amb la lletra 'z'.")
 # any(False, False, True) -> True
SUBSTITUIR PARTS DEL TEXT
 text = "Vaig a contractar el Joaquim"
 text = text.replace("Joaquim", "Pernil") # Vaig a contractar el Pernil
 text = text.replace("a", "i") # Viig i contrictir el Pernil
ESTALVIAR AUXILIARS (TUPLE PACKING / UNPACKING)
 x, y = 3, 2 # assignar vàries coses alhora (x=3, y=2)
 x, y = y, x # intercanviar sense auxiliar (x=2, y=3)
 x, y = y, x + y # actualitzar sense auxiliar (x=3, y=5)
ASSIGNACIÓ MÚLTIPLE
 a = b = c = 1 # a=1, b=1, c=1
 x, y, z = (random.randint(0, 10) for _ in range(3))
 # faig un aleatori entre 0 i 10, tres vegades
...GENERAR UNS QUANTS ALEATORIS DE COP
 llista = ["Pernil", "Joaquim", "Ermessenda"]
 print(llista[-1]) # Ermessenda
AGAFAR COSES PEL FINAL
TROBAR POSICIÓ D’UNA COSA
 llista = [5, 2, 3, 1, 5, 8]
 posicio_del_tres = llista.index(3) # 2
 posicio_de_la_i = "Ornitorrinc".index("i") # 3 (et diu la primera)
AGAFAR I ESBORRAR L’ÚLTIM
ORDENAR LLISTES (AL LLOC)
 llista.sort()
 llista.sort(reverse=True) # si la vull invertida
 llista.sort(key=len) # puc demanar-li criteris alternatius per ordenar
 llista.sort(reverse=True, key=len) # de més llarg a més curt
 llista = [2, 8, 4, 3]
 print(llista.pop()) # 3 (...i ara la llista és [2, 8, 4])
RETORNAR DIVERSOS VALORS ALHORA
 return edat, color_preferit # ...i els reculls amb tuple unpacking
FORMATS ESPECIALS
 print(f"{numero:.2f}") # escriu-me només 2 decimals
 print(f"{0.025:.2%}") # fes-me el percentatge: >>> '2.50%'
 print(f"{nom:>10}") # omple amb espais fins que ocupi 10: >>> ' david'
 print(f"{nom:*<8}") # asteriscs fins a 8 (text a l’esquerra): >>> 'david***'
 print(f"{nom:=^9}") # iguals fins a 9 (text al centre): >>> '==david=='
FORMATAR DATES
 import datetime
 data = datetime.datetime.now()
 print(f"{data:%Y-%m-%d %H:%M}") # >>> 2022-08-28 15:32
 # Podeu veure més %codis (nom del dia/mes, AM/PM, etc) aquí
BUCLES AMB DICCIONARIS
 diccionari = {clau1: "valor1", clau2: "valor2"}
 for clau in diccionari: # per defecte ell agafa les claus
 print(clau)
 for valor in diccionari.values(): # puc agafar els valors
 print(valor)
 for clau, valor in diccionari.items(): # o agafar-ho tot per parelles
 print(f"El valor de {clau} és {valor}.")
VARIABLES DINS EL FORMAT
 quants_decimals = 2
 print(f"{numero:.{quants_decimals}f}")
COORDINAR LLISTES (ZIP)
 gent = ["Mar", "Joan", "Lee", "Nastúrcia"]
 premis = ["Or", "Plata", "Bronze"]
 for persona, premi in zip(gent, premis): # (la més llarga quedarà escapçada)
 print(f"{persona} ha guanyat {premi}.")
 # És un iterador. Si vols guardar el resultat pots convertir-lo en llista:
 resultats = list(zip(gent, premis))
 # >>> [(Mar, Or), (Joan, Plata), (Lee, Bronze)]
TAULA DE VALORS (MAP)
 valors_de_x = [2, 3, 5, -1, 14, 42]
 def f(x):
 return num + 100
 for y in map(f, valors_de_x): # aplica la funció a cada número
 print(y)
 # També és un iterador. Podem guardar la llista convertint-la:
 valors_de_y = list(map(f, valors_de_x)) # [102, 103, 105, 99, 114, 142]
 punts = list(zip(valors_de_x, valors_de_y)) # [(2, 102), (3, 103), ...]