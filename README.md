# Cloud Cost Migration Engine (AWS → GCP)

A deterministic cloud cost analysis system that maps AWS services to equivalent GCP services and pricing models.

---

## 🚀 Overview
This project helps organizations estimate cloud migration cost from AWS to GCP by analyzing billing data and mapping services, regions, and pricing models.

It is designed to solve real-world cloud migration challenges by providing **accurate, structured, and scalable cost comparisons**.

---

## 🧩 Problem Statement
Cloud providers use different:
- Service naming conventions
- Pricing models (on-demand, reserved, committed use)
- Regions and SKUs

This makes:
- Cost comparison difficult  
- Migration planning complex  
- Optimization decisions unreliable  

---

## 💡 Solution
This system:
- Parses AWS billing data (JSON / invoices)
- Maps AWS services → GCP equivalents
- Normalizes regions and usage units
- Applies deterministic mapping logic
- Estimates equivalent GCP cost

---

## ⚙️ Features
- AWS billing JSON parsing  
- Service mapping engine (AWS → GCP)  
- Region normalization  
- SKU-level mapping (extensible for real pricing catalogs)  
- Cost estimation engine  
- Modular architecture for scalability  

---

## 🏗️ Architecture

AWS Billing Data (JSON)
              ↓
      Data Ingestion Layer
              ↓
      Mapping Engine
  (Service / Region / SKU)
              ↓
    Normalization Layer
              ↓
     Cost Calculation
              ↓
 GCP Equivalent Output (JSON)

---

## 🧠 Mapping Logic

### Service Mapping
| AWS Service | GCP Equivalent |
|------------|----------------|
| Amazon EC2 | Compute Engine |
| Amazon S3  | Cloud Storage  |

### Region Mapping
| AWS Region   | GCP Region     |
|--------------|---------------|
| ap-south-1   | asia-south1   |

### Instance Mapping
| AWS Instance | GCP Machine |
|-------------|------------|
| t3.medium   | e2-medium  |

---

## 📊 Example

### Input (AWS)
```json
{
  "service": "Amazon EC2",
  "region": "ap-south-1",
  "instance_type": "t3.medium",
  "usage_hours": 100,
  "cost": 10
}

### Output (GCP)

{
  "service": "Compute Engine",
  "machine_type": "e2-medium",
  "region": "asia-south1",
  "estimated_cost": 9.5
}

### How to Run

cd src
python mapping_engine.py

### Project Structure
cloud-cost-migration-engine/
│
├── src/
│   └── mapping_engine.py
│
├── sample-data/
│   ├── aws_bill.json
│   └── gcp_output.json
│
├── docs/
│   ├── architecture.md
│   ├── mapping-logic.md
│   └── system-design.md
│
└── README.md
