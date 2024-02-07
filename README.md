# Accident Timestamp Extraction

Accident Timestamp Extraction is a Flask web application designed to automate the process of accident detection in surveillance footage and extract precise timestamps corresponding to the moment of occurrence. This project aims to facilitate insurance claims processing by eliminating the need for manual review of entire video footage, providing a more efficient and accurate solution.

## Features

- **Real-Time Accident Detection**: Utilizes deep learning techniques to classify images from surveillance cameras in real-time, accurately identifying accident occurrences.

- **Timestamp Extraction**: Automatically extracts timestamps of accident occurrences, providing precise temporal information crucial for insurance claims processing.

- **Flask Web Application**: User-friendly web interface allows users to upload surveillance footage and initiate real-time analysis with ease.

- **Efficient Claims Processing**: Accelerates insurance claims processing by automating accident detection and timestamp extraction, reducing manual effort and enhancing efficiency.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/accident-timestamp-extraction.git

pip install -r requirements.txt

2. **Download the model file:** https://drive.google.com/file/d/1QYnGJ3A_0Ee8hloNHLTd8dWEqeyJdxWz/view?usp=drive_link 

3. Save model.h5 to **artifacts/**

4. **Run the command**:
```bash
python app.py
```
Access the web application at http://localhost:5000 and follow the instructions to upload surveillance footage and extract accident timestamps.




Feel free to customize the content as needed and replace placeholders (e.g., `your_username`, `accident-timestamp-extraction`) with appropriate values.
