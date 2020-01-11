def get_memory_mapped_rows(file_path):
    lines = []
    with open(file_path , "rb") as fobj:
        file_content = fobj.read()
        no_lines = len(file_content)//16
        for i in range(0, len(file_content) , 16):
            row_content_bytes = file_content[i:(i+16)]
            line = []
            for i in range(0,16,2):
                line.append(hex(int.from_bytes(row_content_bytes[i:i+2] , 'big')))
            lines.append(line)
    return lines




        