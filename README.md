# Flip Data Engineer Assessment Test

---

1. Separation of Routes and Business Logic: I separate route (`main.py`) with business logic (`src/pokemon_service.py`) because this improves code readibility, maintainability, and testability.
2. Use of RDBMS to Store Data: I use PostgreSQL to store data of normalized `effect_entries` in `pokemon_effects` table. I define `language`'s column type as `json` to ensure data fidelity.
3. Implementation of Pydantic's Validation: I validate user's request to ensure strict data integrity before processing.
4. Asynchronous Programming Utilization: I use `async/await` since the task requires hitting an external API (PokeAPI).
5. Containerization and Portability: This approach ensures that the code can be run on any machines.
6. SQLAlchemy 2.0 Usage: This provides modern database translator, which claims of reducing the risk of SQL injection.
