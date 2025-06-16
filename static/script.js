// Optional: This script could give a hint or set default cookies
window.onload = function () {
    // Only set cookies if they don't exist (to simulate login)
    if (!document.cookie.includes("admin")) {
        document.cookie = "admin=False; path=/";
    }

    // Optional console hint (bisa dihapus untuk versi final)
    console.log("Psst... Sometimes cookies tell the truth. Check Application tab 😉");
};
