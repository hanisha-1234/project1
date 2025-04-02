import random
import string

class UsernameGenerator:
    def __init__(self):
        # Define lists of adjectives and nouns
        self.adjectives = [
            'Cool', 'Wild', 'Happy', 'Silly', 'Crazy', 'Lucky', 'Brave', 
            'Gentle', 'Fierce', 'Swift', 'Clever', 'Mighty', 'Calm', 
            'Jolly', 'Wise', 'Bold', 'Proud', 'Quick', 'Daring', 'Nimble'
        ]
        self.nouns = [
            'Tiger', 'Dragon', 'Eagle', 'Wolf', 'Phoenix', 'Lion', 
            'Bear', 'Shark', 'Falcon', 'Panther', 'Hawk', 'Rhino', 
            'Fox', 'Owl', 'Cheetah', 'Gorilla', 'Buffalo', 'Raven', 
            'Python', 'Jaguar'
        ]
        self.special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
        
    def generate_username(self, include_numbers=True, include_special=False, num_length=3):
        """Generate a random username based on user preferences"""
        # Randomly select adjective and noun
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        
        # Combine them
        username = f"{adjective}{noun}"
        
        # Add numbers if requested
        if include_numbers:
            numbers = ''.join(random.choice(string.digits) for _ in range(num_length))
            username += numbers
        
        # Add special character if requested
        if include_special:
            special = random.choice(self.special_chars)
            username += special
        
        return username
    
    def save_to_file(self, usernames, filename='usernames.txt'):
        """Save generated usernames to a text file"""
        with open(filename, 'a') as file:  # 'a' mode appends to the file
            for username in usernames:
                file.write(username + '\n')
        print(f"\nUsernames saved to {filename}")

def main():
    print("=== Random Username Generator ===")
    print("This program will generate creative usernames for you!\n")
    
    generator = UsernameGenerator()
    
    # Get user preferences
    while True:
        try:
            num_usernames = int(input("How many usernames would you like to generate? (1-20): "))
            if 1 <= num_usernames <= 20:
                break
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Please enter a valid number.")
    
    include_numbers = input("Include numbers in the username? (y/n): ").lower() == 'y'
    
    if include_numbers:
        while True:
            try:
                num_length = int(input("How many digits? (1-5): "))
                if 1 <= num_length <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        num_length = 0
    
    include_special = input("Include a special character? (y/n): ").lower() == 'y'
    
    # Generate usernames
    usernames = []
    for _ in range(num_usernames):
        username = generator.generate_username(
            include_numbers=include_numbers,
            include_special=include_special,
            num_length=num_length
        )
        usernames.append(username)
    
    # Display results
    print("\nGenerated Usernames:")
    for i, username in enumerate(usernames, 1):
        print(f"{i}. {username}")
    
    # Save to file if user wants
    save_file = input("\nWould you like to save these usernames to a file? (y/n): ").lower() == 'y'
    if save_file:
        filename = input("Enter filename (or press Enter for 'usernames.txt'): ").strip()
        filename = filename if filename else 'usernames.txt'
        generator.save_to_file(usernames, filename)
    
    print("\nThank you for using the Random Username Generator!")

if __name__ == "__main__":
    main()
