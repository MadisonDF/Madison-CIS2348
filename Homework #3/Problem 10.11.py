# Madison Fletcher
# 1868748
class FoodItem:

    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    food_item = FoodItem()

    food_name = str(input())
    grams_fat = float(input())
    grams_carbs = float(input())
    grams_protein = float(input())
    servings = float(input())

    food_item2 = FoodItem(food_name, grams_fat, grams_carbs, grams_protein)

    food_item.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'.format(servings, food_item.get_calories(servings)))

    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, food_item2.get_calories(servings)))
    
