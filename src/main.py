def main():
    while True:
        print("Welcome to Todo List App")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("Login functionality not implemented yet.Please check back soon.")
        elif choice == "2":
            print("Sign Up functionality not implemented yet. Please check back soon.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
