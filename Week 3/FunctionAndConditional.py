def calculate_discount(price, discount_percent):
    originalPrice = price
    discountAmount = (discount_percent / 100) * originalPrice
    if discount_percent >= 20:
        finalPrice = originalPrice - discountAmount
        return finalPrice
    else:
        return originalPrice
    
print("Price is " ,calculate_discount(100, 25))  # Example usage, replace with actual input
print("Price is " ,calculate_discount(100, 15))  # Example usage, replace with stay Actual input
