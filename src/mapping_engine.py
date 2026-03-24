import json

SERVICE_MAPPING = {
    "Amazon EC2": "Compute Engine",
    "Amazon S3": "Cloud Storage"
}

REGION_MAPPING = {
    "ap-south-1": "asia-south1"
}

INSTANCE_MAPPING = {
    "t3.medium": "e2-medium"
}

def map_aws_to_gcp(data):
    return {
        "service": SERVICE_MAPPING.get(data["service"], "Unknown"),
        "machine_type": INSTANCE_MAPPING.get(data.get("instance_type"), "Unknown"),
        "region": REGION_MAPPING.get(data["region"], "Unknown"),
        "estimated_cost": round(data["cost"] * 0.95, 2)
    }

if __name__ == "__main__":
    with open("../sample-data/aws_bill.json") as f:
        aws_data = json.load(f)

    result = map_aws_to_gcp(aws_data)
    print(result)
