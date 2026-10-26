# Classic Car Restoration Tracker

A web application built with **Django** designed to track vintage vehicle restoration projects, manage specialized restoration parts inventory, and monitor restoration budgets from start to finish.


---

## Key Features

- **Project Dashboard:** Live statistics showing total tracked cars, inventory parts, registered manufacturers, and aggregated restoration investment across all projects.
- **Classic Cars Catalog:** Full CRUD functionality for managing vintage vehicles (manufactured in 1990 or earlier).
- **Parts Inventory:** Full CRUD functionality for tracking replacement parts with pricing, official part numbers, and uniqueness constraints.
- **Brand / Manufacturer Catalog:** Track car manufacturers, their founding year, origin country, and count of cars associated with each brand.
- **Many-to-Many Part Assignment:** Assign multiple restoration parts to any vehicle directly from the car edit interface.
- **Search, Filter & Sort:** Filter cars by manufacturer dropdown, search by model name or VIN using Django `Q` objects, and sort chronologically or alphabetically.
- **Restoration Budget Calculation:** Real-time calculation of overall restoration investment using custom model methods, properties, and custom template filters.
- **Custom Template Tags & Filters:** Custom currency formatter (`|currency`), VIN privacy masker (`|mask_vin`), budget aggregator (`|total_parts_cost`), and dynamic restoration status badge tag (`{% restoration_status_badge %}`).
- **Reusable Component Architecture:** Modular partial templates (`_car_card.html`, `_part_card.html`) with clean template inheritance.
- **Data Validation & Protection:** Model-level and form-level validations with custom error messages, disabled VIN editing on update, and deletion confirmation dialogs.
- **Custom 404 Error Page:** Branded, user-friendly 404 error page with catalog fallback navigation.

---

## Database Architecture & Relationships

The project is structured into **three (3) distinct Django apps**:

1. **`brands` (`Manufacturer`):**
   - Fields: `name` (unique), `country`, `established_year`.
   - Validators: `MinValueValidator(1700)`.
   - Properties: `cars_count` (returns count of associated vehicles).
   - Relationship: One-to-Many with `ClassicCar`.

2. **`parts` (`RestorationPart`):**
   - Fields: `name`, `part_number` (unique), `price` (DecimalField).
   - Validators: `MinValueValidator(Decimal('0.01'))`, `MinLengthValidator(3)`.
   - Relationship: Many-to-Many with `ClassicCar`.

3. **`vehicles` (`ClassicCar`):**
   - Fields: `model_name`, `manufacture_year`, `vin` (unique, 17 characters).
   - Validators: `MinValueValidator(1886)`, `MaxValueValidator(1990)`, `RegexValidator` for standard 17-character VIN.
   - Properties: `total_parts_cost` (sum of assigned parts prices), `parts_count`.
   - Relationships:
     - `ForeignKey` to `Manufacturer` (CASCADE).
     - `ManyToManyField` to `RestorationPart` (`blank=True`).

---

## Technology Stack

- **Framework:** Python 3.14 / Django 6.1.2
- **Database:** SQLite (default configuration, zero external database setup required)
- **Frontend:** Django Template Engine, Bootstrap 5.3 (via CDN)
- **Version Control:** Git / GitHub

---

## Getting Started

### 1. Prerequisites
- Python 3.10 or higher installed on your system.

### 2. Clone the Repository
```bash
git clone <your-repository-url>
cd classic-car-tracker
```

### 3. Create & Activate a Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# Activate on macOS / Linux:
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to: **`http://127.0.0.1:8000/`**

---

## Evaluation Notes

- **Authentication:** User authentication, registration, and login functionality are excluded.
- **Zero Prepopulated Data Needed:** The application is fully functional starting from an empty database. The user can create Manufacturers, Parts, and Classic Cars entirely through the UI using available navigation links.
- **Environment Variables:** The application runs out of the box using default settings without requiring any `.env` files or secret credentials for local testing.

---

## Project Structure

```
classic-car-tracker/
├── brands/                   # Manufacturer management app
│   ├── models.py             # Manufacturer model & validators
│   ├── forms.py              # ManufacturerModelForm
│   ├── views.py              # CBVs for listing and creating brands
│   └── urls.py
├── parts/                    # Restoration parts inventory app
│   ├── models.py             # RestorationPart model & constraints
│   ├── forms.py              # PartForm
│   ├── views.py              # Full CRUD views
│   └── urls.py
├── vehicles/                 # Core vehicle tracking app
│   ├── models.py             # ClassicCar model & properties
│   ├── forms.py              # Create/Update forms with disabled fields & M2M
│   ├── views.py              # Full CRUD views, search, filter, and HomeView
│   ├── urls.py
│   └── templatetags/         # Custom filters and tags
│       ├── __init__.py
│       └── vehicle_tags.py
├── restoration_tracker/      # Project configuration and root routing
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/                # Application and global templates
│   ├── base.html             # Base layout with navbar & footer
│   ├── home.html             # Project dashboard
│   ├── 404.html              # Custom 404 error page
│   ├── brands/               # Manufacturer templates
│   ├── parts/                # Parts templates & partials/_part_card.html
│   └── vehicles/             # Vehicle templates & partials/_car_card.html
├── manage.py
├── requirements.txt          # Pinned project dependencies
├── .gitignore                # Git ignore rules for venv, cache, and db
└── README.md
```

---

## Author

Developed by **Nikola Ivanov**  

