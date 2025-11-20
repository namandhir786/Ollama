from sentence_transformers import SentenceTransformer
import psycopg2

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# PostgreSQL connection
connection = psycopg2.connect(
    host="localhost",
    database="demo_db",
    user="postgres",
    password="Naman2003"
)
cursor = connection.cursor()

user_input = input("Enter a book name: ")

# Generate embedding
query_emb = model.encode(user_input).tolist()

# Convert Python list → pgvector format string
query_vector = "[" + ",".join(str(x) for x in query_emb) + "]"

# Query using cosine distance (<->)
cursor.execute("""
    SELECT book_name, uuid, embedding <-> %s AS distance
    FROM books
    ORDER BY embedding <-> %s
    LIMIT 1;
""", (query_vector, query_vector))

result = cursor.fetchone()

if result:
    print("\nMost similar book:")
    print("Book Name:", result[0])
    print("UUID:", result[1])
    print("Cosine Distance:", result[2])
else:
    print("No matching books found.")

cursor.close()
connection.close()
