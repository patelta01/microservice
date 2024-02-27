# ui.py

import time

while True:
    time.sleep(1)
    print("Enter '1' to perform unit conversion or '2' to exit.")
    user_input = input("Enter your choice: ")

    if user_input == '1':
        # Execute conversion logic by signaling prog.py
        with open("converted.txt", "w") as convert_file:
            convert_file.write("run")
            convert_file.flush()
            print("Conversion request sent.")
            time.sleep(5)  # Simulate processing time
        with open("converted.txt", "r") as prng_file:
            conversion_result = prng_file.read()
            time.sleep(2)
            prng_file.close()
        with open("convert-service.txt", "w") as conversion_file:
            conversion_file.write(conversion_result)
            conversion_file.flush()
            conversion_file.close() 
        with open("convert-service.txt", "r") as conversion_file:
            conversion_result = conversion_file.read()
            conversion_file.close()

    elif user_input == '2':
        print("Exiting the program.")
        break

    else:
        print("Unknown option.")
