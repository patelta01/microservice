import time

def perform_conversion(quantity, from_unit, to_unit):
    conversion_rates = {
        ('Pound', 'Gram'): 453.592,
        ('Ounce', 'Gallon'): 0.0078125,
        ('Cup', 'TSP'): 48,
        ('TBSP', 'Pound'): 0.5,
        ('Gram', 'Ounce'): 0.035274,
        ('Gallon', 'Cup'): 16,
        ('TSP', 'TBSP'): 3,
        ('Pound', 'Ounce'): 16,
        ('Ounce', 'Gram'): 28.3495,
        ('Cup', 'Pound'): 0.521,
        ('TBSP', 'TSP'): 3,
        ('TSP', 'Cup'): 0.0208333,
        ('Gram', 'TSP'): 0.24,
        ('Ounce', 'TBSP'): 2,
        ('Pound', 'Cup'): 1.917
    }

    if (from_unit, to_unit) in conversion_rates:
        conversion_rate = conversion_rates[(from_unit, to_unit)]
        converted_quantity = quantity * conversion_rate
        return f"Converted: {quantity} {from_unit} to {converted_quantity} {to_unit}\n"
    else:
        return f"Conversion from {from_unit} to {to_unit} not supported.\n"

while True:
    time.sleep(5)
    with open("converted.txt", "r+") as convert_file:
        read_data = convert_file.read().strip()
        if read_data == "run":
            convert_file.seek(0)
            convert_file.truncate()
            convert_file.flush()
            with open("ingredient.txt", "r") as ingredients_file:
                conversion_results = ""
                for line in ingredients_file:
                    quantity, from_unit, to_unit = line.strip().split(',')
                    quantity = int(quantity)
                    conversion_result = perform_conversion(quantity, from_unit.strip(), to_unit.strip())
                    conversion_results += conversion_result
                convert_file.write(conversion_results)
                ingredients_file.close()
        convert_file.close()
