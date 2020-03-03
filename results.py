import wget
import numpy as np


def get_results():
    csv_filename = wget.download('https://media23.bechirot.gov.il/files/expc.csv')
    results_by_city = np.genfromtxt(csv_filename, delimiter=',', dtype=int)[1:, 7:-1]
    results = np.sum(results_by_city, axis=0)
    return results


party_names = {0: 'Avoda-Gesher-Meretz',
               1: 'Yahadut Hatorah',
               2: 'Joint List',
               6: 'Yamina',
               15: 'Israel Beitenu',
               16: 'Likud',
               22: 'Kachol Lavan',
               29: 'Shas'}
