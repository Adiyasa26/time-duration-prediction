var jalur={
    cicaheum:['Terminal Cicaheum', 'Halte Padasuka', 'Halte AH Yani', 'Halte Bank Mahyapada', 'Halte BTM', 'Halte Jl Jakarta', 
    'Halte KONI', 'Halte Plaza IBCC', 'Halte Jaya Plaza', 'Halte Jl Ketapang', 'Halte HSBC', 'Halte Alun-alun', 'Halte KEB Hana',
    'Halte Mahyapada Tower', 'Halte Jendral Sudirman', 'Halte Bunderan Sudirman', 'Halte Jendral Sudirman 3'],
    cibereum:['Terminal Cicaheum', 'Halte FIF Grub', 'Halte Toko Akbar', 'Halte Stasiun', 'Halte Stasiun Timur', 'Halte Perintis',
    'Halte Bank CIMB', 'Halte Veteran', 'Halte Toto Bycycle', 'Halte Persib', 'Halte BRI AH Yani', 'Halte Bank AH Yani', 'Halte Padasuka2']
}

// getting the main and sub menus
 
var main = document.getElementById('jalur');
var sub = document.getElementById('halte_awal');

main.addEventListener('change', function(){

    var selected_option = jalur[this.value];

    // removing sub menu opstions while loops
    while(sub.options.length > 0 ){

        sub.options.remove(0);
    }

    Array.from(selected_option).forEach(function(el){

    let option = new Option(el, el);
    sub.appendChild(option);
    
    });
})
