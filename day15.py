class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int
    amount: int

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
        self.amount = 0

    def get_scores(self):
        return {
            "capacity": self.amount * self.capacity,
            "durability": self.amount * self.durability,
            "flavor": self.amount * self.flavor,
            "texture": self.amount * self.texture,
            "calories":self.amount*self.calories
        }


def determine_ingredient_score(list_ingredients):
    scores = {
        "capacity": 0,
        "durability": 0,
        "flavor": 0,
        "texture": 0
    }
    total_calories = 0
    for ingredient in list_ingredients:
        current_scores = ingredient.get_scores()
        for k in scores.keys():
            scores[k] += current_scores[k]
        total_calories += current_scores['calories']
    total = 1
    for val in list(scores.values()):
        if val < 0:
            val = 0
        total *= val
    return total, total_calories


if __name__ == "__main__":
    raw_ingredients = [
        Ingredient("Sprinkles", 5, -1, 0, 0, 5),
        Ingredient("PeanutButter", -1, 3, 0, 0, 1),
        Ingredient("Frosting", 0, -1, 4, 0, 6),
        Ingredient("Sugar", -1, 0, 0, 2, 8)
    ]
    best_caloric_score = 0
    best_score = 0
    for a in range(0, 100):
        for b in range(0, 100):
            for c in range(0, 100):
                for d in range(0, 100):
                    if a + b + c + d == 100:
                        raw_ingredients[0].amount = a
                        raw_ingredients[1].amount = b
                        raw_ingredients[2].amount = c
                        raw_ingredients[3].amount = d
                        total_score, _calories = determine_ingredient_score(raw_ingredients)
                        if _calories == 500:
                            if total_score > best_caloric_score:
                                best_caloric_score = total_score
                        if total_score > best_score:
                            best_score = total_score
                            print(a,b,c,d)
    print(best_score)
    print(best_caloric_score)
