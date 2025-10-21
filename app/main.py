from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        com_clss = car.comfort_class
        clean_power = self.clean_power
        cl_mk = car.clean_mark
        av_rat = self.average_rating
        dis_fc = self.distance_from_city_center
        cost = com_clss * (clean_power - cl_mk) * av_rat / dis_fc
        return cost

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate: float) -> None:
        av_rat = self.average_rating
        cnt_o_rat = self.count_of_ratings
        new_average = (av_rat * cnt_o_rat + rate) / (cnt_o_rat + 1)
        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1
