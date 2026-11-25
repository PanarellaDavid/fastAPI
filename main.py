# main.py - il server del ping-pong, con la sua pagina web
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# 1. creiamo l'applicazione e rendiamo raggiungibile la cartella static
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. i dati che la rotta POST /gioca riceve: la parola del colpo
class Colpo(BaseModel):
	parola: str

# 3. la pagina principale: il file index.html
@app.get("/")
def home():
	return FileResponse("static/index.html")

colpi = 0

# 4. ping: nessun dato, la risposta è sempre pong
@app.get("/ping")
def ping():
	return {"risposta": "pong"}

# 5. il colpo con GET: la parola arriva nell'indirizzo
@app.get("/gioca")
def gioca(parola: str):
	if parola == "ping":
		return {"risposta": "pong"}
	return {"risposta": "Non ho capito: scrivi ping"}

# 6. il colpo con POST: la parola arriva in JSON, nel corpo della richiesta
@app.post("/gioca")

def gioca_post(colpo: Colpo):
	global colpi
	if colpo.parola.strip().lower() == "ping":
		colpi += 1
		return {"risposta": "Tu: ping. -> Server: pong", "colpi": colpi}
		
	return {"risposta": "Non ho capito: scrivi ping"}

@app.get("/somma")
def somma(a: float, b: float):
	return {"risultato": a + b}