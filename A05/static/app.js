console.log("JavaScript loaded!");

document.addEventListener("DOMContentLoaded", () => {
    // URL validation on form submission
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

    // Dark mode toggle logic
    const toggleButton = document.getElementById("dark-mode-toggle");
    const body = document.body;

    // Check user's saved preference
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("dark-mode");
    }

    toggleButton.addEventListener("click", () => {
        if (body.classList.contains("dark-mode")) {
            body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
        } else {
            body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
        }
    });
});
