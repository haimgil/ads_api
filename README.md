# Flask app project

## Description
This project allows manage ads and impressions requests as well as getting statistics according to user/sdkVersion.

## Language and technologies
* Project written in python with flask which is a micro-web framework that allows developing Restfull API.
* Using Redis as a key-value store for managing ads/impressions per user/sdkVersion.

## Design
App designed to have independent controller for each exposed endpoint. Every controller using its dedicated service which perform the app internal logic. Moreover, there is a gateway service which as exit point to external service.  
The app using Redis as one of its data structures is key-value store which meet the requirement of holding a counter of ads/impressions per user/sdkVersion and able to provide high availability when needed.

## APIs
This app exposing 3 endpoints as detailed below:
* **GetAd** - POST request that accept json body as shown below and return as response an XML in a VAST ad format that getting from external api. In addition, updating how many ad requests per user/sdkVersion.
    > curl --location --request POST 'localhost:5000/api/getAd' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'
    ```json
     {
        "sdkVersion": 2.0,
        "sessionId": 213455,
        "platform": "platform_A",
        "username": "Amit",
        "countryCode": 123
    }
    ```
* **Impression** - POST request that accept json body as shown below and updating how many impressions requests per user/sdkVersion.
    > curl --location --request POST 'localhost:5000/api/impression' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'
    ```json
     {
        "sdkVersion": 2.7,
        "sessionId": 213455,
        "platform": "platform_B",
        "username": "Haim",
        "countryCode": 123
    }
    ```
* **GetStats** - GET request that provides statistics according to user/sdkVersion (filterType).
    > curl --location --request GET 'localhost:5000/api/getStats?filterType=user' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'
