
"""
    Created on Fri Apr 10 09:36:36 2020

    @author: babalola
"""


input_data = {
        'region': {
        'name': "Africa",
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71
         },
        'periodType': "days",
        'timeToElapse': 58,
        'reportedCases': 674,
        'population': 66622705,
        'totalHospitalBeds': 1380614
        }


"""output_data  = {
    'data': {}, # the input data you got
    'impact': {}, # your best case estimation
    'severeImpact': {} #your severe case estimation
    }
"""
data = 'reportedCases'

def estimator(data):
    currentlyInfected = input_data[data] * 10
    severeImpact = input_data[data] * 50
    infectionByRequestedTime = currentlyInfected * 512
    data  = {
    'data': {'reportedCases'}, # the input data you got
    'impact': {'currentlyInfected': currentlyInfected, 'infectionByRequestedTime': infectionByRequestedTime}, # your best case estimation
    'severeImpact': {'currentlyInfected': severeImpact, 'infectionByRequestedTime': severeImpact * 512} #your severe case estimation
    }
    return data
print(estimator(data))

