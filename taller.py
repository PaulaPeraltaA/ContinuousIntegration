# membership_plans.py


class MembershipPlan:
    def __init__(self, name, base_cost, features):
        self.name = name
        self.base_cost = base_cost
        self.features = features




# Definición de los planes de membresía
basic_plan = MembershipPlan("Basic", 50, ["Access to gym equipment"])
premium_plan = MembershipPlan("Premium", 100, ["Access to gym equipment", "Personal training sessions"])
family_plan = MembershipPlan("Family", 150, ["Access to gym equipment", "Group classes"])




membership_plans = [basic_plan, premium_plan, family_plan]




# gym_membership.py


def display_membership_plans():
    print("Available Membership Plans:")
    for idx, plan in enumerate(membership_plans):
        print(f"{idx + 1}. {plan.name} - ${plan.base_cost}")
        print("   Features:")
        for feature in plan.features:
            print(f"   - {feature}")
        print()


def select_membership_plan():
    while True:
        try:
            choice = int(input("Select a membership plan (1, 2, 3): "))
            if 1 <= choice <= len(membership_plans):
                return membership_plans[choice - 1]
            else:
                print("Invalid choice. Please select a valid membership plan.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def select_additional_features(membership_plan):
    selected_features = []
    while True:
        print("Available Additional Features:")
        for idx, feature in enumerate(membership_plan.features):
            print(f"{idx + 1}. {feature}")
        print("0. Done selecting features.")
        
        try:
            choice = int(input("Select an additional feature to add (0, 1, 2, ...): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(membership_plan.features):
                selected_features.append(membership_plan.features[choice - 1])
            else:
                print("Invalid choice. Please select a valid additional feature.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    return selected_features


def select_group_size():
    while True:
        try:
            group_size = int(input("Enter the number of people in the group (1 or more): "))
            if group_size >= 1:
                return group_size
            else:
                print("Invalid input. Please enter a valid number (1 or more).")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_total_cost(base_cost, selected_features, group_size):
    additional_features_cost = len(selected_features) * 10  # $10 per additional feature
    total_cost = base_cost + additional_features_cost
    total_cost *= group_size  # multiply by number of people


    return total_cost


def apply_group_discount(total_cost, group_size):
    if group_size >= 2:
        total_cost *= 0.9  # apply 10% discount for group memberships
    return total_cost


def apply_special_offer_discount(total_cost):
    if total_cost > 400:
        total_cost -= 50
    elif total_cost > 200:
        total_cost -= 20
    return total_cost


def apply_premium_surcharge(total_cost, membership_plan):
    if membership_plan.name == "Premium":
        total_cost *= 1.15  # apply 15% surcharge for premium memberships
    return total_cost


def validate_membership_plan(membership_plan, selected_features):
    if not selected_features:  # must select at least one feature
        return False
    if any(feature not in membership_plan.features for feature in selected_features):
        return False
    return True


def confirm_membership_plan(membership_plan, selected_features, total_cost):
    print("\nMembership Plan Summary:")
    print(f"Plan: {membership_plan.name}")
    print("Features:")
    for feature in selected_features:
        print(f"- {feature}")
    print(f"Total Cost: ${total_cost:.2f}")


    confirmation = input("\nConfirm membership plan (yes/no): ").strip().lower()
    if confirmation == "yes":
        return total_cost
    else:
        return -1


def main():
    print("Welcome to Gym Membership Manager!")


    display_membership_plans()
    membership_plan = select_membership_plan()
    selected_features = select_additional_features(membership_plan)
    group_size = select_group_size()


    base_cost = membership_plan.base_cost
    total_cost = calculate_total_cost(base_cost, selected_features, group_size)


    total_cost = apply_group_discount(total_cost, group_size)
    total_cost = apply_special_offer_discount(total_cost)
    total_cost = apply_premium_surcharge(total_cost, membership_plan)


    if not validate_membership_plan(membership_plan, selected_features):
        print("\nInvalid selection. Please start over.")
        return -1


    confirmed_cost = confirm_membership_plan(membership_plan, selected_features, total_cost)
    if confirmed_cost == -1:
        print("Membership plan canceled.")
    else:
        print(f"\nTotal Cost: ${confirmed_cost:.2f}")


if __name__ == "__main__":
    main()


