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

    // Dark mode toggle
    const themeToggle = document.getElementById("theme-toggle");
    const currentTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", currentTheme);
    themeToggle.textContent = currentTheme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";

    themeToggle.addEventListener("click", () => {
        const newTheme = document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);
        themeToggle.textContent = newTheme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";
    });
});
