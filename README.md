# Project-Work-Simulazione
# Simulazione del Processo Produttivo

## Descrizione
Questo progetto simula un processo produttivo composto da più fasi: Taglio Materie Prime, Assemblaggio, Verniciatura, Imballaggio e Controllo Qualità.  
Per ogni fase viene calcolato il tempo totale e medio di produzione. Al termine della simulazione, il modello Random Forest prevede i tempi basandosi sui dati raccolti e confronta i risultati con quelli reali.  

## Requisiti
- **Python:** Versione 3.10 o superiore  
- **Librerie necessarie:**  
  - `pandas` (gestione dei dati)  
  - `numpy` (calcoli numerici)  
  - `matplotlib` (grafici)  
  - `scikit-learn` (modelli di machine learning)  
  - `tqdm` (barra di avanzamento)  

## Installazione
1. **Clona la repository:**  
```bash
git clone https://github.com/MichBarb00/Project-Work-Simulazione.git
```

2. **Installa le librerie richieste:**  
```bash
pip install pandas numpy matplotlib scikit-learn tqdm
```

## Esecuzione del Progetto
Per avviare la simulazione, eseguire il file principale:  
```bash
python simulazione_produzione.py
```
Durante l'esecuzione, la barra di avanzamento mostra il progresso di ogni fase. Al termine, verranno generati:  
- Un report finale con i tempi totali, medi, MAE e RMSE  
- Due grafici:  
   - **Confronto** tra tempi reali e previsti  
   - **Errore di predizione** per ogni fase  

## Output della Simulazione
Esempio del report finale:
```
--- Report Finale della Produzione ---

         Fase               Quantità   Tempo Totale (sec)   Tempo Medio (sec)
Taglio Materie Prime           10              20.50              2.05
Assemblaggio                   12              35.60              2.97
Verniciatura                    8              19.40              2.42
Imballaggio                     6              10.80              1.80
Controllo Qualità              14              14.20              1.01

MAE (Mean Absolute Error): 8.25 sec
RMSE (Root Mean Squared Error): 10.03 sec
```

##  Struttura della Repository
```
Project-Work-Simulazione
├── simulazione_produzione.py
└── README.md
```

##  Funzionalità Principali
+ Simulazione dettagliata con barra di avanzamento  
+ Calcolo di tempo totale e medio per ogni fase  
+ Previsione dei tempi usando Random Forest  
+ Grafici chiari e leggibili per l’analisi dei risultati  
