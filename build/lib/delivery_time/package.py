class Package:
    def __init__(self, package_id, weight, distance, offer_code, base_cost):
        self.package_id = package_id
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code
        self.base_cost = base_cost
        self.total_discount = 0
        self.total_cost = 0
        self.final_total_cost = 0
        self.estimate_delivery_time = 0
        self.final_delivery_time = 0

        self.get_cost()

    def get_cost(self):
        if self.offer_code == "NA":
            discount = 0
        else:
            if self.offer_code == "OFR001" and self.distance < 200 and 70 <= self.weight <= 200:
                discount = 0.1
            elif self.offer_code == "OFR002" and 50 <= self.distance <= 150 and 100 <= self.weight <= 250:
                discount = 0.07
            elif self.offer_code == "OFR003" and 50 <= self.distance <= 250 and 10 <= self.weight <= 150:
                discount = 0.05
            else:
                discount = 0  # Offer code does not match criteria

        self.total_cost = self.base_cost + (self.distance * 5) + (self.weight * 10)
        self.total_discount = round(self.total_cost * discount, 2)
        self.final_total_cost = self.total_cost - self.total_discount
