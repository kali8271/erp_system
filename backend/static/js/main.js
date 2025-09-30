// Simple example: auto-hide messages after 5 seconds
document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll("[data-auto-hide]");
  alerts.forEach((el) => {
    setTimeout(() => {
      el.style.display = "none";
    }, 5000);
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("signupModal");
  const btn = document.getElementById("signupBtn");
  const closeBtn = document.getElementById("closeModal");

  if (btn && modal && closeBtn) {
    btn.addEventListener("click", () => modal.classList.remove("hidden"));
    closeBtn.addEventListener("click", () => modal.classList.add("hidden"));
  }
});