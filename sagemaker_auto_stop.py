import boto3 

def get_notebook_name():
    log_path = '/opt/ml/metadata/resource-metadata.json'
    with open(log_path, 'r') as logs:
        _logs = json.load(logs)
    return _logs['ResourceName']

client=boto3.client('sagemaker')
client.stop_notebook_instance(
        NotebookInstanceName=get_notebook_name()
    )
print("test-completed")