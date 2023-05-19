function changeTableCSS() {
    const curr_theme = document.querySelector("html").attributes['data-theme'].value
    let myStyles = "";
    if (curr_theme == 'dark'){
        myStyles = `
        background-color: rgb(55, 55, 55);
        `;
    }
    else if (curr_theme == 'light'){
        myStyles = `
        background-color: rgb(235, 235, 235);
        `;
    }
    const elements = document.querySelectorAll("table.striped-table tr:nth-child(even)");
    elements.forEach((e)=>e.style.cssText = myStyles)
}

function createChart() {
    const canvas_bprmax = document.querySelector('canvas.bar-chart[id="bprmax"]');
    const tables_bprmax = document.querySelectorAll('table.bprmax'); 
    var bprmax_labels = [];
    var bprmax_rec_20 = [];
    for (var i = 0; i < tables_bprmax.length; ++i){
        const table = tables_bprmax[i];
        const rows = table.getElementsByTagName('tr');
        var array_recall_20 = Array.from(rows, row => row.cells[8].firstChild.innerHTML).slice(1,);
        var array_model_names = Array.from(rows, row => row.cells[0].firstChild.innerHTML).slice(1,);
        bprmax_rec_20 = bprmax_rec_20.concat(array_recall_20)
        bprmax_labels = bprmax_labels.concat(array_model_names)
        break;
    } 
    new Chart(
    canvas_bprmax, 
        {
            type: 'bar',
            data: {
                labels: bprmax_labels,
                datasets: [
                    {
                    label: '# of Votes',
                    data: bprmax_rec_20,
                    borderWidth: 1,
                    barThickness: 10
                    }
                ]
            },
            options: {
                scales: {
                    y: {beginAtZero: true}
                }
            }
        }
    );
}

window.addEventListener("load", function(){
    changeTableCSS();
    const button = document.querySelector("button.theme-switch-button");
    button.addEventListener("click", changeTableCSS);
    createChart();
});