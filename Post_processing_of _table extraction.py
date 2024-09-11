import pandas as pd
import numpy as np
from collections import OrderedDict
import os

def save_table_to_csv(s_table_no, table):
    # Specify the file name
    table_no="92"
    file_name = f"output_table_{table_no}_sub_tab_{s_table_no}.csv"

    # Combine the directory path and file name
    file_path = os.path.join("C:\\Users\\VIKAS\\Downloads", file_name)

    # Write the table content to the CSV file
    with open(file_path, 'w') as file:
        file.write(table)
        
        
def cells_to_csv(cells):
    tables = []  # List to store tables

    if len(cells) > 0:
        num_columns = max([max(cell['column_nums']) for cell in cells]) + 1
        num_rows = max([max(cell['row_nums']) for cell in cells]) + 1
    else:
        return tables

    header_cells = [cell for cell in cells if cell['column header']]
    if len(header_cells) > 0:
        max_header_row = max([max(cell['row_nums']) for cell in header_cells])
    else:
        max_header_row = -1

    table_array = np.empty([num_rows, num_columns], dtype="object")
    if len(cells) > 0:
        for cell in cells:
            for row_num in cell['row_nums']:
                for column_num in cell['column_nums']:
                    table_array[row_num, column_num] = cell["cell text"]

    header = table_array[:max_header_row+1,:]
    flattened_header = []
    for col in header.transpose():
        flattened_header.append(' | '.join(OrderedDict.fromkeys(col)))
    df = pd.DataFrame(table_array[max_header_row+1:,:], index=None, columns=flattened_header)
        
    # Logic to identify sub-tables based on rows with all values equal
    current_table = []
    current_table.append(flattened_header)
    #print(flattened_header)
    for row in df.itertuples(index=False):
        if len(set(row)) == 1:  # If all values in the row are equal
            if current_table and not (len(current_table)==1 and current_table[0]==flattened_header):
                tables.append(current_table)
            current_table = []  # Empty the current table
            starting_row = [' | '.join([header_val, row_val]) for header_val, row_val in zip(flattened_header, row)]  # Combine header with row
            current_table.append(starting_row)
        else:
            current_table.append(list(row))
    
    if current_table:
        tables.append(current_table)  # Append the last table if not empty
    
    # Print each table
    for idx, table in enumerate(tables, start=1):
        table_content = '\n'.join(','.join(row) for row in table)
        save_table_to_csv(idx, table_content)
        print(f"Table {idx}:")
        for row in table:
            print(row)
        print()
        

