let lastTemperature = 25; // Start at a known temperature

// Function to simulate fetching temperature data
function fetchTemperatureData() {
    // Generate a new temperature value that is either +5 or -5 from the last value
    const change = Math.floor(Math.random() * 2) * 10 - 5; // Randomly change it by +/- 5 or 0
    lastTemperature += change; // Update lastTemperature
    return Math.max(20, Math.min(lastTemperature, 100)); // Ensure it's between 20°C and 100°C
}

// Function to update the temperature display
function updateTemperatureDisplay() {
    const temperatureDisplay = document.getElementById("temperature-display");
    const temperatureData = fetchTemperatureData(); // Fetch new temperature
    console.log(`Generated Temperature: ${temperatureData}°C`); // Debug log
    temperatureDisplay.textContent = `Current Temperature: ${temperatureData}°C`; // Update display
}

// Add event listener to the refresh button
document.getElementById("refresh-button").addEventListener("click", () => {
    updateTemperatureDisplay(); // Update display when button is clicked
});

// Initial load of temperature data
updateTemperatureDisplay(); // Initial display
