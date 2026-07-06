document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".sidebar-tree a.reference").forEach(function (link) {
        if (link.textContent.trim() === "References") {
            var checkbox = link.closest("li").querySelector(".toctree-checkbox");
            if (checkbox) {
                checkbox.checked = true;
            }
        }
    });
});
