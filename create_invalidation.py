import boto3
import time
 
# Create CloudFront client
cf = boto3.client('cloudfront')
 
# Enter Original name
 
DISTRIBUTION_ID = "ED8JFB08XUH05"
 
# Create CloudFront invalidation
def create_invalidation():
    res = cf.create_invalidation(
        DistributionId=DISTRIBUTION_ID,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*'
                ]
            },
            'CallerReference': str(time.time()).replace(".", "")
        }
    )
    invalidation_id = res['Invalidation']['Id']
    return invalidation_id
 
# Create CloudFront Invalidation
id = create_invalidation()
print("Invalidation created successfully with Id: " + id)