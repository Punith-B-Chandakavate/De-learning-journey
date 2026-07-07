# 🔒 ACID Properties in Database Transactions

⬅️ [Back to Unity Catalog
](13_Unity_Catalog.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- What are ACID Properties?
- Atomicity
- Consistency
- Isolation
- Durability
- ACID Transaction Flow
- ACID vs Non-ACID
- Real-World Example
- Real-World Use Cases
- Best Practices
- Interview Questions
- Summary
- Key Takeaways
- Next Topic

---

# 📖 Overview

**ACID** is a set of four fundamental properties that ensure database transactions are processed **reliably, consistently, and safely**.

ACID guarantees that every transaction maintains data integrity, even when multiple users access the database simultaneously or when unexpected failures occur.

The four ACID properties are:

- ⚛️ **Atomicity**
- ✅ **Consistency**
- 🔒 **Isolation**
- 💾 **Durability**

Together, these properties form the foundation of modern relational database systems such as **PostgreSQL**, **MySQL**, **Oracle**, **SQL Server**, and transactional storage engines like **Delta Lake**.

---

# 🎯 Learning Objectives

After completing this guide, you will understand:

- What ACID properties are
- Why ACID is important
- The four ACID properties
- Transaction lifecycle
- Real-world transaction examples
- ACID vs Non-ACID databases
- Best practices for transactional systems

---

# 🔒 What are ACID Properties?

**ACID** represents a set of rules that every reliable database transaction should follow.

| Property       | Meaning                                 |
| -------------- | --------------------------------------- |
| ⚛️ Atomicity | All operations succeed or all fail      |
| ✅ Consistency | Database always remains valid           |
| 🔒 Isolation   | Concurrent transactions don't interfere |
| 💾 Durability  | Committed data is never lost            |

These guarantees ensure that database transactions remain reliable even during failures or concurrent execution.

---

# ⚛️ Atomicity

## Definition

**Atomicity** ensures that a transaction is treated as a single indivisible unit.

Either:

- All operations succeed

or

- All operations fail

No partial updates are allowed.

---

## Example

```sql
BEGIN TRANSACTION;

UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE account_id = 2;

COMMIT;
```

If the second update fails,

Spark/Database automatically performs

```sql
ROLLBACK;
```

Both updates are undone.

---

## Benefits

- Prevents partial transactions
- Maintains data integrity
- Supports rollback during failures

---

# ✅ Consistency

## Definition

**Consistency** guarantees that every transaction moves the database from one valid state to another while preserving all constraints and business rules.

---

## Example

```sql
CREATE TABLE accounts (

    account_id INT PRIMARY KEY,

    account_type VARCHAR(20),

    balance DECIMAL(10,2),

    CONSTRAINT positive_balance
    CHECK(balance >= 0)

);
```

The database will reject transactions that violate the constraint.

Example

```text
Balance = -500

❌ Transaction Rejected
```

---

## Benefits

- Preserves business rules
- Prevents invalid data
- Maintains database integrity

---

# 🔒 Isolation

## Definition

**Isolation** ensures that multiple transactions execute independently without affecting one another.

Each transaction behaves as if it is the only transaction running.

---

## Example

Suppose two users transfer money simultaneously.

Without isolation:

```text
Transaction A

↓

Reads Balance

↓

Transaction B

↓

Updates Balance

↓

Incorrect Result
```

With isolation:

```text
Transaction A

↓

Locks Data

↓

Completes

↓

Transaction B Starts
```

---

## Benefits

- Prevents dirty reads
- Prevents lost updates
- Maintains concurrent consistency

---

# 💾 Durability

## Definition

**Durability** guarantees that once a transaction has been committed, its changes are permanently stored.

Even if the database crashes immediately afterward, the committed data remains safe.

---

## Example

```text
BEGIN

↓

UPDATE

↓

COMMIT

↓

Power Failure

↓

Restart Database

↓

Data Still Exists
```

---

## Benefits

- Permanent data storage
- Crash recovery
- Reliable transactions

---

# 🔄 ACID Transaction Flow

![ACID Transaction Flow](images/ACID_Transaction_Flow.png)

---

# ⚖️ ACID vs Non-ACID

| Feature             | ACID Database                 | Non-ACID Database                 |
| ------------------- | ----------------------------- | --------------------------------- |
| Atomic Transactions | ✅                            | Limited                           |
| Data Consistency    | ✅                            | Eventual                          |
| Concurrent Safety   | ✅                            | Depends                           |
| Crash Recovery      | ✅                            | Varies                            |
| Strong Integrity    | ✅                            | Lower                             |
| Examples            | PostgreSQL, MySQL, SQL Server | MongoDB, Cassandra (configurable) |

---

# 🌍 Real-World Example

Consider a bank transfer of ₹100 from Account A to Account B.

### ⚛️ Atomicity

Both debit and credit happen together.

Otherwise, both are rolled back.

---

### ✅ Consistency

Account balances remain valid.

Business rules are never violated.

---

### 🔒 Isolation

Other users cannot interfere while the transfer is being processed.

---

### 💾 Durability

Once confirmed, the transfer remains permanent even if the system crashes.

---

# 🌎 Real-World Use Cases

| Application       | Why ACID Matters   |
| ----------------- | ------------------ |
| Banking           | Money transfers    |
| E-Commerce        | Order processing   |
| Healthcare        | Patient records    |
| Airline Booking   | Seat reservations  |
| Inventory         | Stock management   |
| Financial Systems | Payment processing |

---

# 💡 Best Practices

- ✅ Use ACID-compliant databases for financial and business-critical applications.
- ✅ Keep transactions as short as possible to reduce locking and improve concurrency.
- ✅ Always use **COMMIT** after successful transactions and **ROLLBACK** when errors occur.
- ✅ Define **PRIMARY KEY**, **FOREIGN KEY**, and **CHECK** constraints to maintain consistency.
- ✅ Choose the appropriate transaction isolation level based on application requirements.
- ✅ Monitor long-running transactions to prevent blocking and deadlocks.
- ✅ Regularly back up transaction logs to support durability and disaster recovery.
- ✅ Test transaction behavior under concurrent workloads before deploying to production.

---

# 🎤 Interview Questions

### 1. What does ACID stand for?

Atomicity, Consistency, Isolation, Durability.

---

### 2. What is Atomicity?

It ensures that a transaction either completes entirely or is rolled back completely.

---

### 3. What is Consistency?

It guarantees that every transaction moves the database from one valid state to another.

---

### 4. What is Isolation?

It prevents concurrent transactions from interfering with one another.

---

### 5. What is Durability?

Committed transactions remain permanent even after a system crash.

---

### 6. Why is ACID important?

It ensures reliable, consistent, and fault-tolerant transaction processing.

---

### 7. Which databases support ACID?

PostgreSQL, MySQL (InnoDB), SQL Server, Oracle, and Delta Lake.

---

### 8. What happens if a transaction fails before COMMIT?

The database performs a **ROLLBACK**, undoing all changes.

---

### 9. Which ACID property prevents partial updates?

Atomicity.

---

### 10. Which ACID property protects committed data after a crash?

Durability.

---

# 📊 Summary

| Property       | Purpose                                 |
| -------------- | --------------------------------------- |
| ⚛️ Atomicity | All operations succeed or fail together |
| ✅ Consistency | Maintains valid database state          |
| 🔒 Isolation   | Prevents transaction interference       |
| 💾 Durability  | Preserves committed data permanently    |

---

# 🎯 Key Takeaways

- **Atomicity** ensures that every transaction is executed completely or not at all.
- **Consistency** guarantees that all database rules and constraints are preserved after every transaction.
- **Isolation** allows concurrent transactions to execute safely without interfering with one another.
- **Durability** ensures that committed transactions remain permanent, even after system failures.
- Together, the **ACID properties** provide reliable, fault-tolerant, and trustworthy transaction management.
- ACID is essential for applications requiring strong consistency, such as banking, e-commerce, healthcare, and financial systems.
- Understanding ACID is fundamental for designing scalable, secure, and production-ready database applications.

---

# 📚 Next Topic

➡️ [Time Travel](15_Time_Travel.md)