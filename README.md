# Cloud Cost Migration Engine (AWS → GCP)

A deterministic cloud cost analysis system that maps AWS services to equivalent GCP services and pricing models.

## Problem
Cloud migration decisions are complex due to differences in pricing models, SKUs, and service structures across providers.

## Solution
This system analyzes AWS billing data and maps it to GCP services to estimate equivalent costs.

## Features
- AWS billing JSON parsing
- Service mapping (AWS → GCP)
- SKU and pricing alignment
- Region normalization
- Cost comparison engine

## Architecture
- Backend: Python / Go
- Data Processing: BigQuery / MongoDB
- APIs: REST-based services

## Example

Input: AWS EC2 usage  
Output: Equivalent GCP Compute Engine cost  

## Future Scope
- Multi-cloud support (Azure)
- UI dashboard
- SaaS platform

## Author
Manikanta N
