import time
import random
import statistics
import datetime

class ProcessoProduttivo:
    def __init__(self, nome, durata_media, quantita, efficienza=1.0):
        self.nome = nome
        self.durata_media = durata_media
        self.quantita = quantita
        self.efficienza = efficienza  # Influenza sulla velocità di produzione
        self.tempo_riposo = random.uniform(0.2, 0.5)  # Simula pausa tra unità prodotte
        self.tempi_unitari = []
        self.start_time = None
        self.end_time = None
    
    def eseguire(self):
        """Simula il processo di produzione di un certo numero di unità."""
        durata_totale = 0
        self.start_time = datetime.datetime.now()
        
        for i in range(1, self.quantita + 1):
            variazione_efficienza = random.uniform(0.9, 1.1) * self.efficienza
            durata = (random.uniform(self.durata_media * 0.8, self.durata_media * 1.2)) / variazione_efficienza
            durata_totale += durata
            self.tempi_unitari.append(durata)
            print(f"{self.nome}: produzione unità {i}/{self.quantita} - tempo: {durata:.2f} sec")
            time.sleep(self.tempo_riposo)
        
        self.end_time = datetime.datetime.now()
        media_tempo = statistics.mean(self.tempi_unitari)
        print(f"{self.nome} COMPLETATO! Tempo totale: {durata_totale:.2f} sec (Tempo medio per unità: {media_tempo:.2f} sec)")
        return durata_totale, media_tempo

class LineaProduzione:
    def __init__(self):
        self.fasi = []
        self.inizio_produzione = None
        self.fine_produzione = None
    
    def aggiungi_fase(self, fase):
        """Aggiunge una fase alla linea di produzione."""
        self.fasi.append(fase)
    
    def avvia_produzione(self):
        """Esegue tutte le fasi della produzione registrando il tempo totale."""
        self.inizio_produzione = datetime.datetime.now()
        print("\nAvvio della produzione...\n")
        tempi_totali = []
        tempi_medi = []
        
        for fase in self.fasi:
            tempo_fase, media_fase = fase.eseguire()
            tempi_totali.append(tempo_fase)
            tempi_medi.append(media_fase)
        
        self.fine_produzione = datetime.datetime.now()
        tempo_complessivo = sum(tempi_totali)
        media_globale = statistics.mean(tempi_medi)
        print(f"\nProduzione COMPLETATA! Tempo complessivo: {tempo_complessivo:.2f} sec")
        print(f"Tempo medio di produzione per unità: {media_globale:.2f} sec")

    def report_finale(self):
        """Genera un report finale della produzione."""
        print("\n--- Report Finale Produzione ---\n")
        print(f"Inizio produzione: {self.inizio_produzione.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Fine produzione: {self.fine_produzione.strftime('%Y-%m-%d %H:%M:%S')}")
        for fase in self.fasi:
            print(f"Fase: {fase.nome}, Quantità: {fase.quantita}, Efficienza: {fase.efficienza:.2f}")
        print("\nAnalisi completata. Valutare possibili ottimizzazioni per il prossimo ciclo di produzione.\n")

if __name__ == "__main__":
    print("\nSimulazione del processo produttivo avviata!\n")
    
    # Definizione dei processi produttivi
    prodotti = ["Taglio Materie Prime", "Assemblaggio", "Verniciatura", "Imballaggio", "Controllo Qualità"]
    durate_medie = [2, 3, 2.5, 1.5, 1.0]
    quantita_prodotti = [random.randint(5, 15) for _ in range(5)]
    efficienze = [random.uniform(0.8, 1.2) for _ in range(5)]
    
    # Configurazione della linea di produzione
    linea = LineaProduzione()
    for nome, durata, quantita, efficienza in zip(prodotti, durate_medie, quantita_prodotti, efficienze):
        print(f"Configurazione: {nome} - {quantita} unità previste, Efficienza stimata: {efficienza:.2f}")
        linea.aggiungi_fase(ProcessoProduttivo(nome, durata, quantita, efficienza))
    
    # Avvio della produzione
    linea.avvia_produzione()
    linea.report_finale()
    
    print("\nSimulazione completata. Grazie per aver utilizzato il nostro sistema!")