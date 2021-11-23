import os
import time

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = '6e888ca1f52143f89c831e1e6b53c22c'
endpoint = 'https://karmapsyy.cognitiveservices.azure.com/'



def ocr_function(filename):
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    print("===== Read File - remote =====")
    # Get an image with text

    # Call API with URL and raw response (allows you to get the operation location)
    images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static/uploads")

    read_image_path = os.path.join(images_folder, filename)
    read_image = open(read_image_path, "rb")

    read_response = computervision_client.read_in_stream(read_image,  raw=True)

    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]
    
    message = ""
    
    message_wrong = "Nie kupuj tej karmy, nie jest ona dobra dla piesków! "
    
    message_good = " Ta karma jest odpowiednia, dobry wybór!"
    
    keyword_list = ['pochodzenia drobiowego', 'zboż', 'pszenica', 'jęczmień', 'żyto', 'owies','pochodzenia zwierzęcego', 'odzwierzęce', 'pochodzenia roślinnego', 'pochodzenia wieprzowego']

    # Call the "GET" API and wait for it to retrieve the results
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print the detected text, line by line
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                if any(word in line.text.lower() for word in keyword_list):
                    message = message_wrong
                    is_good = False
                    break
                message = message_good
                is_good = True
                #print(line.text)
             
    return message, is_good


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
