markdown
# Comprehensive Insights Platform for Freelancer Business Activities

This repository contains the implementation of a Comprehensive Insights Platform for Freelancer Business Activities in Abu Dhabi. The platform provides a centralized resource for accessing and analyzing data on various freelance business activities in the region.

## Features

- Centralized repository for freelancer business activities data.
- User-friendly search and filter functionalities.
- Dynamic insights and data visualizations.
- Multilingual support (English and Arabic).
- Regular data updates and notifications.
- Mobile-friendly interface.
- Community engagement features.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Pandas
- An Excel file containing the Freelancer Business Activities Dataset (`DL06-Freelance-Activities-ADRA-OD-010-AFR.xlsx`).

### Installation

1. Clone this repository:
   bash
   git clone https://github.com/your-repo/freelancer-insights-platform.git
   cd freelancer-insights-platform
   

2. Install dependencies:
   bash
   pip install -r requirements.txt
   

3. Place the dataset (`DL06-Freelance-Activities-ADRA-OD-010-AFR.xlsx`) in the root directory of the project.

### Running the Application

1. Start the Flask server:
   bash
   python app.py
   

2. Access the platform in your web browser at:
   
   http://127.0.0.1:5000/
   

### API Endpoints

#### Fetch All Activities

**Endpoint:** `/api/activities`

**Method:** `GET`

**Response:** Returns a JSON array containing all freelancer business activities.

#### Search Activities

**Endpoint:** `/api/search`

**Method:** `GET`

**Query Parameters:**

- `q` (string, required): The search keyword or category.

**Response:** Returns a JSON array of activities matching the query.

### Contributing

We welcome contributions to enhance the platform. Please fork the repository and submit a pull request with your proposed changes.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.
