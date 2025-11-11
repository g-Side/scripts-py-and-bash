import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:Environment', 'Values': ['Sandbox']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    if instance_ids:
        ec2_client.stop_instances(InstanceIds=instance_ids)
        print(f" As seguintes instâncias foram desligadas: {instance_ids}")
    else:
        print("Nenhuma instância de Sandbox rodando encontrada para desligar.")
        
    return {
        'statusCode': 200,
        'body': 'Processo de desligar instâncias concluído.'
    }