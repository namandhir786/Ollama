from sentence_transformers import SentenceTransformer
import psycopg2
import uuid

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="demo_db",
    user="postgres",
    password="Naman2003"
)
cursor = connection.cursor()

# Read book list
books = []
with open("books.txt", "r") as f:
    for line in f:
        book_uuid, name = line.strip().split(",", 1)
        books.append((book_uuid, name.strip()))

# Insert with embeddings
for book_uuid, name in books:
    emb = model.encode(name).tolist()

    cursor.execute("""
        INSERT INTO books (uuid, book_name, embedding)
        VALUES (%s, %s, %s)
    """, (book_uuid, name, emb))

connection.commit()
cursor.close()
connection.close()

print("Inserted all books successfully!")
