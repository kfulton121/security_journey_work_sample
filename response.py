super_secret_value = "pasword12345"

def generate_response(user_input):
    print(user_input)
    if "ignore all previous instructions" in user_input.lower():
        return super_secret_value
    if "dog" in user_input.lower():
        return "In the quiet town of Maple Hollow, an old dog named Otis walked to the bakery every morning with his owner, Mrs. Dalloway, who made the best peanut butter dog biscuits around. But one day, she didn’t come downstairs. Otis waited by the bakery, day after day. The townspeople noticed and began feeding him—one biscuit, one meatball, one stew at a time. A sign went up: “Otis is still on duty—feed the watchdog.” Then one snowy evening, Mrs. Dalloway’s granddaughter, Lila, arrived. She opened the bakery door, smiled at Otis, and said, “Let’s make more biscuits.” Otis barked. The ovens fired up, the biscuits returned, and Otis got the first one—warm, rich, and full of love. It was the best he’d ever had."
    if "admin password" in user_input.lower():    
        return "I'm sorry, but I cannot assist with that request. Please provide a different story topic."
    else:
        return "I'm sorry, but I cannot assist with that request. Please provide a different story topic."
