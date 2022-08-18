from flask import Flask, request, jsonify
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import json

app = Flask(__name__)
model_time_arrival = pickle.load(open("model_pickle_baru.pkl", "rb"))
model_congestion = pickle.load(open("rf_pickle.pkl", "rb"))

def pilihan_hari():
    if (day == 'senin'):
        return 0

    elif (day == 'selasa'):
        return 1

    elif (day == 'rabu'):
        return 2

    elif (day == 'kamis'):
       return 3

    elif (day == 'jumat'):
       return 4

    elif (day == 'sabtu'):
        return 5

    elif (day == 'minggu'):
        return 6
    
def pilihan_jalur():
    if (path == 'Cicaheum-Cibereum'):
        return 1

    elif (path == 'Cibereum-Cicaheum'):
        return  2

def pilihan_halte_berangkat():
    if(halteStart=='Terminal Cicaheum'):
       return 0

    elif (halteStart=='Halte Padasuka'):
        return 1

    elif (halteStart =='Halte AH Yani'):
        return 2
        
    elif (halteStart=='Halte Bank Mahyapada'):
        return 3
        
    elif (halteStart =='Halte BTM'):
        return 4
        
    elif (halteStart=='Halte Jl Jakarta'):
        return 5

    elif (halteStart=='Halte KONI'):
        return 6

    elif (halteStart=='Halte Plaza IBCC'):
        return 7

    elif (halteStart=='Halte Jaya Plaza'):
        return 8

    elif (halteStart=='Halte Jl Ketapang'):
        return 9
        
    elif (halteStart=='Halte HSBC'):
        return 10
    
    elif (halteStart=='Halte Halte Alun-Alun'):
        return 11
    
    elif (halteStart=='Halte KEB Hana'):
        return 12

    elif (halteStart=='Halte Mahaypada Tower'):
        return 13
    
    elif (halteStart=='Halte Jendral Sudirman'):
        return 14

    elif (halteStart=='Halte Bunderan Sudirman'):
        return 15

    elif (halteStart=='Halte Jendral Sudirman 3'):
        return 16
    
    elif (halteStart=='Terminal Cibereum'):
        return 17
    
    elif (halteStart=='Halte FIF Grub'):
        return 18
    
    elif (halteStart=='Halte Toko Akbar Jaya'):
        return 19
    
    elif (halteStart=='Halte Stasiun'):
        return 20

    elif (halteStart=='Halte Stasiun Timur'):
        return 21

    elif (halteStart=='Halte Perintis'):
        return 22

    elif (halteStart=='Halte Bank CIMB'):
        return 23

    elif (halteStart=='Halte Veteran'):
        return 24

    elif (halteStart=='Halte Toto Bicycle'):
        return 25

    elif (halteStart=='Halte Persib'):
        return 26

    elif (halteStart=='Halte BRI AH Yani'):
        return 27

    elif (halteStart=='Halte Bank AH Yani'):
        return 28

    elif (halteStart=='Halte Padasuka 2'):
        return 29

def pilihan_halte_tujuan():
    if(halteEnd=='Terminal Cicaheum'):
        return 0

    elif (halteEnd=='Halte Padasuka'):
        return 1

    elif (halteEnd =='Halte AH Yani'):
        return 2
        
    elif (halteEnd=='Halte Bank Mahyapada'):
        return 3
        
    elif (halteEnd =='Halte BTM'):
        return 4
        
    elif (halteEnd=='Halte Jl Jakarta'):
        return 5

    elif (halteEnd=='Halte KONI'):
        return 6

    elif (halteEnd=='Halte Plaza IBCC'):
        return 7

    elif (halteEnd=='Halte Jaya Plaza'):
        return 8

    elif (halteEnd=='Halte Jl Ketapang'):
        return 9
        
    elif (halteEnd=='Halte HSBC'):
        return 10
    
    elif (halteEnd=='Halte Halte Alun-Alun'):
        return 11
    
    elif (halteEnd=='Halte KEB Hana'):
        return 12

    elif (halteEnd=='Halte Mahaypada Tower'):
        return 13
    
    elif (halteEnd=='Halte Jendral Sudirman'):
        return 14

    elif (halteEnd=='Halte Bunderan Sudirman'):
        return 15

    elif (halteEnd=='Halte Jendral Sudirman 3'):
        return 16
    
    elif (halteEnd=='Terminal Cibereum'):
        return 17
    
    elif (halteEnd=='Halte FIF Grub'):
        return 18
    
    elif (halteEnd=='Halte Toko Akbar Jaya'):
        return 19
    
    elif (halteEnd=='Halte Stasiun'):
        return 20

    elif (halteEnd=='Halte Stasiun Timur'):
        return 21

    elif (halteEnd=='Halte Perintis'):
        return 22

    elif (halteEnd=='Halte Bank CIMB'):
        return 23

    elif (halteEnd=='Halte Veteran'):
        return 24

    elif (halteEnd=='Halte Toto Bicycle'):
        return 25

    elif (halteEnd=='Halte Persib'):
        return 26

    elif (halteEnd=='Halte BRI AH Yani'):
        return 27

    elif (halteEnd=='Halte Bank AH Yani'):
        return 28

    elif (halteEnd=='Halte Padasuka 2'):
        return 29

def deskripsi_jam_sibuk():
    if ((deptime_hour >= 6 and deptime_hour <= 9) or (deptime_hour >= 16 and deptime_hour <= 18)):
        return 1
    elif ((deptime_hour == 9 and deptime_minute <= 0) or (deptime_hour == 16 and deptime_minute <= 0)):
        return 2
    else:
        return 2

def list_converter(input):
    for item in range(len(input)):
        if(input[item] == [1]):
            congestion_list_number.append(1)

        elif(input[item] == [2]):
            congestion_list_number.append(2)

        elif(input[item] == [3]):
            congestion_list_number.append(3)
        else:
            congestion_list_number.append(4)
    
    return congestion_list_number


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    global  deptime, deptime_hour, deptime_minute, day, halteStart, halteEnd, path, Hari, Halte_Awal, Halte_Sampai, jam_sibuk, congestion_list, congestion_list_number
    content_type = request.headers.get('Content-Type')
    congestion_list = []
    congestion_list_number = []
    if (content_type == 'application/json'):
        json = request.json

        deptime = json['deptime']
        day = json['day']
        halteEnd = json['halteEnd']
        halteStart = json['halteStart']
        path = json['path']

        deptime_hour = int(pd.to_datetime(deptime, format ="%H:%M").hour)
        deptime_minute = int(pd.to_datetime(deptime, format ="%H:%M").minute)

        Hari = pilihan_hari()
        Jalur = pilihan_jalur()
        Halte_Awal = pilihan_halte_berangkat()
        Halte_Sampai = pilihan_halte_tujuan()
        jam_sibuk = deskripsi_jam_sibuk()

        
        prediction1=model_time_arrival.predict([[
            deptime_hour,
            deptime_minute,
            Hari,
            Jalur,
            Halte_Awal,
            Halte_Sampai
        ]])

        if (Jalur == 1):
            for congestion in range(17):
                prediction2=model_congestion.predict([[
                    Hari + 1,
                    jam_sibuk,
                    congestion,
                ]])
                congestion_list.append(prediction2)
        elif(Jalur == 2):
            congestion_list = []
            congestion_list.append(4)

        output=round(prediction1[0],5)

        convert_array_to_number = list_converter(congestion_list)
        dict = convert_array_to_number

        json_type = jsonify(output, dict)

        return json_type
    else:
        return 'Content-Type not supported!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
