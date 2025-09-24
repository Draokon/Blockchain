# Custom Hash Generator

## Aprašymas
Programa sugeneruoja paprastą hash'a Python kalba. 

### Algoritmo idėja

funkcija hash(text):     
jei simbolis yra *list* -> pakeisti jį į tam tikrą simbolį,jei ne - nekeisti.

funkcija insert(text):   
įterpia *salt* į teksto vidurį

funkcija add_letters(text):   
po kiekvieno simbolio prideda dar vieną, kuris yra 5tas abėcėlėje po jo. 

funkcija substitute(text):   
paslenka simbolį 5 pozicijomis į priekį ir jį pakeičia, jei nėra to simbolio, tia palieka

funkcija move(text):   
kas 2 pozicijas sukeičia simbolių poras vietomis

funkcija swap(text):  
jei *text* ilgis nesidalina iš 3 -> prideda "x", suskirsto *text* į 3 simbolių blokus ir kiekvieną apverčia atbulai.

funkcija fixed_hash(text):  
pritaiko *hash* ir *salt*  
suskaičiuoja ASCII simbolių sumą (kad papildomai išmaišytų)  
jei tekstas trumpesnis už 16 simbolių, tai kartoja, kad iki tol kol pasieks 16 simbolių  
jei tekstas ilgesnis -> paima pirmus 16 simbolių  


skaitymas iš failo:  
perskaito failą ir šifruoja tvarka:   
hash -> insert -> add_letters -> substitute -> move -> swap -> fixed_hash
