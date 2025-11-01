// Detect user's browser timezone
function detectTimezone() {
  try {
    return Intl.DateTimeFormat().resolvedOptions().timeZone;
  } catch (e) {
    return "Asia/Jerusalem";
  }
}

// Fetch current time from server
async function updateClock() {
  const select = document.getElementById("timezone-select");
  const tz = select.value || detectTimezone();

  try {
    const response = await fetch(`/api/time?tz=${encodeURIComponent(tz)}`);
    if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
    const data = await response.json();

    document.getElementById("clock").textContent = data.formatted;
    select.value = data.timezone;
  } catch (error) {

    document.getElementById("clock").textContent = "⚠ Server unreachable";
    console.error("Failed to fetch time:", error);
  }
}

// Initialize
window.onload = function() {
  const select = document.getElementById("timezone-select");
  const detected = detectTimezone();
  select.value = detected;
  updateClock();
  select.addEventListener("change", updateClock);
  setInterval(updateClock, 1000);
};
