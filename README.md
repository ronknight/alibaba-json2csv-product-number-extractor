<h1 align="center"><a href="https://github.com/ronknight/alibaba-json2csv-product-number-extractor">🔄 Alibaba JSON to CSV Product Number Extractor</a></h1>
<h4 align="center">🔄 This Python script extracts product numbers (specifically the red_model field) from Alibaba ProductList JSON Response files and compiles them into a single CSV file.</h4>
<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/alibaba-json2csv-product-number-extractor/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/alibaba-json2csv-product-number-extractor/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>
<p align="center">
  <a href="#-requirements">Requirements</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-script">Script</a> •
  <a href="#-disclaimer">Disclaimer</a> •
  <a href="#-diagrams">Diagrams</a> •
</p>

---

## 📋 Requirements

- Python 3.x
- JSON module (built-in with Python)
- CSV module (built-in with Python)
- tqdm library (`pip install tqdm`)

## 🚀 Usage

1. Clone the repository:
   ```
   git clone https://github.com/ronknight/alibaba-json2csv-product-number-extractor.git
   ```

2. Navigate to the project directory:
   ```
   cd alibaba-json2csv-product-number-extractor
   ```

3. Place your Alibaba JSON files in the same directory as the script.

4. Run the script:
   ```
   python json_2_csv.py
   ```

5. The script will process all JSON files in the directory and create a CSV file named `red_models.csv` with the extracted product numbers.

## 🔍 Script

The main script `json_2_csv.py` performs the following tasks:

1. Sets up logging to track the script's execution.
2. Reads all JSON files in the current directory.
3. Extracts the `red_model` values from each JSON file.
4. Writes the extracted `red_model` values to a CSV file named `red_models.csv`.
5. Provides a progress bar using tqdm to show the processing status.

Key features:
- Error handling and logging for each file processed.
- Uses tqdm for a visual progress indicator.
- Processes multiple JSON files in a single run.

## ⚠️ Disclaimer

This script is for educational and personal use only. Please ensure you have the necessary permissions to extract and use the data from Alibaba JSON files. The author is not responsible for any misuse or violation of terms of service.

## 📊 Diagrams

