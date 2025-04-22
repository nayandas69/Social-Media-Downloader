// Function to handle download logic with countdown and spinner
function handleDownload(button) {
    if (button.classList.contains("counting-down")) return; // Prevent double clicks
    button.classList.add("counting-down");

    const link = button.getAttribute("data-link");
    if (!link) {
        alert("Download link not found!");
        button.classList.remove("counting-down");
        return;
    }

    let countdown = 5;
    const originalHTML = button.innerHTML;
    button.disabled = true;
    button.innerHTML = `<i class="fa-solid fa-hourglass-start"></i> Wait ${countdown}s`;

    const timer = setInterval(() => {
        countdown--;
        button.innerHTML = `<i class="fa-solid fa-hourglass-half"></i> Wait ${countdown}s`;

        if (countdown === 0) {
            clearInterval(timer);
            button.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Preparing...`;

            console.log(`Download starting: ${link}`);

            setTimeout(() => {
                window.location.href = link;
                button.innerHTML = originalHTML;
                button.disabled = false;
                button.classList.remove("counting-down");
            }, 1000);
        }
    }, 1000);
}

// Attach click handler to all download buttons
document.querySelectorAll(".download-btn").forEach(button => {
    button.addEventListener("click", () => handleDownload(button));
});

// Detect user's OS and mark the recommended button
function markRecommendedButton() {
    const platform = navigator.platform.toLowerCase();
    const userAgent = navigator.userAgent.toLowerCase();

    let os = "unknown";

    if (platform.includes("win")) {
        os = "windows";
    } else if (platform.includes("linux") || userAgent.includes("linux")) {
        if (userAgent.includes("ubuntu") || userAgent.includes("debian")) {
            os = "debian";
        } else {
            os = "linux";
        }
    }

    document.querySelectorAll(".download-btn").forEach(button => {
        const link = button.getAttribute("data-link");
        if (!link) return;

        if (
            (os === "windows" && link.endsWith(".exe")) ||
            (os === "linux" && link.endsWith(".deb")) ||
            (os === "debian" && link.endsWith(".deb"))
        ) {
            const recommendedBadge = `<span style="margin-left: 8px; background: #00ff9d; color: #000; padding: 3px 6px; border-radius: 5px; font-size: 0.75rem;">Recommended</span>`;
            button.innerHTML += recommendedBadge;
        }
    });
}

// Run on page load
markRecommendedButton();
