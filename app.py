from flask import Flask, request, jsonify
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import json

app = Flask(__name__)
model = pickle.load(open("model_pickle_baru.pkl", "rb"))

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    global  deptime, day, halteStart, halteEnd, path, Halte_Awal, Halte_Sampai
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json

        deptime = json['deptime']
        day = json['day']
        halteEnd = json['halteEnd']
        halteStart = json['halteStart']
        path = json['path']

        deptime_hour = int(pd.to_datetime(deptime, format ="%H:%M").hour)
        deptime_minute = int(pd.to_datetime(deptime, format ="%H:%M").minute)

        if (day == 'senin'):
            Hari = 0

        elif (day == 'selasa'):
            Hari = 1

        elif (day == 'rabu'):
            Hari = 2

        elif (day == 'kamis'):
            Hari = 3

        elif (day == 'jumat'):
            Hari = 4

        elif (day == 'sabtu'):
            Hari = 5

        elif (day == 'minggu'):
            Hari = 6

        if (path == 'Cicaheum-Cibereum'):
            Jalur = 1

        elif (path == 'Cibereum-Cicaheum'):
            Jalur = 2

        if(halteStart=='Terminal Cicaheum'):
            Halte_Awal = 0
        elif (halteStart=='Halte Padasuka'):
            Halte_Awal = 1

        elif (halteStart =='Halte AH Yani'):
            Halte_Awal = 2
            
        elif (halteStart=='Halte Bank Mahyapada'):
            Halte_Awal = 3
            
        elif (halteStart =='Halte BTM'):
            Halte_Awal = 4
            
        elif (halteStart=='Halte Jl Jakarta'):
            Halte_Awal = 5

        elif (halteStart=='Halte KONI'):
            Halte_Awal = 6

        elif (halteStart=='Halte Plaza IBCC'):
            Halte_Awal = 7

        elif (halteStart=='Halte Jaya Plaza'):
            Halte_Awal = 8

        elif (halteStart=='Halte Jl Ketapang'):
            Halte_Awal = 9
            
        elif (halteStart=='Halte HSBC'):
            Halte_Awal = 10
        
        elif (halteStart=='Halte Halte Alun-Alun'):
            Halte_Awal = 11
        
        elif (halteStart=='Halte KEB Hana'):
            Halte_Awal = 12

        elif (halteStart=='Halte Mahaypada Tower'):
            Halte_Awal = 13
        
        elif (halteStart=='Halte Jendral Sudirman'):
            Halte_Awal = 14

        elif (halteStart=='Halte Bunderan Sudirman'):
            Halte_Awal = 15

        elif (halteStart=='Halte Jendral Sudirman 3'):
            Halte_Awal = 16
        
        elif (halteStart=='Terminal Cibereum'):
            Halte_Awal = 17
        
        elif (halteStart=='Halte FIF Grub'):
            Halte_Awal = 18
        
        elif (halteStart=='Halte Toko Akbar Jaya'):
            Halte_Awal = 19
        
        elif (halteStart=='Halte Stasiun'):
            Halte_Awal = 20

        elif (halteStart=='Halte Stasiun Timur'):
            Halte_Awal = 21

        elif (halteStart=='Halte Perintis'):
            Halte_Awal = 22

        elif (halteStart=='Halte Bank CIMB'):
            Halte_Awal = 23

        elif (halteStart=='Halte Veteran'):
            Halte_Awal = 24

        elif (halteStart=='Halte Toto Bicycle'):
            Halte_Awal = 25

        elif (halteStart=='Halte Persib'):
            Halte_Awal = 26

        elif (halteStart=='Halte BRI AH Yani'):
            Halte_Awal = 27

        elif (halteStart=='Halte Bank AH Yani'):
            Halte_Awal = 28

        elif (halteStart=='Halte Padasuka 2'):
            Halte_Awal = 29


        if(halteEnd=='Terminal Cicaheum'):
            Halte_Sampai = 0
        elif (halteEnd=='Halte Padasuka'):
            Halte_Sampai = 1

        elif (halteEnd =='Halte AH Yani'):
            Halte_Sampai = 2
            
        elif (halteEnd=='Halte Bank Mahyapada'):
            Halte_Sampai = 3
            
        elif (halteEnd =='Halte BTM'):
            Halte_Sampai = 4
            
        elif (halteEnd=='Halte Jl Jakarta'):
            Halte_Sampai = 5

        elif (halteEnd=='Halte KONI'):
            Halte_Sampai = 6

        elif (halteEnd=='Halte Plaza IBCC'):
            Halte_Sampai = 7

        elif (halteEnd=='Halte Jaya Plaza'):
            Halte_Sampai = 8

        elif (halteEnd=='Halte Jl Ketapang'):
            Halte_Sampai = 9
            
        elif (halteEnd=='Halte HSBC'):
            Halte_Sampai = 10
        
        elif (halteEnd=='Halte Halte Alun-Alun'):
            Halte_Sampai = 11
        
        elif (halteEnd=='Halte KEB Hana'):
            Halte_Sampai = 12

        elif (halteEnd=='Halte Mahaypada Tower'):
            Halte_Sampai = 13
        
        elif (halteEnd=='Halte Jendral Sudirman'):
            Halte_Sampai = 14

        elif (halteEnd=='Halte Bunderan Sudirman'):
            Halte_Sampai = 15

        elif (halteEnd=='Halte Jendral Sudirman 3'):
            Halte_Sampai = 16
        
        elif (halteEnd=='Terminal Cibereum'):
            Halte_Sampai = 17
        
        elif (halteEnd=='Halte FIF Grub'):
            Halte_Sampai = 18
        
        elif (halteEnd=='Halte Toko Akbar Jaya'):
            Halte_Sampai = 19
        
        elif (halteEnd=='Halte Stasiun'):
            Halte_Sampai = 20

        elif (halteEnd=='Halte Stasiun Timur'):
            Halte_Sampai = 21

        elif (halteEnd=='Halte Perintis'):
            Halte_Sampai = 22

        elif (halteEnd=='Halte Bank CIMB'):
            Halte_Sampai = 23

        elif (halteEnd=='Halte Veteran'):
            Halte_Sampai = 24

        elif (halteEnd=='Halte Toto Bicycle'):
            Halte_Sampai = 25

        elif (halteEnd=='Halte Persib'):
            Halte_Sampai = 26

        elif (halteEnd=='Halte BRI AH Yani'):
            Halte_Sampai = 27

        elif (halteEnd=='Halte Bank AH Yani'):
            Halte_Sampai = 28

        elif (halteEnd=='Halte Padasuka 2'):
            Halte_Sampai = 29
        
        prediction=model.predict([[
            deptime_hour,
            deptime_minute,
            Hari,
            Jalur,
            Halte_Awal,
            Halte_Sampai
        ]])

        output=round(prediction[0],5)

        return jsonify(output)
    else:
        return 'Content-Type not supported!'

if __name__ == "__main__":
    app.run(debug=True)
