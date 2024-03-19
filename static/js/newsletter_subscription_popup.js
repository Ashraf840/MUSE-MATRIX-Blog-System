let newsSubBox = document.querySelector("#newsSubBox");

if (newsSubBox != null) {
    var newsSubBox_close_btn = document.querySelector("#newsSubBox_close_btn");

    newsSubBox_close_btn.addEventListener("click", (e) => {
        newsSubBox.remove();
    });
}