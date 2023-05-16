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

window.addEventListener("load", function(){
    changeTableCSS();
    const button = document.querySelector("button.theme-switch-button");
    button.addEventListener("click", changeTableCSS);
});