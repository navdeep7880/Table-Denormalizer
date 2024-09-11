OCR-Based Table Extraction and Conversion from normalised to denormalised form : 

Overview :
This project provides a solution for extracting tables from images or PDFs using Optical Character Recognition (OCR), 
converting the extracted data into a structured JSON format, and subsequently transforming it into a denormalized table that is saved as a CSV file.
The project focuses on handling complex table structures, detecting sub-tables, and ensuring accurate data representation.

Features : 
OCR Extraction: Extracts text data from images and PDFs using advanced OCR technology.
JSON Conversion: Converts OCR results into a structured JSON format for easy manipulation.
Table Denormalization: Processes JSON data to normalize tables and convert them into a denormalized format.
Sub-Table Detection: Identifies and separates sub-tables within a larger table based on specific row patterns.
CSV Export: Saves the final denormalized tables as CSV files for compatibility with various data processing tools.

Installation : 
To use this project, you need to have Python installed along with the necessary libraries. You can set up your environment using the following steps:

Clone the Repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Create a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Required Packages:
pip install -r requirements.txt

The requirements.txt file should include:
pandas
numpy

Usage : 
Prepare Your Data: Ensure you have your images or PDFs ready for OCR extraction. Place them in the appropriate directory.

Run the Script: Execute the main Python script to perform table extraction and conversion. Update the script as needed to point to your data sources.
python process_tables.py
Output: The processed tables will be saved as CSV files in the specified directory, with filenames indicating their respective table numbers.

Code Explanation :
Main Functions
cells_to_csv(cells):

Processes the list of cells extracted by OCR and performs the following:

Constructs a DataFrame from the cell data.
Detects and separates sub-tables based on row patterns (rows with identical values).
Saves each detected sub-table as a CSV file.

save_table_to_csv(s_table_no, table):

Saves the content of a table as a CSV file. The file is named based on the table number and sub-table number.

Sub-Table Detection Logic
Row Iteration:
The code iterates over each row in the DataFrame. Each row is checked for specific patterns that might indicate the end of a sub-table.

for row in df.itertuples(index=False):
Separator Row Detection:

A row where all values are identical is considered a separator row that demarcates the end of one sub-table and the start of another.

if len(set(row)) == 1:
Handling New Sub-Tables:

When a separator row is detected:

The current sub-table is finalized and added to the list of tables.
A new sub-table is started with the separator row included as the first row.
if current_table and not (len(current_table) == 1 and current_table[0] == flattened_header):
    tables.append(current_table)
Appending the Last Sub-Table:

After processing all rows, any remaining sub-table is appended to the list of tables.

if current_table:
    tables.append(current_table)
    
Example : 
Here's an example of how to use the cells_to_csv() function:

python
Copy code
cells = [
    {"bbox": [12.63, 32.39, 66.16, 44.41], "column_nums": [0], "row_nums": [0], "column header": False, "subcell": False, "projected row header": False, "cell text": "", "spans": []},
    {"bbox": [12.63, 37.95, 66.16, 48.68], "column_nums": [0], "row_nums": [1], "column header": False, "subcell": False, "projected row header": False, "cell text": "Accelerated filer", "spans": [{"bbox": [12.63, 39.33, 50.83, 48.19], "text": "Accelerated", "block_num": 1, "line_num": 0}, {"bbox": [52.83, 39.33, 66.16, 48.19], "text": "filer", "block_num": 1, "line_num": 0}]},
    # More cell data here
]

cells_to_csv(cells)


Future Improvements : 
Enhanced OCR Accuracy: Integrate advanced OCR models to improve text extraction from complex or low-quality images.
Complex Table Structures: Improve handling for more intricate table formats, including merged cells and multi-row headers.
Automated Error Detection: Implement automated checks for data consistency and integrity.
Real-Time Processing: Optimize the pipeline for faster processing, especially for large datasets or real-time applications.
Contributing
Contributions are welcome! If you find bugs or have suggestions for improvements, please open an issue or submit a pull request. Ensure that you follow the contribution guidelines and include tests for new features or fixes.


Acknowledgements
OCR Tools: Thanks to the providers of OCR technologies that facilitate text extraction.
Libraries: Appreciation to the developers of pandas and numpy for their powerful data processing libraries.





