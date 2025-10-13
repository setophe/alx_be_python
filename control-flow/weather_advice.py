Weather_Input = input("What's the weather like today? (sunny/rainy/cold): ")

if Weather_Input == "sunny":
    # Recommendation for sunny weather
    print("Wear a t-shirt and sunglasses.")

elif Weather_Input == "rainy":
    # Recommendation for rainy weather
    print("Don't forget your umbrella and a raincoat.")

elif Weather_Input == "cold":
    # Recommendation for cold weather
    print("Make sure to wear a warm coat and a scarf.")

else:
    # Handle unexpected or invalid input
    print("Sorry, I don't have recommendations for this weather.")
