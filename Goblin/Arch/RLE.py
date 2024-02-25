def compressor(input_file, output_file):
    with open(input_file, 'r') as f_in:
        input_file = f_in.read()
    compressed_file = ''
    i = 0
    while i <= len(input_file) - 1:
        counter = 1
        counted_symbol = input_file[i]
        j = i
        while j < len(input_file) - 1:
            if input_file[j] == input_file[j + 1]:
                counter += 1
                j += 1
            else:
                break
        compressed_file = compressed_file + str(counter) + counted_symbol
        i = j + 1
        with open(output_file, 'w') as f_out:
            f_out.write(compressed_file)
    return compressed_file


print(compressor('primer.txt', 'output.txt'))

