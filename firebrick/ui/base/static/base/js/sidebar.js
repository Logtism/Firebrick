function collapse() {
    let sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("collapsed");
    let sidebar_container = document.getElementById("page-content");
    sidebar_container.classList.toggle("collapsed-container");
}