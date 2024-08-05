import os
import json
import csv
import logging
from tqdm import tqdm

# Setup logging configuration
logging.basicConfig(
    filename='json_to_csv.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

def extract_red_model_from_json(json_data):
    red_models = []
    try:
        products = json_data["alibaba_icbu_product_list_response"]["products"]["alibaba_product_brief_response"]
        for product in products:
            if "red_model" in product:
                red_models.append(product["red_model"])
    except KeyError as e:
        logging.error(f"Key error: {e}")
    return red_models

def main():
    root_dir = os.getcwd()  # Get the current working directory
    json_files = [file for file in os.listdir(root_dir) if file.endswith('.json')]
    all_red_models = []

    logging.info(f"Found {len(json_files)} JSON files.")

    for json_file in tqdm(json_files, desc="Processing JSON files"):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                red_models = extract_red_model_from_json(data)
                all_red_models.extend(red_models)
                logging.info(f"Processed file {json_file}: extracted {len(red_models)} red_model entries.")
        except Exception as e:
            logging.error(f"Failed to process file {json_file}: {e}")

    csv_file = 'red_models.csv'
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['red_model'])
            for model in all_red_models:
                csvwriter.writerow([model])
        logging.info(f"Extracted red_model data has been written to {csv_file}")
    except Exception as e:
        logging.error(f"Failed to write CSV file {csv_file}: {e}")

if __name__ == '__main__':
    main()
