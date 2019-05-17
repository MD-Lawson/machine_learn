#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
count = 0
salaryCount = 0
emailCount = 0
totalPayments = 0
for person in enron_data:
    
    if enron_data[person]['poi'] == 1:
        count += 1
    if enron_data[person]['salary'] != 'NaN':
        salaryCount += 1
    if enron_data[person]['email_address'] != 'NaN':
        emailCount += 1 
    if enron_data[person]['total_payments'] == 'NaN' and enron_data[person]['poi'] == 1:
        totalPayments += 1

percentagePayments = (totalPayments/len(enron_data))*100
print('total payments:', totalPayments, '\nPercentage of Payments:', percentagePayments, '%')
print('Num poi:', count)
print(salaryCount)
print(emailCount)
print('Size of data set:', len(enron_data))



