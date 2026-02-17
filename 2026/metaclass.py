class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, host="localhost"):
        self.host = host
        print(f"Connected to {self.host}")

# Test
db1 = DatabaseConnection("db1.example.com")
db2 = DatabaseConnection("db2.example.com")
print(db1 is db2)  # True (same instance)
print(db1.host)     # "db1.example.com" (first arg used)
