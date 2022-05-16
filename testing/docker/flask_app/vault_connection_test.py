import hvac

f = open('/var/run/secrets/kubernetes.io/serviceaccount/token')
jwt = f.read()
#print("jwt:", jwt)
f.close()

client = hvac.Client(url='https://vault-cicd.safersoftware.net:8200')

res = client.auth_kubernetes("k8s-role", jwt)
res = client.is_authenticated()
print("res:", res)
hvac_secrets_data_k8s = client.read('kubernetes/test/test')
print("hvac_secrets_data_k8s:", hvac_secrets_data_k8s)