<p><a target="_blank" href="https://app.eraser.io/workspace/EI92SBlA9m64DqxsJurC" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# [﻿🔄 Alibaba JSON to CSV Product Number Extractor](https://github.com/ronknight/alibaba-json2csv-product-number-extractor) 
#### 🔄 This Python script extracts product numbers (specifically the red_model field) from Alibaba ProductList JSON Response files and compiles them into a single CSV file.
 [﻿Requirements](#-requirements) • [﻿Usage](#-usage) • [﻿Script](#-script) • [﻿Disclaimer](#-disclaimer) • [﻿Diagrams](#-diagrams) • 

---

## 📋 Requirements
- Python 3.x
- JSON module (built-in with Python)
- CSV module (built-in with Python)
- tqdm library (`pip install tqdm` )
## 🚀 Usage
1. Clone the repository:git clone https://github.com/ronknight/alibaba-json2csv-product-number-extractor.git
2. Navigate to the project directory:cd alibaba-json2csv-product-number-extractor
3. Place your Alibaba JSON files in the same directory as the script.
4. Run the script:python json_2_csv.py
5. The script will process all JSON files in the directory and create a CSV file named `red_models.csv`  with the extracted product numbers.
## 🔍 Script
The main script `json_2_csv.py` performs the following tasks:

1. Sets up logging to track the script's execution.
2. Reads all JSON files in the current directory.
3. Extracts the `red_model`  values from each JSON file.
4. Writes the extracted `red_model`  values to a CSV file named `red_models.csv` .
5. Provides a progress bar using tqdm to show the processing status.
Key features:

- Error handling and logging for each file processed.
- Uses tqdm for a visual progress indicator.
- Processes multiple JSON files in a single run.
## ⚠️ Disclaimer
This script is for educational and personal use only. Please ensure you have the necessary permissions to extract and use the data from Alibaba JSON files. The author is not responsible for any misuse or violation of terms of service.

## 📊 Diagrams



<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Alibaba JSON to CSV Product Number Extractor-1.eraserdiagram" data-element-id="Ckq53B3oZkfWfDF8m5LGd"><img src="/.eraser/EI92SBlA9m64DqxsJurC___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----580de6f43c8a2da6fd5e421dad314ce5-Alibaba-JSON-to-CSV-Product-Number-Extractor.png" alt="" data-element-id="Ckq53B3oZkfWfDF8m5LGd" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/EI92SBlA9m64DqxsJurC --->