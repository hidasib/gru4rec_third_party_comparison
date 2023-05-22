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

function createChart(canvas, models_metrics, plot_bar_colors, plot_bar_border_colors, chart_label) {
    let screen_width = document.documentElement.clientWidth;
    if ((screen_width > 992) || (window.orientation > 0)) {
        border_width = 3 //6.5
        bar_thickness = 30
    }
    else {
        border_width = 1.5
        bar_thickness = 15
    }
    
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
                    borderWidth: border_width,
                    barThickness: bar_thickness,
                    backgroundColor: plot_bar_colors,
                    borderColor: plot_bar_border_colors,
                    }
                ]
            },
            options: { 
                scales: {y: {beginAtZero: true} },
            }
        }
    );
}

const colors_0 = "#e60049";
const colors = ["#0bb4ff", "#50e991", "#e6d800", "#9b19f5", "#ffa300", "#dc0ab4", "#b3d4ff", "#00bfa0"];

function createChartByDataset(table_id, column_index, chart_label) {
    const canvas = document.querySelector(`canvas.bar-chart[id="${table_id}_${chart_label}"]`);
    if (canvas == null) {
        return;
    }
    const tables = document.querySelectorAll(`table.${table_id}`); 
    var models_metrics = {};
    var plot_bar_colors = [];
    var plot_bar_border_colors = [];
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

        new_colors = Array(no_new_items).fill(colors[i%colors.length])
        plot_bar_colors = plot_bar_colors.concat(new_colors)
        new_colors[0] = colors_0
        if (i == 0) {
            new_colors[1] = colors_0
        }
        plot_bar_border_colors = plot_bar_border_colors.concat(new_colors)

    }
    plot_bar_colors[0] = colors_0;
    // plot_bar_border_colors[0] = colors_0;
    createChart(canvas, models_metrics, plot_bar_colors, plot_bar_border_colors, chart_label)    
}

window.addEventListener("load", function(){
    changeTableCSS();
    createChartByDataset("bprmax", 8, "Recall@20");
    createChartByDataset("xe", 8, "Recall@20");
    createChartByDataset("bprmax", 9, "MRR@20");
    createChartByDataset("xe", 9, "MRR@20");
    const button = document.querySelector("button.theme-switch-button");
    button.addEventListener("click", changeTableCSS);
});