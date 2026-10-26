# Classic Car Restoration Tracker

A full-featured web application built with **Django** for tracking vintage vehicle restoration projects, managing specialized restoration parts inventory, and monitoring estimated restoration budgets.

Developed as an individual project for the **Django Basics** course at **SoftUni**.

---

## Features

- **Classic Cars Catalog:** Complete CRUD functionality for managing classic cars (manufactured in 1990 or earlier).
- **Parts Inventory:** Manage specialized replacement parts with pricing, part numbers, and unique constraints.
- **Brand / Manufacturer Catalog:** Track car manufacturers, their founding year, and origin country.
- **Many-to-Many Part Assignment:** Assign multiple restoration parts to any car to calculate the total restoration budget.
- **Search, Filter & Sort:** Filter cars by manufacturer, search by model or VIN using Django `Q` objects, and sort chronologically or alphabetically.
- **Restoration Budget Calculation:** Real-time calculation of overall restoration investment using custom model methods and template filters.
- **Custom Template Tags & Filters:** Custom currency formatter (`|currency`), VIN masker (`|mask_vin`), budget aggregator (`|total_parts_cost`), and restoration status badge tag (`{% restoration_status_badge %}`).
- **Reusable Component Architecture:** Modular partial templates (`_car_card.html`, `_part_card.html`) with template inheritance.
- **Data Validation & Protection:** Model-level and form-level validations with custom error messages, disabled VIN editing on update, and deletion confirmation dialogs.
- **Custom 404 Error Page:** Branded, user-friendly 404 page with navigation fallback.

---

## Database Architecture

The application is structured into **three (3) distinct Django apps**:

1. **`brands` (`Manufacturer`):**
   - Stores car brands (`name`, `country`, `established_year`).
   - One-to-Many relationship with `ClassicCar`.
2. **`parts` (`RestorationPart`):**
   - Inventory of restoration components (`name`, `part_number`, `price`).
   - Many-to-Many relationship with `ClassicCar`.
3. **`vehicles` (`ClassicCar`):**
   - Represents the vintage automobile project (`model_name`, `manufacture_year`, `vin`).
   - ForeignKey to `Manufacturer` (CASCADE).
   - ManyToManyField to `RestorationPart` (`blank=True`).

---

## Technology Stack

- **Backend:** Python 3.14 / Django 6.1.2
- **Database:** SQLite (default configuration, zero external DB dependencies)
- **Frontend:** Django Template Engine, Bootstrap 5 (CDN)

---

## Getting Started

### 1. Prerequisites
- Python 3.10+ installed on your system.

### 2. Clone and Setup
```bash
# Clone the repository
git clone <your-repository-url>
cd classic-car-tracker

# Create and activate a virtual environment
python -m venv .venv

# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# On macOS / Linux:
source .venv/bin/activate

# Install required dependencies
pip install -r requirements.txt