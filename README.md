# microservice

1. The request data will be in a specific text file that the microservice monitors.
   A text file or a request in the format of "Quantity, From Unit, To Unit" must be inputted.
   Ensure that the microservice is actively monitoring the designated file for new requests.
   For example, if you want to request a unit conversion, you would write the conversion
   request data (such as quantity, from unit, to unit) into a predefined text file that the
   microservice reads.

   A sample request: 100, Pound, Gram
   Output: Converted: 100 Pound to 45359.2 Gram

2. After sending the request, periodically check another designated text file where the microservice writes the response.
   Parse the content of the response file to extract the data returned by the microservice.
   Once the file is updated by the microservice, read the content of the file to retrieve the conversion result.

<img width="655" alt="Screen Shot 2024-02-26 at 10 59 05 PM" src="https://github.com/patelta01/microservice/assets/157430405/2c8373a3-c647-4693-be13-800c5e1b5883">

   
