motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("harley")
print(motorcycles)

motorcycles.insert(1, "kawasaki")
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped = motorcycles.pop()
print("Removed:", popped)
print(motorcycles)

motorcycles.remove("kawasaki")
print(motorcycles)
