<?php
header('Content-Type: application/json');

require 'WeatherData.php';

$apiKey = 'YOUR API';
$cityIds = [524901, 703448, 2643743, 3469058, 1835848, 2988507];

try {
    $weatherData = new WeatherData($apiKey);
    $data = $weatherData->getProcessedData($cityIds);
    echo json_encode($data);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
