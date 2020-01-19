from foodProducer import FoodProducer

foodData = FoodProducer()

c = 0
for food in foodData.foods:
    c += 1
    print(c)
    food.findImage(food.name)

foodData.save()
print("Finished")
