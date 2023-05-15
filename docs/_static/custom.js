function changeMultipleCSS() {
    // Defining all our CSS styles
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
    // elements.style.cssText = myStyles;
}

window.addEventListener("load", function(){
    changeMultipleCSS();
    const button = document.querySelector("button.theme-switch-button");
    button.addEventListener("click", changeMultipleCSS);
});