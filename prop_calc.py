class Property:
    def __init__(self, bedrooms, bathrooms, carparks, price):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.carparks = carparks
        self.price = price

    def calculate_worth(self):
        # Define weights for each feature
        weight_bedroom = 0.4
        weight_bathroom = 0.2
        weight_carpark = 0.3
        weight_price = -0.1  # Lower price is better

        # Normalize price by dividing by 1 million because the average property price is $1 million.
        # A property selling for $500,000 should have normalised price of 0.5.
        normalized_price = self.price / 1_000_000

        # Calculate worth score
        worth_score = (
                (self.bedrooms * weight_bedroom) +
                (self.bathrooms * weight_bathroom) +
                (self.carparks * weight_carpark) +
                (normalized_price * weight_price)
        )
        return worth_score

    def __repr__(self):
        return f"Property({self.bedrooms} BR, {self.bathrooms} BA, {self.carparks} CP, ${self.price})"


def input_properties():
    properties = []
    print("Enter property details (or type 'done' to finish):")

    while True:
        data = input("Enter number of bedrooms, bathrooms, carparks, price (comma-separated): ")
        if data.lower() == "done":
            break

        try:
            bedrooms, bathrooms, carparks, price = map(float, data.split(",")) # int / float?2,
            properties.append(Property(bedrooms, bathrooms, carparks, price))
        except ValueError:
            print("Invalid input. Please enter 4 numbers separated by commas (e.g., 3,2,1,450000).")

    return properties


def main():
    # Input properties
    properties = input_properties()

    # Sort properties by worth score
    properties.sort(key= lambda prop: prop.calculate_worth(), reverse=True)

    # Display sorted properties
    print("\nProperties sorted by worth:")
    for prop in properties:
        print(f"{prop} - Worth Score: {prop.calculate_worth(): .2f}")


if __name__ == "__main__":
    main()
