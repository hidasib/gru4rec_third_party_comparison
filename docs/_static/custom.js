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

function createChart(table_id, column_index, chart_label) {
    const colors_0 = "#e60049";
    const colors = ["#0bb4ff", "#50e991", "#e6d800", "#9b19f5", "#ffa300", "#dc0ab4", "#b3d4ff", "#00bfa0"];
    const canvas = document.querySelector(`canvas.bar-chart[id=${table_id}]`);
    const tables = document.querySelectorAll(`table.${table_id}`); 
    var models_metrics = {};
    var plot_colors = [];
    for (var i = 0; i < tables.length; ++i){
        const table = tables[i];
        const rows = table.getElementsByTagName('tr');
        var array_recall_20 = Array.from(rows, row => row.cells[column_index].firstChild.innerHTML).slice(1,);
        var array_model_names = Array.from(rows, row => row.cells[0].firstChild.innerHTML).slice(1,);
        var array_variants = Array.from(rows, row => row.cells[1].firstChild.innerHTML).slice(1,);
        array_model_names = array_model_names.map((model_name, i) => `${model_name} ${array_variants[i]}`);
        var m_m = {};
        array_model_names.forEach((key, i) => m_m[key] = array_recall_20[i]);
        no_new_items = Object.keys(models_metrics).length 
        models_metrics = Object.assign({}, models_metrics, m_m)
        no_new_items = Object.keys(models_metrics).length - no_new_items
        plot_colors = plot_colors.concat(Array(no_new_items).fill(colors[i%colors.length]));
    } 
    plot_colors[0] = colors_0;
    console.log(models_metrics)
    new Chart(
    canvas, 
        {
            type: 'bar',
            data: {
                labels: Object.keys(models_metrics),
                datasets: [
                    {
                    label: chart_label,
                    data: Object.values(models_metrics),
                    borderWidth: 1,
                    barThickness: 20,
                    backgroundColor: plot_colors,
                    }
                ]
            },
            options: { 
                scales: {y: {beginAtZero: true} },
            }
        }
    );
}

window.addEventListener("load", function(){
    createChart("bprmax", 8, "Recall@20");
    createChart("xe", 8, "Recall@20");
    changeTableCSS();
    const button = document.querySelector("button.theme-switch-button");
    button.addEventListener("click", changeTableCSS);
});