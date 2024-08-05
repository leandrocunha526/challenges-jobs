<?php
class WeatherData
{
    private $apiKey;
    private $apiUrl;

    public function __construct($apiKey)
    {
        $this->apiKey = $apiKey;
        $this->apiUrl = 'https://api.openweathermap.org/data/2.5/group';
    }

    public function fetchWeatherData($cityIds)
    {
        $url = $this->apiUrl . '?id=' . implode(',', $cityIds) . '&units=metric&appid=' . $this->apiKey;
        $response = file_get_contents($url);
        if ($response === FALSE) {
            throw new Exception('Unable to fetch data from API');
        }
        return json_decode($response, true);
    }

    public function getProcessedData($cityIds)
    {
        $data = $this->fetchWeatherData($cityIds);
        return $this->transformData($data);
    }

    private function transformData($data)
    {
        $result = ['name' => 'root', 'children' => []];
        foreach ($data['list'] as $city) {
            $result['children'][] = [
                'name' => $city['name'],
                'size' => $city['main']['temp']
            ];
        }
        return $result;
    }
}
