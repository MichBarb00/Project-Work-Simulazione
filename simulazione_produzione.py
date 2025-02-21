import time
import random
import statistics
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tqdm import tqdm

# Classe per simulare una singola fase del processo produttivo
class ProcessoProduttivo:
    def __init__(self, nome, durata_media, quantita, efficienza=1.0):
        # Inizializza i parametri della fase di produzione
        self.nome = nome
        self.durata_media = durata_media
        self.quantita = quantita
        self.efficienza = efficienza
        self.tempo_riposo = random.uniform(0.2, 0.5)  # Pausa simulata tra ogni unità
        self.tempi_unitari = []
        self.start_time = None
        self.end_time = None
    
    def eseguire(self):
        """Simula il processo di produzione con una barra di avanzamento dettagliata."""
        durata_totale = 0
        self.start_time = datetime.datetime.now()

        print(f"\n{self.nome} - Avvio produzione: {self.start_time.strftime('%H:%M:%S')}")
        for i in tqdm(range(1, self.quantita + 1), desc=f"Produzione {self.nome}", ncols=100, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} - {elapsed}/{remaining} - Velocità: {rate_fmt}'):
            # Calcola la durata di ogni unità con una variazione casuale basata sull'efficienza
            variazione_efficienza = random.uniform(0.9, 1.1) * self.efficienza
            durata = (random.uniform(self.durata_media * 0.8, self.durata_media * 1.2)) / variazione_efficienza
            durata_totale += durata
            self.tempi_unitari.append(durata)
            print(f"Unità {i}/{self.quantita} - Tempo: {durata:.2f} sec")
            time.sleep(self.tempo_riposo)

        self.end_time = datetime.datetime.now()
        media_tempo = statistics.mean(self.tempi_unitari)
        print(f"{self.nome} COMPLETATO! Tempo totale: {durata_totale:.2f} sec, Tempo medio: {media_tempo:.2f} sec\n")
        return durata_totale, media_tempo

# Classe per simulare un'intera linea di produzione composta da più fasi
class LineaProduzione:
    def __init__(self):
        self.fasi = []
        self.inizio_produzione = None
        self.fine_produzione = None

    def aggiungi_fase(self, fase):
        """Aggiunge una fase alla linea di produzione."""
        self.fasi.append(fase)

    def avvia_produzione(self):
        """Esegue tutte le fasi della linea di produzione."""
        self.inizio_produzione = datetime.datetime.now()
        print(f"\nAvvio della produzione complessiva: {self.inizio_produzione.strftime('%H:%M:%S')}\n")
        tempi_totali = []
        tempi_medi = []
        dettagli_produzione = []

        # Esegue ogni fase e registra i tempi
        for fase in self.fasi:
            tempo_fase, media_fase = fase.eseguire()
            tempi_totali.append(tempo_fase)
            tempi_medi.append(media_fase)
            dettagli_produzione.append((fase.nome, fase.quantita, tempo_fase, media_fase))

        self.fine_produzione = datetime.datetime.now()
        self.analizza_dati(dettagli_produzione)

    def analizza_dati(self, dettagli_produzione):
        """Simula una previsione dei tempi di produzione usando un Random Forest ottimizzato."""
        # Crea un DataFrame con i dettagli di produzione
        df = pd.DataFrame(dettagli_produzione, columns=["Fase", "Quantità", "Tempo Totale (sec)", "Tempo Medio (sec)"])

        # Generazione di dati sintetici realistici per l'addestramento del modello
        np.random.seed(42)
        X = np.random.randint(5, 20, size=(100, 1))
        y = 2.5 * X.flatten() + np.random.normal(0, 2, size=100)

        # Addestramento del modello Random Forest ottimizzato
        modello = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
        modello.fit(X, y)

        # Predizione dei tempi basata sulle quantità delle fasi reali
        previsioni = modello.predict(df["Quantità"].values.reshape(-1, 1))

        # Calcolo delle metriche MAE e RMSE per valutare l'accuratezza
        mae = mean_absolute_error(df["Tempo Totale (sec)"], previsioni)
        rmse = np.sqrt(mean_squared_error(df["Tempo Totale (sec)"], previsioni))

        # Stampa del report finale con i risultati
        print("\n--- Report Finale della Produzione ---\n")
        print(df.to_string(index=False))
        print(f"\nMAE (Mean Absolute Error): {mae:.2f} sec")
        print(f"RMSE (Root Mean Squared Error): {rmse:.2f} sec")

        # Grafico comparativo tra tempi reali e previsti
        plt.figure(figsize=(10, 6))
        plt.plot(df["Quantità"], df["Tempo Totale (sec)"], marker='o', label='Tempi Reali')
        plt.plot(df["Quantità"], previsioni, marker='x', label='Tempi Previsti')
        plt.xlabel("Quantità")
        plt.ylabel("Tempo Totale (sec)")
        plt.title("Confronto Tempi Reali vs Tempi Previsti")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Grafico dell’errore per fase
        errori = df["Tempo Totale (sec)"] - previsioni
        plt.figure(figsize=(10, 6))
        plt.bar(df["Fase"], errori, color='coral')
        plt.xlabel("Fase")
        plt.ylabel("Errore (sec)")
        plt.title("Errore di Predizione per Ogni Fase")
        plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
        plt.xticks(rotation=45)
        plt.show()

# Avvio della simulazione se il file viene eseguito direttamente
if __name__ == "__main__":
    # Definizione delle fasi e delle loro caratteristiche
    prodotti = ["Taglio Materie Prime", "Assemblaggio", "Verniciatura", "Imballaggio", "Controllo Qualità"]
    durate_medie = [2, 3, 2.5, 1.5, 1.0]
    quantita_prodotti = [random.randint(5, 15) for _ in range(5)]
    efficienze = [random.uniform(0.8, 1.2) for _ in range(5)]

    # Creazione della linea di produzione e aggiunta delle fasi
    linea = LineaProduzione()
    for nome, durata, quantita, efficienza in zip(prodotti, durate_medie, quantita_prodotti, efficienze):
        linea.aggiungi_fase(ProcessoProduttivo(nome, durata, quantita, efficienza))

    print("\nSimulazione del processo produttivo avviata!\n")
    linea.avvia_produzione()


