console.log("JavaScript loaded!");

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", (event) => {
            const urlInput = document.getElementById("url");
            if (urlInput && !urlInput.value.startsWith("http")) {
                alert("Please enter a valid URL (starting with http or https).");
                event.preventDefault();
            }
        });
    }
});
