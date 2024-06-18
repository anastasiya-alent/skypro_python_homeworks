class Smartphone:
    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number
    
    def brend(self):
        print(self.phone_brend)

    def model(self):
        print(self.phone_model)
        
    def subscriberNumber(self):
        print(self.subscriber_number)
    
    def fullinfo(self):
        print(self.phone_brand + ' - ' + self.phone_model + '. ' + self.subscriber_number)