def map_aws_to_gcp(service):
    mapping = {
        "Amazon EC2": "Compute Engine",
        "Amazon S3": "Cloud Storage"
    }
    return mapping.get(service, "Unknown")

print(map_aws_to_gcp("Amazon EC2"))
