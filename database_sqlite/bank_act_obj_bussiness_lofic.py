import sqlite3

class BankAccount:
    """Represents a Bank Account object with business logic."""

    def __init__(self, owner, balance=0.0, acc_id=None):
        self.acc_id = acc_id   
        self.owner = owner
        self.balance = balance

    # OBJECT BUSINESS LOGIC: Deposit Money
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        self.balance += amount
        print(f"💵 Deposited ${amount}. New Balance: ${self.balance}")
        return True

    # OBJECT BUSINESS LOGIC: Withdraw Money
    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds! Withdrawal cancelled.")
            return False
        self.balance -= amount
        print(f"💸 Withdrew ${amount}. Remaining Balance: ${self.balance}")
        return True


class BankDatabase:
    """Handles SQLite persistence for BankAccount objects."""

    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner TEXT NOT NULL,
                balance REAL NOT NULL
            )
        """)
        self.conn.commit()

    def save_account(self, account: BankAccount):
        """Saves a BankAccount object to the database."""
        if account.acc_id is None:
            query = "INSERT INTO accounts (owner, balance) VALUES (?, ?)"
            self.cursor.execute(query, (account.owner, account.balance))
            self.conn.commit()
            account.acc_id = self.cursor.lastrowid
            print(f"Created DB Record for {account.owner} (ID: {account.acc_id})")
        else:
            query = "UPDATE accounts SET balance = ? WHERE id = ?"
            self.cursor.execute(query, (account.balance, account.acc_id))
            self.conn.commit()
            print(f"Synced DB Balance for {account.owner}: ${account.balance}")

    def load_account(self, acc_id):
        """Loads data from DB and returns a BankAccount object."""
        self.cursor.execute("SELECT owner, balance FROM accounts WHERE id = ?", (acc_id,))
        row = self.cursor.fetchone()
        if row:
            return BankAccount(owner=row[0], balance=row[1], acc_id=acc_id)
        return None


# -------------------------------------------------------------
# HOW IT WORKS IN PRACTICE
# -------------------------------------------------------------
if __name__ == "__main__":
    bank_db = BankDatabase("bank.db")

    # 1. Create a BankAccount object with $100
    account = BankAccount("John Doe", balance=100.0)
    bank_db.save_account(account)

    # 2. Perform business logic on object (Deposit $500)
    print("\n--- Depositing Money ---")
    if account.deposit(500.0):
        bank_db.save_account(account)  # Sync new balance to DB

    # 3. Attempt invalid withdrawal (Overdraft check inside object)
    print("\n--- Attempting Overdraft ---")
    if account.withdraw(1000.0):
        bank_db.save_account(account)  # Will not run because withdraw fails!

    # 4. Valid withdrawal
    print("\n--- Valid Withdrawal ---")
    if account.withdraw(200.0):
        bank_db.save_account(account)  # Sync to DB
