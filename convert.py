import time
import os

convert_file_path = "convert-service.txt"

while True:
    time.sleep(5)
    # Check if the file exists
    if os.path.isfile(convert_file_path):
        with open(convert_file_path, "r+") as convert_file:
            # Read the conversion result from the file
            conversion_result = convert_file.read().strip()    
            # If there's a conversion result
            if conversion_result:
                # Format the conversion result nicely
                formatted_result = f"Conversion Result: {conversion_result}\n"
                
                # Move the file pointer to the beginning of the file
                convert_file.seek(0)
                
                # Truncate the file to remove any existing content
                convert_file.truncate(0)
                
                # Write the formatted result back to the file
                convert_file.write(formatted_result)
            
            # Close the file
            convert_file.close()
