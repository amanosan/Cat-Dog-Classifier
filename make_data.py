import os
import shutil

cwd = os.getcwd()
original_dataset = os.path.join(cwd, 'original_data')
base_dir = os.path.join(cwd, "cat_dogs_small")

# print(original_dataset)
# print(base_dir)
os.mkdir(base_dir)

#  creating the train, validation and test folders
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')
os.mkdir(train_dir)
os.mkdir(validation_dir)
os.mkdir(test_dir)

# Now creating folders for cats and dogs
cat_training = os.path.join(train_dir, "cat")
os.mkdir(cat_training)
dog_training = os.path.join(train_dir, 'dog')
os.mkdir(dog_training)

cat_validation = os.path.join(validation_dir, 'cat')
os.mkdir(cat_validation)
dog_validation = os.path.join(validation_dir, 'dog')
os.mkdir(dog_validation)

cat_test = os.path.join(test_dir, 'cat')
os.mkdir(cat_test)
dog_test = os.path.join(test_dir, 'dog')
os.mkdir(dog_test)

# Copying the Cat Images
# copying to the training folder
cat_names = [f"cat.{i}.jpg" for i in range(1000)]
for cat_name in cat_names:
    src = os.path.join(original_dataset, cat_name)
    dst = os.path.join(cat_training, cat_name)
    shutil.copyfile(src, dst)

# copying to the validation folder
cat_names = [f"cat.{i}.jpg" for i in range(1000, 1500)]
for cat_name in cat_names:
    src = os.path.join(original_dataset, cat_name)
    dst = os.path.join(cat_validation, cat_name)
    shutil.copyfile(src, dst)

# copying to the test folder
cat_names = [f"cat.{i}.jpg" for i in range(1500, 2000)]
for cat_name in cat_names:
    src = os.path.join(original_dataset, cat_name)
    dst = os.path.join(cat_test, cat_name)
    shutil.copyfile(src, dst)

# Now copying Dog Images
dog_names = [f"dog.{i}.jpg" for i in range(1000)]
for dog in dog_names:
    src = os.path.join(original_dataset, dog)
    dst = os.path.join(dog_training, dog)
    shutil.copyfile(src, dst)

dog_names = [f"dog.{i}.jpg" for i in range(1000, 1500)]
for dog in dog_names:
    src = os.path.join(original_dataset, dog)
    dst = os.path.join(dog_validation, dog)
    shutil.copyfile(src, dst)

dog_names = [f"dog.{i}.jpg" for i in range(1500, 2000)]
for dog in dog_names:
    src = os.path.join(original_dataset, dog)
    dst = os.path.join(dog_test, dog)
    shutil.copyfile(src, dst)

# Checking if copying was successful
print(f"Cat Training: {len(os.listdir(cat_training))}")
print(f"Cat Validation: {len(os.listdir(cat_validation))}")
print(f"Cat Test: {len(os.listdir(cat_test))}")
print(f"Dog Training: {len(os.listdir(dog_training))}")
print(f"Dog Validation: {len(os.listdir(dog_validation))}")
print(f"Dog Test: {len(os.listdir(dog_test))}")
