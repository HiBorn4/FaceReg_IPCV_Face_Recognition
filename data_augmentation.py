from keras.preprocessing.image import ImageDataGenerator

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# Load and augment training images
train_generator = datagen.flow_from_directory(
    'train_data/21bcs001',
    target_size=(1080, 1920),
    batch_size=32,
    class_mode='categorical',
    shuffle=True)

# Save augmented images