# Example usage:
cells =[{"bbox": [19.830001831054688, 74.437255859375, 161.1614990234375, 85.9791259765625], "column_nums": [0], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "Year ended December 31, 2022", "spans": [{"bbox": [19.830001831054688, 74.437255859375, 40.03009033203125, 85.609130859375], "text": "Year", "block_num": 7, "line_num": 0}, {"bbox": [42.80000305175781, 74.437255859375, 70.60151672363281, 85.609130859375], "text": "ended", "block_num": 7, "line_num": 0}, {"bbox": [73.36998748779297, 74.437255859375, 119.49005126953125, 85.609130859375], "text": "December", "block_num": 7, "line_num": 0}, {"bbox": [122.25997924804688, 74.437255859375, 136.15829467773438, 85.609130859375], "text": "31,", "block_num": 7, "line_num": 0}, {"bbox": [138.91998291015625, 74.437255859375, 161.1614990234375, 85.609130859375], "text": "2022", "block_num": 7, "line_num": 0}]}, {"bbox": [276.3299865722656, 59.8072509765625, 281.8915100097656, 70.9791259765625], "column_nums": [1], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [276.3299865722656, 59.8072509765625, 281.8915100097656, 70.9791259765625], "text": "$", "block_num": 6, "line_num": 1}]}, {"bbox": [276.3299865722656, 74.437255859375, 281.8915100097656, 85.9791259765625], "column_nums": [1], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [276.3299865722656, 74.8072509765625, 281.8915100097656, 85.9791259765625], "text": "$", "block_num": 7, "line_num": 1}]}, {"bbox": [321.8599853515625, 59.8072509765625, 346.8714904785156, 70.9791259765625], "column_nums": [2], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "1,344", "spans": [{"bbox": [321.8599853515625, 59.8072509765625, 346.8714904785156, 70.9791259765625], "text": "1,344", "block_num": 6, "line_num": 2}]}, {"bbox": [321.8599853515625, 74.437255859375, 346.8714904785156, 85.9791259765625], "column_nums": [2], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "1,389", "spans": [{"bbox": [321.8599853515625, 74.8072509765625, 346.8714904785156, 85.9791259765625], "text": "1,389", "block_num": 7, "line_num": 2}]}, {"bbox": [357.3299865722656, 59.8072509765625, 362.8915100097656, 70.9791259765625], "column_nums": [3], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [357.3299865722656, 59.8072509765625, 362.8915100097656, 70.9791259765625], "text": "$", "block_num": 6, "line_num": 2}]}, {"bbox": [357.3299865722656, 74.437255859375, 362.8915100097656, 85.9791259765625], "column_nums": [3], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [357.3299865722656, 74.8072509765625, 362.8915100097656, 85.9791259765625], "text": "$", "block_num": 7, "line_num": 2}]}, {"bbox": [385.6099853515625, 59.8072509765625, 410.6214904785156, 70.9791259765625], "column_nums": [4], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "2,092", "spans": [{"bbox": [385.6099853515625, 59.8072509765625, 410.6214904785156, 70.9791259765625], "text": "2,092", "block_num": 6, "line_num": 3}]}, {"bbox": [385.6099853515625, 74.437255859375, 410.6214904785156, 85.9791259765625], "column_nums": [4], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "2,125", "spans": [{"bbox": [385.6099853515625, 74.8072509765625, 410.6214904785156, 85.9791259765625], "text": "2,125", "block_num": 7, "line_num": 3}]}, {"bbox": [421.0799865722656, 59.8072509765625, 426.6415100097656, 70.9791259765625], "column_nums": [5], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [421.0799865722656, 59.8072509765625, 426.6415100097656, 70.9791259765625], "text": "$", "block_num": 6, "line_num": 3}]}, {"bbox": [421.0799865722656, 74.437255859375, 426.6415100097656, 85.9791259765625], "column_nums": [5], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [421.0799865722656, 74.8072509765625, 426.6415100097656, 85.9791259765625], "text": "$", "block_num": 7, "line_num": 3}]}, {"bbox": [446.02996826171875, 59.8072509765625, 477.70001220703125, 70.9791259765625], "column_nums": [6], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "(2,047)", "spans": [{"bbox": [446.02996826171875, 59.8072509765625, 477.70001220703125, 70.9791259765625], "text": "(2,047)", "block_num": 6, "line_num": 4}]}, {"bbox": [446.02996826171875, 74.437255859375, 477.70001220703125, 85.9791259765625], "column_nums": [6], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "(2,301)", "spans": [{"bbox": [446.02996826171875, 74.8072509765625, 477.70001220703125, 85.9791259765625], "text": "(2,301)", "block_num": 7, "line_num": 4}]}, {"bbox": [484.8299865722656, 59.8072509765625, 490.3914794921875, 70.9791259765625], "column_nums": [7], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [484.8299865722656, 59.8072509765625, 490.3914794921875, 70.9791259765625], "text": "$", "block_num": 6, "line_num": 4}]}, {"bbox": [484.8299865722656, 74.437255859375, 490.3914794921875, 85.9791259765625], "column_nums": [7], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "$", "spans": [{"bbox": [484.8299865722656, 74.8072509765625, 490.3914794921875, 85.9791259765625], "text": "$", "block_num": 7, "line_num": 4}]}, {"bbox": [513.1100463867188, 59.8072509765625, 538.12158203125, 70.9791259765625], "column_nums": [8], "row_nums": [1], "column header": True, "subcell": False, "projected row header": False, "cell text": "1,389", "spans": [{"bbox": [513.1100463867188, 59.8072509765625, 538.12158203125, 70.9791259765625], "text": "1,389", "block_num": 6, "line_num": 5}]}, {"bbox": [513.1100463867188, 74.437255859375, 538.12158203125, 85.9791259765625], "column_nums": [8], "row_nums": [2], "column header": False, "subcell": False, "projected row header": False, "cell text": "1,213", "spans": [{"bbox": [513.1100463867188, 74.8072509765625, 538.12158203125, 85.9791259765625], "text": "1,213", "block_num": 7, "line_num": 5}]}, {"bbox": [276.3299865722656, 39.037811279296875, 346.8714904785156, 55.975311279296875], "column_nums": [1, 2], "row_nums": [0], "column header": True, "projected row header": False, "cell text": "Balance at Beginning of Year", "spans": [{"bbox": [292.3500061035156, 39.037811279296875, 322.9992370605469, 47.975311279296875], "text": "Balance", "block_num": 3, "line_num": 0}, {"bbox": [325.2140197753906, 39.037811279296875, 332.3180847167969, 47.975311279296875], "text": "at", "block_num": 3, "line_num": 0}, {"bbox": [278.1499938964844, 47.037811279296875, 317.2207336425781, 55.975311279296875], "text": "Beginning", "block_num": 4, "line_num": 0}, {"bbox": [319.4380187988281, 47.037811279296875, 326.9820861816406, 55.975311279296875], "text": "of", "block_num": 4, "line_num": 0}, {"bbox": [329.2060241699219, 47.037811279296875, 346.5353088378906, 55.975311279296875], "text": "Year", "block_num": 4, "line_num": 0}]}, {"bbox": [484.8299865722656, 39.037811279296875, 538.12158203125, 55.975311279296875], "column_nums": [8, 7], "row_nums": [0], "column header": True, "projected row header": False, "cell text": "Balance at End of Year", "spans": [{"bbox": [492.219970703125, 39.037811279296875, 522.8692016601562, 47.975311279296875], "text": "Balance", "block_num": 5, "line_num": 0}, {"bbox": [525.083984375, 39.037811279296875, 532.1880493164062, 47.975311279296875], "text": "at", "block_num": 5, "line_num": 0}, {"bbox": [490.0, 47.037811279296875, 505.10272216796875, 55.975311279296875], "text": "End", "block_num": 5, "line_num": 1}, {"bbox": [507.32000732421875, 47.037811279296875, 514.8640747070312, 55.975311279296875], "text": "of", "block_num": 5, "line_num": 1}, {"bbox": [517.0880126953125, 47.037811279296875, 534.4172973632812, 55.975311279296875], "text": "Year", "block_num": 5, "line_num": 1}]}, {"bbox": [357.3299865722656, 39.037811279296875, 410.6214904785156, 55.975311279296875], "column_nums": [3, 4], "row_nums": [0], "column header": True, "projected row header": False, "cell text": "Additions", "spans": [{"bbox": [366.2799987792969, 47.037811279296875, 403.1372375488281, 55.975311279296875], "text": "Additions", "block_num": 4, "line_num": 1}]}, {"bbox": [19.830001831054688, 39.037811279296875, 161.1614990234375, 70.9791259765625], "column_nums": [0], "row_nums": [0, 1], "column header": True, "projected row header": False, "cell text": "Year ended December 31, 2021", "spans": [{"bbox": [19.830001831054688, 59.437255859375, 40.03009033203125, 70.609130859375], "text": "Year", "block_num": 6, "line_num": 0}, {"bbox": [42.80000305175781, 59.437255859375, 70.60151672363281, 70.609130859375], "text": "ended", "block_num": 6, "line_num": 0}, {"bbox": [73.36998748779297, 59.437255859375, 119.49005126953125, 70.609130859375], "text": "December", "block_num": 6, "line_num": 0}, {"bbox": [122.25997924804688, 59.437255859375, 136.15829467773438, 70.609130859375], "text": "31,", "block_num": 6, "line_num": 0}, {"bbox": [138.91998291015625, 59.437255859375, 161.1614990234375, 70.609130859375], "text": "2021", "block_num": 6, "line_num": 0}]}, {"bbox": [421.0799865722656, 39.037811279296875, 477.70001220703125, 55.975311279296875], "column_nums": [5, 6], "row_nums": [0], "column header": True, "projected row header": False, "cell text": "Usage", "spans": [{"bbox": [436.4599914550781, 47.037811279296875, 460.4452209472656, 55.975311279296875], "text": "Usage", "block_num": 4, "line_num": 2}]}]

cells_to_csv(cells)


