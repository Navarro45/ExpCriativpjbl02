 // Fetch sensor data from Flask server
fetch('/sensor_data')
.then(response => response.json())
.then(data => {
    document.getElementById('temperature').innerHTML = data.temperature + '&deg;C';
    document.getElementById('humidity').innerHTML = data.humidity + '%';
})
.catch(error => console.error('Error:', error));