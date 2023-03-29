from .offer_codes import offer_codes_list


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

        self.offer_codes = offer_codes_list
        self.get_cost()

    def get_cost(self):
        discount = 0

        if self.offer_code in self.offer_codes:
            offer = self.offer_codes[self.offer_code]
            offer_criteria = offer['criteria']

            if all([
                self.distance >= offer_criteria['distance_min'],
                self.distance <= offer_criteria['distance_max'],
                self.weight >= offer_criteria['weight_min'],
                self.weight <= offer_criteria['weight_max']
            ]):
                discount = offer['discount']

        self.total_cost = self.base_cost + (self.distance * 5) + (self.weight * 10)
        self.total_discount = round(self.total_cost * discount, 2)
        self.final_total_cost = self.total_cost - self.total_discount
