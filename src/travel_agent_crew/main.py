from travel_agent_crew.crew import travel_agent_crew


def run():
    print("\n==============================")
    print("      AI Trip Planner")
    print("==============================\n")

    while True:
        try:
            budget = int(input("Enter your travel budget (₹): "))

            if budget <= 0:
                print("Please enter a valid budget.\n")
                continue

            break

        except ValueError:
            print("Please enter a numeric value.\n")

    inputs = {
        "budget": budget
    }

    print("\nPlanning your trip...\n")

    result = travel_agent_crew().crew().kickoff(inputs=inputs)

    print("\n==============================")
    print("     Trip Planning Complete")
    print("==============================\n")

    print(result)
    print("\nA detailed itinerary has been saved as 'itinerary.md'.")


if __name__ == "__main__":
    run()