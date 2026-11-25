# 01

1. Che cos’è un codespace? Dove gira, e che cosa ti serve per usarlo da un altro computer?

Un codespace  è un ambiente virtuale separato dal pc in uso, gira su un server di proprietà dell'azienda dietro Github. Per accedervi da un altro pc, basta avere una connesione internet e l'account github con cui è stato creato in origine


2. A che cosa serve l’ambiente virtuale .venv , e perché non deve finire su GitHub?

L'ambiente virtuale .venv serve per avere un ambiente separato sul nostro computer. Non deve finire su Github poichè è un ambiente separato, destinato a essere privato


3. Che differenza c’è tra Commit e Sync Changes?

Commit crea il commit nel codespace, Sync serve per mandare il commit nella repository Github


# 02

1. Nel Passo 2 l’indirizzo principale risponde {"detail":"Not Found"} , con il codice 404; dopo il Passo 7 mostra la pagina. Che cosa è cambiato in main.py ?

Nel passo 2, il server non aveva un rimando per "/", nel passo7 però "/" ha rimando alla pagina html


2.  Che differenza c’è tra la richiesta GET /gioca?parola=ping e la richiesta POST /gioca ? Dove viaggia la parola nei due casi?

"/gioca?parola=ping" imposta in automatico la parola, "/gioca" invece la fà immettere sul momento


3. A che cosa serve la classe Colpo ? Che cosa risponde il server se nel JSON manca il campo parola ?

La classe Colpo serve per avere un oggetto colpo con le varie impostazioni, se manca la parola, il JSON  non fà mandare


4. Molti servizi veri hanno una rotta come /ping , che risponde sempre la stessa cosa. A che cosa serve?

Serve per fare i vari test