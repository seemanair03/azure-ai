from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential


# set `<your-endpoint>` and `<your-key>` variables with the values from the Azure portal
endpoint = "https://sn-instance.cognitiveservices.azure.com/"
key = "#####" #add key

docUrl = "https://seemanair03.files.wordpress.com/2023/12/receipt_azure_ai_analyzer.jpeg"

# create your `DocumentAnalysisClient` instance and `AzureKeyCredential` variable
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, 
    credential=AzureKeyCredential(key))

poller = document_analysis_client.begin_analyze_document_from_url(
    "prebuilt-document", docUrl)
result = poller.result()