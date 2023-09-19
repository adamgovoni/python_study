import imagehash
from PIL import Image

# Calculate hash of a given image
def calculate_image_hash(image_path):
    img = Image.open(image_path)
    hash_value = imagehash.average_hash(img)
    return hash_value

# Hash values for reference images
reference_image_hash = calculate_image_hash("reference_image.jpg")

# Compare hash values to calculate similarity
def calculate_similarity(hash1, hash2):
    return 1 - (hash1 - hash2) / len(hash1.hash) ** 2

# Compare an image with the reference image
def compare_to_reference(image_path):
    image_hash = calculate_image_hash(image_path)
    similarity = calculate_similarity(reference_image_hash, image_hash)
    return similarity

# List of images to compare
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Compare each image and print similarity
for path in image_paths:
    similarity = compare_to_reference(path)
    print(f"Similarity with {path}: {similarity:.2%}")
