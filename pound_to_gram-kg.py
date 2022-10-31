def converter(pound):
    gram = 453.59237
    kilogram = 0.454
    in_gram = pound * gram
    in_kilogram = pound * kilogram
    print("The amount you entered is", pound, "pound")
    print("Gram =", in_gram)
    print("Kilogram =", in_kilogram)

pound = float(input("Enter the weight in pound:"))
converter(pound)
