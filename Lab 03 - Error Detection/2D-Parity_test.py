def generate_2d_parity(data):
    rows = len(data)
    cols = len(data[0])

    for i in range(rows):
        row_data = data[i]
        count_ones = row_data.count('1')
        parity_bit = '0' if count_ones % 2 == 0 else '1'
        data[i] += parity_bit  

    col_parity = ''
    for j in range(cols):
        count_ones = sum(data[i][j] == '1' for i in range(rows))
        col_parity += '0' if count_ones % 2 == 0 else '1'

    bottom_right_parity = '0' if col_parity.count('1') % 2 == 0 else '1'
    col_parity += bottom_right_parity  

    data.append(col_parity)

    return data

def get_user_input():
    data = []
    for i in range(4):
        while True:
            byte = input(f"Enter byte {i+1} (8 bits): ")
            if len(byte) == 8 and all(bit in '01' for bit in byte):
                data.append(byte)
                break
            else:
                print("Invalid input! Please enter exactly 8 bits (0 or 1).")
    return data

user_data = get_user_input()

parity_data = generate_2d_parity([row[:] for row in user_data]) 
print("\n2D Parity Grid with row and column parity bits:")
for row in parity_data:
    print(row)
