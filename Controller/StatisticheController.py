from datetime import datetime, timedelta

from Model.Atleta import Atleta
from Model.Gara import Gara


class StatisticheController:
    @staticmethod
    def get_statistiche_iscritti_per_livello():
        atleti = Atleta.get_lista_atleti()
        totale_iscritti = len(atleti)
        iscritti_per_livello = {}

        for atleta in atleti.values():
            livello = atleta.livello_atleta
            if livello not in iscritti_per_livello:
                iscritti_per_livello[livello] = 0
            iscritti_per_livello[livello] += 1

        percentuali_per_livello = {livello: (count / totale_iscritti) * 100 for livello, count in iscritti_per_livello.items()}
        return totale_iscritti, iscritti_per_livello, percentuali_per_livello

    @staticmethod
    def get_statistiche_risultati_per_livello():
        all_risultati = Gara.get_all_risultati()
        atleti = Atleta.get_lista_atleti()
        risultati_per_livello = {}

        for risultati in all_risultati.values():
            for cf, risultato in risultati.items():
                atleta = atleti.get(cf)
                if atleta:
                    livello = atleta.livello_atleta
                    if livello not in risultati_per_livello:
                        risultati_per_livello[livello] = 0
                    risultati_per_livello[livello] += 1

        totale_risultati = sum(risultati_per_livello.values())
        percentuali_risultati = {livello: (count / totale_risultati) * 100 for livello, count in risultati_per_livello.items()}
        return totale_risultati, risultati_per_livello, percentuali_risultati

    @staticmethod
    def get_certificati_in_scadenza():
        atleti = Atleta.get_lista_atleti()
        oggi = datetime.now()
        settimana_prossima = oggi + timedelta(days=7)
        prossimo_mese = oggi + timedelta(days=30)

        certificati_settimana = []
        certificati_mese = []

        for atleta in atleti.values():
            if isinstance(atleta.scadenza_certificato_medico, str):
                try:
                    atleta.scadenza_certificato_medico = datetime.strptime(atleta.scadenza_certificato_medico, "%Y-%m-%d")
                except ValueError as e:
                    print(f"Error parsing date for atleta {atleta.cf}: {e}")
                    continue
            if oggi <= atleta.scadenza_certificato_medico <= settimana_prossima:
                certificati_settimana.append(atleta)
            if oggi <= atleta.scadenza_certificato_medico <= prossimo_mese:
                certificati_mese.append(atleta)

        return certificati_settimana, certificati_mese

    @staticmethod
    def get_statistiche_risultati_tipo():
        all_risultati = Gara.get_all_risultati()
        tipi_risultati = {"oro": 0, "argento": 0, "bronzo": 0, "squalifica": 0}

        for risultati in all_risultati.values():
            for risultato in risultati.values():
                risultato = risultato.lower()
                if risultato in tipi_risultati:
                    tipi_risultati[risultato] += 1

        totale_risultati = sum(tipi_risultati.values())
        percentuali_risultati = {tipo: (count / totale_risultati) * 100 for tipo, count in tipi_risultati.items()}
        return totale_risultati, tipi_risultati, percentuali_risultati
