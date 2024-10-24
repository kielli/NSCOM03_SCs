def calculate_parity(data: str, parity_type: str = 'even') -> str:
    ones_count = data.count('1')
    
    if parity_type == 'even':
        parity_bit = '0' if ones_count % 2 == 0 else '1'
    elif parity_type == 'odd':
        parity_bit = '1' if ones_count % 2 == 0 else '0'
    else:
        raise ValueError("parity_type must be 'even' or 'odd'")
    
    return data + parity_bit

def check_parity(data_with_parity: str, parity_type: str = 'even') -> bool:
    data = data_with_parity[:-1]
    parity_bit = data_with_parity[-1]
    expected_parity = calculate_parity(data, parity_type)[-1]

    return parity_bit == expected_parity

data = input("Enter the binary data: ")
parity_type = input("Enter the parity type (even/odd): ")

data_with_parity = calculate_parity(data, parity_type)
print(f"Data with parity bit: {data_with_parity}")

