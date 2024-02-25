def decompressor(output_file, decompressed_file):
    with open(output_file, 'r') as f_in:
        output_file = f_in.read()
    output_string = ''
    i = 0
    while i < len(output_file):
        if output_string[i].isdigit():
            count = int(output_string[i])
            output_string += output_string[i + 1] * count
            i += 2
        else:
            output_string += output_string[i]
            i += 1
        with open(output_file, 'w') as f_out:
            f_out.write(decompressed_file)
    return output_string


print(decompressor('output.txt', 'output1.txt'))




