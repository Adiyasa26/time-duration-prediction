from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model_pickle_baru.pkl", "rb"))

  

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        global  Halte_Awal, Halte_Sampai

        date_dep = request.form["Dep_Time"]
        Jam = int(pd.to_datetime(date_dep, format ="%H:%M").hour)
        Menit = int(pd.to_datetime(date_dep, format ="%H:%M").minute)

        Hari_berangkat = request.form["hari"]
        if (Hari_berangkat == 'senin'):
            Hari = 0

        elif (Hari_berangkat == 'selasa'):
            Hari = 1

        elif (Hari_berangkat == 'rabu'):
            Hari = 2

        elif (Hari_berangkat == 'kamis'):
            Hari = 3

        elif (Hari_berangkat == 'jumat'):
            Hari = 4

        elif (Hari_berangkat == 'sabtu'):
            Hari = 5

        elif (Hari_berangkat == 'minggu'):
            Hari = 6


        Jalur_berangkat = request.form["subject"]
        if (Jalur_berangkat == 'Cicaheum-Cibereum'):
            Jalur = 1

        elif (Jalur_berangkat == 'Cibereum-Cicaheum'):
            Jalur = 2


        Halte = request.form['topic']
        if(Halte=='Terminal Cicaheum'):
            Halte_Awal = 0
        elif (Halte=='Halte Padasuka'):
            Halte_Awal = 1

        elif (Halte =='Halte AH Yani'):
            Halte_Awal = 2
            
        elif (Halte=='Halte Bank Mahyapada'):
            Halte_Awal = 3
            
        elif (Halte =='Halte BTM'):
            Halte_Awal = 4
            
        elif (Halte=='Halte Jl Jakarta'):
            Halte_Awal = 5

        elif (Halte=='Halte KONI'):
            Halte_Awal = 6

        elif (Halte=='Halte Plaza IBCC'):
            Halte_Awal = 7

        elif (Halte=='Halte Jaya Plaza'):
            Halte_Awal = 8

        elif (Halte=='Halte Jl Ketapang'):
            Halte_Awal = 9
            
        elif (Halte=='Halte HSBC'):
            Halte_Awal = 10
        
        elif (Halte=='Halte Halte Alun-Alun'):
            Halte_Awal = 11
        
        elif (Halte=='Halte KEB Hana'):
            Halte_Awal = 12

        elif (Halte=='Halte Mahaypada Tower'):
            Halte_Awal = 13
        
        elif (Halte=='Halte Jendral Sudirman'):
            Halte_Awal = 14

        elif (Halte=='Halte Bunderan Sudirman'):
            Halte_Awal = 15

        elif (Halte=='Halte Jendral Sudirman 3'):
            Halte_Awal = 16
        
        elif (Halte=='Terminal Cibereum'):
            Halte_Awal = 17
        
        elif (Halte=='Halte FIF Grub'):
            Halte_Awal = 18
        
        elif (Halte=='Halte Toko Akbar Jaya'):
            Halte_Awal = 19
        
        elif (Halte=='Halte Stasiun'):
            Halte_Awal = 20

        elif (Halte=='Halte Stasiun Timur'):
            Halte_Awal = 21

        elif (Halte=='Halte Perintis'):
            Halte_Awal = 22

        elif (Halte=='Halte Bank CIMB'):
            Halte_Awal = 23

        elif (Halte=='Halte Veteran'):
            Halte_Awal = 24

        elif (Halte=='Halte Toto Bicycle'):
            Halte_Awal = 25

        elif (Halte=='Halte Persib'):
            Halte_Awal = 26

        elif (Halte=='Halte BRI AH Yani'):
            Halte_Awal = 27

        elif (Halte=='Halte Bank AH Yani'):
            Halte_Awal = 28

        elif (Halte=='Halte Padasuka 2'):
            Halte_Awal = 29



        Halte_Akhir = request.form['chapter']
        if(Halte_Akhir=='Terminal Cicaheum'):
            Halte_Sampai = 0
        elif (Halte_Akhir=='Halte Padasuka'):
            Halte_Sampai = 1

        elif (Halte_Akhir =='Halte AH Yani'):
            Halte_Sampai = 2
            
        elif (Halte_Akhir=='Halte Bank Mahyapada'):
            Halte_Sampai = 3
            
        elif (Halte_Akhir =='Halte BTM'):
            Halte_Sampai = 4
            
        elif (Halte_Akhir=='Halte Jl Jakarta'):
            Halte_Sampai = 5

        elif (Halte_Akhir=='Halte KONI'):
            Halte_Sampai = 6

        elif (Halte_Akhir=='Halte Plaza IBCC'):
            Halte_Sampai = 7

        elif (Halte_Akhir=='Halte Jaya Plaza'):
            Halte_Sampai = 8

        elif (Halte_Akhir=='Halte Jl Ketapang'):
            Halte_Sampai = 9
            
        elif (Halte_Akhir=='Halte HSBC'):
            Halte_Sampai = 10
        
        elif (Halte_Akhir=='Halte Halte Alun-Alun'):
            Halte_Sampai = 11
        
        elif (Halte_Akhir=='Halte KEB Hana'):
            Halte_Sampai = 12

        elif (Halte_Akhir=='Halte Mahaypada Tower'):
            Halte_Sampai = 13
        
        elif (Halte_Akhir=='Halte Jendral Sudirman'):
            Halte_Sampai = 14

        elif (Halte_Akhir=='Halte Bunderan Sudirman'):
            Halte_Sampai = 15

        elif (Halte_Akhir=='Halte Jendral Sudirman 3'):
            Halte_Sampai = 16
        
        elif (Halte_Akhir=='Terminal Cibereum'):
            Halte_Sampai = 17
        
        elif (Halte_Akhir=='Halte FIF Grub'):
            Halte_Sampai = 18
        
        elif (Halte_Akhir=='Halte Toko Akbar Jaya'):
            Halte_Sampai = 19
        
        elif (Halte_Akhir=='Halte Stasiun'):
            Halte_Sampai = 20

        elif (Halte_Akhir=='Halte Stasiun Timur'):
            Halte_Sampai = 21

        elif (Halte_Akhir=='Halte Perintis'):
            Halte_Sampai = 22

        elif (Halte_Akhir=='Halte Bank CIMB'):
            Halte_Sampai = 23

        elif (Halte_Akhir=='Halte Veteran'):
            Halte_Sampai = 24

        elif (Halte_Akhir=='Halte Toto Bicycle'):
            Halte_Sampai = 25

        elif (Halte_Akhir=='Halte Persib'):
            Halte_Sampai = 26

        elif (Halte_Akhir=='Halte BRI AH Yani'):
            Halte_Sampai = 27

        elif (Halte_Akhir=='Halte Bank AH Yani'):
            Halte_Sampai = 28

        elif (Halte_Akhir=='Halte Padasuka 2'):
            Halte_Sampai = 29
        
        prediction=model.predict([[
            Jam,
            Menit,
            Hari,
            Jalur,
            Halte_Awal,
            Halte_Sampai
        ]])

        output=round(prediction[0],5)

        return render_template('home.html',prediction_text="Waktu Kedatangan Anda: {} Menit".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
