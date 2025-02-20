import time
import random
import statistics
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tqdm import tqdm

class ProcessoProduttivo:
    def __init__(self, nome, durata_media, quantita, efficienza=1.0):
        self.nome = nome
        self.durata_media = durata_media
        self.quantita = quantita
        self.efficienza = efficienza
        self.tempo_riposo = random.uniform(0.2, 0.5)
        self.tempi_unitari = []
        self.start_time = None
        self.end_time = None
    
    def eseguire(self):
        """Simula il processo di produzione."""
        durata_totale = 0
        self.start_time = datetime.datetime.now()

        print(f"\n{self.nome} - Avvio produzione: {self.start_time.strftime('%H:%M:%S')}")
        for i in tqdm(range(1, self.quantita + 1), desc=f"Produzione {self.nome}", ncols=100):
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

class LineaProduzione:
    def __init__(self):
        self.fasi = []
        self.inizio_produzione = None
        self.fine_produzione = None

    def aggiungi_fase(self, fase):
        self.fasi.append(fase)

    def avvia_produzione(self):
        self.inizio_produzione = datetime.datetime.now()
        print(f"\nAvvio della produzione complessiva: {self.inizio_produzione.strftime('%H:%M:%S')}\n")
        tempi_totali = []
        tempi_medi = []
        dettagli_produzione = []

        for fase in self.fasi:
            tempo_fase, media_fase = fase.eseguire()
            tempi_totali.append(tempo_fase)
            tempi_medi.append(media_fase)
            dettagli_produzione.append((fase.nome, fase.quantita, tempo_fase, media_fase))

        self.fine_produzione = datetime.datetime.now()
        self.visualizza_risultati(tempi_medi, dettagli_produzione)

    def visualizza_risultati(self, tempi_medi, dettagli_produzione):
        """Visualizza il grafico dei tempi medi e il report finale."""
        print("\n--- Report Finale della Produzione ---\n")

        df = pd.DataFrame(dettagli_produzione, columns=["Fase", "Quantità", "Tempo Totale (sec)", "Tempo Medio (sec)"])
        print(df.to_string(index=False))

        print("\nGrafico dei Tempi Medi di Produzione")
        plt.figure(figsize=(8, 5))
        plt.plot(range(len(tempi_medi)), tempi_medi, marker='o', linestyle='-', color='b')
        plt.xlabel("Fasi di produzione")
        plt.ylabel("Tempo medio (sec)")
        plt.title("Andamento dei Tempi Medi di Produzione")
        plt.grid(True)
        plt.show()

        print(f"\nProduzione COMPLETATA con successo alle: {self.fine_produzione.strftime('%H:%M:%S')}\n")

if __name__ == "__main__":
    prodotti = ["Taglio Materie Prime", "Assemblaggio", "Verniciatura", "Imballaggio", "Controllo Qualità"]
    durate_medie = [2, 3, 2.5, 1.5, 1.0]
    quantita_prodotti = [random.randint(5, 15) for _ in range(5)]
    efficienze = [random.uniform(0.8, 1.2) for _ in range(5)]

    linea = LineaProduzione()
    for nome, durata, quantita, efficienza in zip(prodotti, durate_medie, quantita_prodotti, efficienze):
        linea.aggiungi_fase(ProcessoProduttivo(nome, durata, quantita, efficienza))

    print("\nSimulazione del processo produttivo avviata!\n")
    linea.avvia_produzione()
